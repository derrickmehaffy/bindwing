# Bindwing

A visual, **cross-game HOTAS bind editor**. Load your controller bindings, see them mapped onto a 3D (or 2D) model of your actual device, rebind by clicking, and export a valid bind file back to the game.

Started for **Elite Dangerous**; built to grow into a **device-first, games-as-plugins** tool (Star Citizen, X4, DCS, and more) — scan/model a device once, use it across every game.

> **Status:** early prototype. Fully functional for **Elite Dangerous** (`.binds`). 3D device models are stylized placeholders until real scans are added.

## Run it

Requires **Python 3**. No build step, no packages to install (Three.js is vendored).

```
py serve.py
```

Open <http://localhost:8777/> (redirects to the 3D editor). To reach it from another device on your LAN (e.g. a phone), browse to `http://<this-pc-ip>:8777/` and allow port 8777 through your firewall.

## Layout

| Path | What it is |
|---|---|
| `viewer3d.html` | Main **3D editor** (Three.js): orbit a device model, click markers to bind, export `.binds`. |
| `editor2d.html` | Earlier **2D / list editor**. |
| `index.html` | Redirects to the 3D editor. |
| `serve.py` | Tiny no-cache static server (binds `0.0.0.0:8777`). |
| `data/` | Control catalog + device coordinate maps (JSON), derived from **EDRefCard** (MIT — see `CREDITS.md`). |
| `vendor/` | Three.js (MIT). |
| `tools/extract.py` | Regenerate `data/` (+ `images/`) from a local EDRefCard clone. |
| `tools/verify.py` | Headless check of the bind-parsing logic against a `.binds`. |
| `DEVICES.md` | Device wishlist + asset-sourcing plan. |
| `sample.binds` | Demo Elite Dangerous profile, auto-loaded on startup. |

## Roadmap

See **`DEVICES.md`**. Space-sim first wave: **Elite ✅ → Star Citizen → X4: Foundations**, then flight sims (IL-2, Falcon BMS, X-Plane), then the deep ones (DCS, MSFS). Each game is an adapter (its control catalog + bind reader/writer) over the shared device layer.

## Before making this repo public — TODO

- Swap `sample.binds` for a curated demo if you'd rather not ship a personal profile.
- Don't bundle third-party device art or scans — ship your own scans or get vendor permission (see `DEVICES.md`).
- Choose a license for **device model assets** separately from the code.

## License

Code: **MIT** (see `LICENSE`). Reuses EDRefCard (MIT) and Three.js (MIT) — see `CREDITS.md`.
Not affiliated with or endorsed by Frontier Developments, VKB, or any hardware maker; all trademarks belong to their owners.
