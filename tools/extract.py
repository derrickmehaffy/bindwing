#!/usr/bin/env python3
"""Extract EDRefCard's Python data (control catalog + device coordinate maps +
device table) into portable JSON for Bindwing.

Usage:
    py tools/extract.py [path-to-edrefcard-clone]

Defaults the EDRefCard location to a sibling folder `../edrefcard2` next to the
repo. Clone it from https://github.com/richardbuckle/EDRefCard (or the edrefcard2
fork) first. Outputs to data/ and images/ in the repo root.
"""
import json, sys, shutil
from pathlib import Path

ROOT  = Path(__file__).resolve().parent.parent            # repo root
EDREF = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT.parent / "edrefcard2"
SCRIPTS = EDREF / "www" / "scripts"
RES     = EDREF / "www" / "res"
OUT     = ROOT / "data"
IMG     = ROOT / "images"

if not SCRIPTS.exists():
    sys.exit(f"EDRefCard scripts not found at {SCRIPTS}\n"
             f"Clone EDRefCard and pass its path: py tools/extract.py <path-to-edrefcard>")

OUT.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(SCRIPTS))
import controlsData, bindingsData

controls  = controlsData.controls
supported = bindingsData.supportedDevices    # name -> {Template, HandledDevices, ...}
hotas     = bindingsData.hotasDetails         # deviceId -> { item -> {x,y,width,height,Type} }

# 1) Control catalog (ordered list)
catalog = [{
    "control": key, "name": c.get("Name", key), "group": c.get("Group", ""),
    "category": c.get("Category", ""), "order": c.get("Order", 0),
    "type": c.get("Type", "Digital"), "hasAnalogue": c.get("HasAnalogue", False),
} for key, c in controls.items()]
(OUT / "controls.json").write_text(json.dumps(catalog, indent=1), encoding="utf-8")

# 2) Supported-device table + coordinate maps
devices = {name: {
    "name": name, "template": meta.get("Template"),
    "handledDevices": meta.get("HandledDevices", []), "keyDevices": meta.get("KeyDevices", []),
} for name, meta in supported.items()}
(OUT / "devices.json").write_text(json.dumps(devices, indent=1), encoding="utf-8")
(OUT / "coords.json").write_text(json.dumps(hotas, indent=1), encoding="utf-8")

# 3) Single JS bundle so the app runs over file:// or http:// with no fetch/CORS
(OUT / "data.js").write_text(
    "window.ED_DATA = " + json.dumps({"controls": catalog, "devices": devices, "coords": hotas}) + ";\n",
    encoding="utf-8")

# 4) Copy VKB / gladiator device images (used by the 2D editor). Not committed — see .gitignore.
copied = []
if RES.exists():
    for jpg in RES.glob("*.jpg"):
        if "vkb" in jpg.name.lower() or "gladiator" in jpg.name.lower():
            shutil.copy(jpg, IMG / jpg.name); copied.append(jpg.name)

print(f"controls: {len(catalog)} | devices: {len(devices)} | coord maps: {len(hotas)} | images: {len(copied)}")
