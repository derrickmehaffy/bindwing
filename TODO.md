# Bindwing — TODO

Working punch-list. `[ ]` open · `[x]` done · `[~]` in progress. Roadmap for *games/devices* lives in `DEVICES.md`.

## 🐞 Fixes (from testing)
_Add items here as we find them; we'll check them off as we go._
- [ ]

## ✨ Editor polish (near-term)
- [x] **Live controller input** (Gamepad API): press-to-highlight + press-to-bind, device auto-match/add, baseline axis detection, POV-hat decode, 64/128-button multi-collection merge
- [x] 2D list is the default view
- [ ] Live: make button-bank ordering **deterministic** — currently assumes higher HID index = primary bank; add auto-detect (by axis activity) or a per-device "swap banks" toggle
- [ ] Conflict handling: option to **auto-replace** a same-mode conflict instead of only flagging it
- [ ] **Author Elite modifiers in-app** (currently display-only) — pick a modifier button when binding, write `<Modifier>`
- [ ] Show **physical button names** on markers/2D tiles (e.g. "Trigger", "Pinky") — source from EDRefCard item comments
- [ ] Verify the viewport toolbar doesn't crowd the model on small/folded screens
- [ ] Theme: confirm dark is the default on a fresh load; consider honoring `prefers-color-scheme`
- [ ] Empty/edge states pass (no device, unknown control, hat/axis in 2D)

## 🎮 Games (see DEVICES.md for detail)
- [x] Elite Dangerous (`.binds`)
- [ ] Star Citizen (XML actionmaps) — next adapter
- [ ] X4: Foundations
- [ ] Flight sims (IL-2, Falcon BMS, X-Plane), then DCS / MSFS

## 🕹️ Devices
- [x] VKB right stick `231D0200`, left EVO `231D0201`, STECS Max `231D012E`, T-Rudder `231D011F` — all bindable (2D list)
- [ ] Real 3D scans (POP 4) to replace the placeholder model, per device

## 📦 Before making the repo public
- [ ] Rename project folder → `bindwing` (once the live server isn't tied to it)
- [ ] Swap `sample.binds` for a curated demo (currently a personal profile)
- [ ] Device art / scan licensing — ship own scans or get vendor OK (see DEVICES.md)
- [ ] Push to GitHub (install `gh`, or add a remote)
- [ ] Donations/funding model for the scan queue
