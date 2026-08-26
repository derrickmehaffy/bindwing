# Device Wishlist & Asset Plan

Two independent tracks per device:
- **Functional support** — control mapping in the editor. Works for *any* device **today** via list-mode (no model needed). ✅ = verified with a real `.binds`.
- **3D asset** — a textured model for the 3D view. Sourced in priority: **① official CAD/model from vendor → ② donation-funded scan → ③ 2D template fallback** (EDRefCard / joystick-diagrams). 3D is polish, never a blocker.

Asset legend: `official` `scan` `2D` `community(murky license)` `none`

---

## Vendor stance (reputation, reachability, official assets)

| Vendor | Stance | Official 3D? | Notes |
|---|---|---|---|
| **VKB** | 🟢 very community-friendly | none public | Ask likely = yes; may share CAD. We own the gear. |
| **Virpil (VPC)** | 🟢 enthusiast, reachable | none public | Small, community-driven — ask. |
| **MFG Crosswind** | 🟢 small/friendly | none public | Pedals; reachable maker. |
| **Honeycomb** | 🟡 neutral | none public | More MSFS than ED. |
| **Thrustmaster (Guillemot)** | 🟡 big corp, likely unresponsive | none public | Won't chase a fan model, but won't answer either. EDRefCard has shipped their images ~8 yrs = precedent. Community `.step` on GrabCAD (murky license). |
| **Logitech (Saitek)** | 🟡 big corp, likely unresponsive | none public | Same as Thrustmaster. |
| **WinWing / WinCTRL** | 🟠 check first | none public | Fast-growing; has had community/IP friction — read the room before bundling. |
| **Moza** | 🟡 newer entrant | none public | New flight line; unproven stance. |
| **CH Products** | 🟡 legacy | none public | Older gear, small ED user base now. |

Policy for all: ship models under an unofficial/fan license, offer de-branded textures, per-device provenance, honor takedowns. Ask friendly vendors first; big/silent vendors rely on precedent + takedown-readiness; sketchy-rep vendors → 2D only / user-supplied scans.

---

## Priority backlog

### Tier 1 — most common in Elite Dangerous
| Device | Vendor | Functional | 3D asset | Status / next |
|---|---|---|---|---|
| Gladiator NXT / EVO (R/L) | VKB | ✅ (own binds) | scan (own gear) | placeholder in app; scan when POP4 arrives |
| STECS Mk.II Max | VKB | ✅ | scan | list-mode works; scan pending |
| T-Rudder Mk.V | VKB | ✅ | scan | list-mode works; scan pending |
| T.16000M / FCS | Thrustmaster | ☐ | ask→scan | very common budget stick |
| TWCS Throttle | Thrustmaster | ☐ | ask→scan | pairs with T.16000M |
| HOTAS Warthog (stick+throttle) | Thrustmaster | ☐ | ask→scan | popular high-end |
| X52 / X52 Pro | Logitech/Saitek | ☐ | ask→scan | huge ED install base |
| X56 Rhino | Logitech/Saitek | ☐ | ask→scan | popular HOTAS |
| Xbox / generic gamepad | — | ✅ (generic) | n/a | no model needed |

### Tier 2
| Device | Vendor | Functional | 3D asset | Status / next |
|---|---|---|---|---|
| Constellation Alpha/Delta + WarBRD/base | Virpil | ☐ | ask→scan | |
| MongoosT-50 CM3 Throttle | Virpil | ☐ | ask→scan | |
| TCA Sidestick + Quadrant (Airbus/Boeing) | Thrustmaster | ☐ | ask→scan | |
| T-Flight HOTAS X / 4 / One | Thrustmaster | ☐ | scan | cheap, very common |
| Orion 2 HOTAS (F16/F18) | WinWing | ☐ | check→2D | verify vendor stance first |
| Fighterstick / Pro Throttle / Pro Pedals | CH Products | ☐ | 2D | legacy |
| Alpha Yoke / Bravo Throttle | Honeycomb | ☐ | ask→scan | MSFS-leaning |
| Crosswind V3 pedals | MFG | ☐ | ask→scan | |
| AB9 base + grips | Moza | ☐ | check→scan | new |

---

## Donation-funded scan queue
For devices where **no official asset** is granted, accept donations earmarked to **buy the gear, scan it (POP 4), and add it**. Keep this transparent:
- Public queue (this list) with a "funded / not funded" flag per device.
- Rough cost note per device (hardware price) so backers know the target.
- Once scanned, the model is added and the device marked done.

## Asset resources
- **Ask the vendor** (best — clean license, maybe official CAD/renders).
- **Own/donated hardware → POP 4 scan → GLB** (accurate + textured).
- **2D fallback:** [EDRefCard](https://github.com/richardbuckle/EDRefCard) images (MIT, attribute) · [joystick-diagrams templates](https://joystick-diagrams.com/templates/) (SVG, many devices — check license / consider collaborating).
- **Community CAD** (GrabCAD/Cults3D): usable as *reference* only — licensing is per-upload and usually personal-use; do **not** bundle without checking.
