#!/usr/bin/env python3
"""Headless check of the bind-parsing logic: replicate the app's bindingsFor()
against the extracted coords + a .binds file, to confirm hotspots resolve.

Usage: py tools/verify.py [path-to.binds]   (default: sample.binds in repo root)
"""
import json, sys, xml.etree.ElementTree as ET
from pathlib import Path

ROOT   = Path(__file__).resolve().parent.parent
binds  = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "sample.binds"
coords = json.loads((ROOT / "data" / "coords.json").read_text(encoding="utf-8"))
controls = {c["control"]: c for c in json.loads((ROOT / "data" / "controls.json").read_text(encoding="utf-8"))}
root = ET.parse(binds).getroot()

def bindings_for(dev, key):
    hits = []
    for ctrl in root:
        for slot in ctrl:                         # Primary / Secondary / Binding / Modifier
            if slot.get("Device") == dev and slot.get("Key") == key:
                hits.append((ctrl.tag, slot.tag))
    return hits

used_devices = sorted({el.get("Device") for el in root.iter()
                       if el.get("Device") and el.get("Device", "")[:1].isdigit()})
for dev in used_devices:
    items = coords.get(dev)
    keys = {slot.get("Key") for ctrl in root for slot in ctrl if slot.get("Device") == dev and slot.get("Key")}
    print(f"\n=== {dev} — {'coords: '+str(len([k for k in items if k!='displayName'])) if items else 'NO coord map'} ===")
    print(f"  keys bound in file: {sorted(keys)}")
    if items:
        for key in list(items)[:6]:
            if key == "displayName":
                continue
            b = bindings_for(dev, key)
            if b:
                names = " / ".join(controls.get(c, {}).get("name", c) for c, _ in b)
                print(f"    {key:16s} -> {names}")
