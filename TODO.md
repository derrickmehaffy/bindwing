# Bindwing — TODO

Working punch-list. `[ ]` open · `[x]` done · `[~]` in progress. Roadmap for *games/devices* lives in `DEVICES.md`.

## 🐞 Fixes (from testing)
_Add items here as we find them; we'll check them off as we go._
- [x] 2D view showed all 64 buttons for every device — now built from each device's real input map (`D.coords[id]`); T-Rudder shows only its 3 axes. Unknown devices still get the full generic set.
- [x] Newer-firmware VKB PIDs unmapped by EDRefCard — `COORD_ALIAS` maps hardware PID → reference coord key (T-Rudder `231D011F`→`T-Rudder`).
- [x] Live mode created a phantom device (left grip's raw HID PID `012E` ≠ Elite's virtual-controller PID `0201`) → rendered nothing. `DEVICE_ALIAS` normalizes HID→bind PID; `ensureDeviceOption` gated to known devices only.
- [x] Persist settings across refresh — theme (pre-paint inline script, no dark→light flash), Live on/off, loaded `.binds` text + filename, selected device, and 2D/3D view, all via `localStorage`; restore on load, sample only when nothing saved. (Fixed a TDZ crash: restore must run at the end of the module, after `stageView` is initialized, since it calls `refresh2D()`.)
- [ ] Generalize device-identity aliasing before public — the `012E`→`0201` map is rig-specific. Auto-detect (VID match + input signature) or make it user-editable. Also handle swap-in devices sharing a PID (user swaps STECS ⇄ EVO left grip; confirm STECS PID when next connected).
- [ ]

## 🎨 Design pass (v0.5)
- [x] **Typography** — vendored Exo 2 (Elite's own typeface, `vendor/fonts/`) for UI + Orbitron for the wordmark; new `--ui`/`--display` tokens.
- [x] **Device rail** (left sidebar) — one card per device with 2-line name, coverage meter (bound/total), PID, and conflict count; active card glows + pulses on live auto-switch. Vertical to scale for many devices; horizontal strip on mobile.
- [x] **Filter bar** in 2D — All / Bound / Unbound / Conflicts, with a bound/total readout; dims non-matching hotspots, filters the list.
- [x] **Conflict visualization** — red rings on diagram hotspots + list tiles; per-device conflict count in the rail (modifier-aware).
- [x] **Keyboard + Mouse devices** — GameGlass/manual binds now show as devices (list-only, no diagram); inventory = only the keys actually bound; coverage/conflicts computed.
- [x] **Keyboard shortcuts** — `/` search · `Esc` clear/close · `2`/`3` views · `L` live · `A B U C` filters · `?` help overlay.
- [x] Fixed overflow — device-card names wrap (2 lines). Moved the status readout out of the cramped header into a full-width **bottom status bar** (MFD line) with a pulsing live-indicator dot — no more mid-sentence truncation.
- [x] **Dark-mode diagram** framed as a physical reference card (matte + shadow); **Print/PDF** (white bg, prints active subsystem); `1·2·3` = List·Diagram·3D.
- [x] **Live auto-switch fix** — switching devices now needs a *deliberate* signal (button rising edge or firm >0.55 axis deflection), not axis noise; the left grip's many idle axes no longer steal focus. Excludes Keyboard/Mouse (won't fight typing/clicking). Covers axis-only pedals via the firm-deflection path.
- [x] **Live input debug modal** (🐞 / `D`) — lists each connected controller (name, PID, HID alias, collections, btn/axis counts, raw Chrome id) + a rolling event log (press/axis/switch). Invaluable for diagnosing VKB multi-collection / PID quirks.
- [x] **3D work-in-progress banner** — hazard-stripe bar in the viewport; steers users to 2D for accurate binding until real scans land.
- [x] **Dark-mode diagram** — can't recolor the baked-light EDRefCard JPG; instead frame it as a physical reference card (cream matte + drop shadow) so the white reads as intentional.
- [x] **Print / PDF** — `⎙ Print` button + `@media print` strips app chrome and lays out just the current diagram or list (landscape, color-exact); print-only title for list.
- [x] **Shortcuts 1·2·3** = List · Diagram · 3D (was 2/3); `set2dMode()` helper.
- [x] **Subsystem/channel filter** — legend of the Elite control groups actually present on the device (Ship/SRV/On-Foot/Fighter/UI/Camera…), colored by channel with counts; click to isolate that subsystem on the diagram/list (dims the rest). Combines with bound/unbound/conflict filter and with print (prints only the active subsystem — one channel per page).
- [ ] Ideas parked: hover a picker control → pulse where it's bound; export diff/confirm; "jump to next conflict"; rename keyboard group "Buttons"→"Keys".

## 🎮 Multi-game architecture
- [x] **Game selector** in header (`GAMES` config) — Elite Dangerous live; Star Citizen / X4 / DCS / MSFS shown as "— soon" (selecting one shows a coming-soon status + reverts). Sets `html[data-game]` and reserves a per-game `accent` for future theming.
- [ ] Per-game **accent themes** (Elite amber / SC blue / X4 teal …) via `html[data-game=…]` token overrides — groundwork laid, wire up when each adapter lands.
- [ ] Each game = adapter: control catalog + bind reader/writer (see DEVICES.md rollout order). Print already defaults to white bg (ink-saving) per request.

## 🎨 Design pass 2 (top bar) — v0.6
- [x] **Top-bar redesign** — flat 13-control toolbar → "MFD bezel": 3 quiet zones (brand · editing-context · tools+export), one ghost-button language, monochrome SVG line-icons (no emoji), single amber primary. Wraps to 2 rows on mobile.
- [x] **Samples picker** — data-driven from `samples.json`, surfaced in a **Profile ▾** menu (Open file… + Samples list). Currently the "Bindwing Sample"; structured to add popular-device examples (X52 Pro, T16000M, Warthog…).
- [x] Renamed `viewer3d.html`→`index.html` (app at site root); curated **Bindwing Sample** replaces the personal profile; **Sample** badge when the built-in demo is loaded.
- [x] **Example library batch 1** — authored starter profiles for **X52 Pro, T.16000M FCS, Warthog** (with EDRefCard diagram images copied in); all load with full diagrams. Fixed `loadBinds` to accept EDRefCard **name-based device IDs** (SaitekX52Pro, Warthog…), which unlocks every non-VKB device the data supports — not just these three.
- [ ] Grow further: CH Fighterstick/Combatstick, X55/X56, Virpil, WinWing; and per-game examples once other-game adapters exist.

## ✨ Editor polish (near-term)
- [x] **2D Diagram view** — EDRefCard device JPG (3840×2160) scaled to the panel with percentage-positioned hotspot `<div>`s from `coords.json`; bound/selected/live highlighting + click-to-bind, aligned to the template's own label boxes. `List ⇄ Diagram` toggle (persisted `bw-2dmode`, default diagram), falls back to List when a device has no image (T-Rudder) or the JPG 404s.
  - [x] Long control names — single-line ellipsis by default; box grows + text wraps on hover/select to reveal the full name.
  - [x] Dark-mode readability — hotspot text is fixed dark (`#1b1712`) on the always-light EDRefCard sheet, regardless of app theme.
  - [x] Overlapping hotspots — VKB hats map both button-mode (`Joy_N`) and hat-mode (`Joy_POVnDir`) keys onto the same box; empty twin was stealing clicks. Now co-located coords merge into one hotspot (active = bound key, else button-mode), highlight if any twin is bound/live. 51→39 boxes on the right stick.
- [x] **Modifier-aware conflict detection** — two same-group binds only clash if they share the same modifier signature; a control needing a held modifier no longer false-flags against an unmodified one. Shows a `+<key>` modifier badge on modified binds. (Was: Joy_12 UI Right vs Next Panel[+Joy_5] wrongly flagged.)
  - [ ] Template JPGs carry EDRefCard's baked-in "Elite: Dangerous — …" title; fine for now, replace with own/neutral art before public.
  - [ ] `images/` (EDRefCard template art) is gitignored + licensing-sensitive — resolve art licensing (see DEVICES.md) before shipping the diagram publicly.
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
