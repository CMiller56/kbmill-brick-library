# Look, don't trust me — ArduPilot Plane Params retrieval demo

**Brick:** [`ArduPilot_Plane_Params`](bricks/ArduPilot_Plane_Params/)  
**Generated:** 2026-08-12  
**Method:** cosine top-3 over brick embeddings (nomic-embed-text v1.5); query embed with search_query: prefix via SentenceTransformer

This page is a **published, verifiable demonstration** that the brick retrieves real content — not a marketing claim.

## What this is (and is not)

| This demo shows | This demo is not |
|----------------|------------------|
| **15 real questions** run against the **published brick embeddings** | An LLM “chat” transcript (no model invented these excerpts) |
| **Top-3 hits** with **cosine score**, **chunk id**, **heading**, and **excerpt** | A guarantee of perfect param selection for flight |
| Evidence you can **re-run yourself** after unzipping the brick | A substitute for the ArduPilot parameter documentation |

Anyone with the portable ZIP + the same embed model can reproduce these rankings.

## Why params (not ops)

This brick is the **dense parameter table** facet — not flight-mode doctrine. Pair with [`ArduPilot_Plane`](bricks/ArduPilot_Plane/) for ops narrative and [`ArduPilot_MAVLink`](bricks/ArduPilot_MAVLink/) for protocol. See **[COMPOSITION_ArduPilot_Plane.md](COMPOSITION_ArduPilot_Plane.md)**.

| Brick | Role |
|-------|------|
| [ArduPilot_Plane](bricks/ArduPilot_Plane/) | How to fly / configure (ops wiki) |
| **[ArduPilot_Plane_Params](bricks/ArduPilot_Plane_Params/)** | What each parameter *is* (structured list → chunks) |
| [ArduPilot_MAVLink](bricks/ArduPilot_MAVLink/) | Wire protocol messages |

**Residual:** large soft residual by design (param table density). Soft residual craft notes live on the brick card — not hidden. **Not flight-critical advice.**

## How to re-run (reproduce)

1. Download [`ArduPilot_Plane_Params_portable.zip`](bricks/ArduPilot_Plane_Params/ArduPilot_Plane_Params_portable.zip) and unzip.
2. Load `embeddings.npy` + chunk list from `kb.json` / `chunks.jsonl`.
3. Embed each question with **nomic-embed-text** v1.5 using the brick’s **query** task prefix (`search_query: `).
4. Cosine-rank against the matrix; compare top hits to the tables below.

Scores below are **cosine similarity** (higher is better). Excerpts are truncated source text from the hit chunk — not model paraphrases.

## 15 questions

### 1. What does TECS_LAND_ARSPD control during landing?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.820 | `chunk-1507` | TECS_LAND_ARSPD: Airspeed during landing approach (m/s) |
| 2 | 0.795 | `chunk-1511` | TECS_LAND_TCONST: Land controller time constant (sec) |
| 3 | 0.767 | `chunk-1508` | TECS_LAND_IGAIN: Controller integrator during landing |

**Top excerpt** (`chunk-1507`):

> ## TECS_LAND_ARSPD: Airspeed during landing approach (m/s) Airspeed during landing approach (m/s) When performing an autonomous landing, this value is used as the goal airspeed during approach. Max airspeed allowed is Trim Airspeed or AIRSPEED_MAX as defined by LAND_OPTIONS bitmask. Note that this parameter is not use…

### 2. What is AIRSPEED_CRUISE used for on Plane?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.784 | `chunk-0027` | AIRSPEED_CRUISE: Target cruise airspeed |
| 2 | 0.754 | `chunk-0045` | ARSPD_TYPE: Airspeed type |
| 3 | 0.754 | `chunk-0077` | ARSPD6_TYPE: Airspeed type |

**Top excerpt** (`chunk-0027`):

> ## AIRSPEED_CRUISE: Target cruise airspeed Target cruise airspeed Target cruise airspeed in m/s in automatic throttle modes. Value is as an indicated (calibrated/apparent) airspeed. Units | meters per second | ### AIRSPEED_MAX: Maximum Airspeed Maximum Airspeed Maximum airspeed demanded in automatic throttle modes. Sh…

### 3. What does TECS_SINK_MIN set?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.751 | `chunk-1515` | TECS_SINK_MIN: Minimum Sink Rate (metres/sec) |
| 2 | 0.717 | `chunk-1505` | TECS_APPR_SMAX: Sink rate max for landing approach stage |
| 3 | 0.702 | `chunk-1509` | TECS_LAND_SINK: Sink rate for final landing stage |

**Top excerpt** (`chunk-1515`):

> ## TECS_SINK_MIN: Minimum Sink Rate (metres/sec) Minimum Sink Rate (metres/sec) Minimum sink rate when at THR_MIN and AIRSPEED_CRUISE. Increment | Range | 0.1 | 0.1 to 10.0 | ### TECS_SPDWEIGHT: Weighting applied to speed control Weighting applied to speed control Note: This parameter is for advanced users Mixing of p…

### 4. Which parameters configure battery failsafe voltage source?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.798 | `chunk-0192` | BATT8_FS_VOLTSRC: Failsafe voltage source |
| 2 | 0.798 | `chunk-0203` | BATT9_FS_VOLTSRC: Failsafe voltage source |
| 3 | 0.796 | `chunk-0170` | BATT6_FS_VOLTSRC: Failsafe voltage source |

**Top excerpt** (`chunk-0192`):

> ## BATT8_FS_VOLTSRC: Failsafe voltage source Failsafe voltage source Note: This parameter is for advanced users Voltage type used for detection of low voltage event Values | Value | Meaning | 0 | Raw Voltage | 1 | Sag Compensated Voltage | | ### BATT8_LOW_MAH: Low battery capacity Low battery capacity Battery capacity…

### 5. What does RTL_ALTITUDE control?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.789 | `chunk-1324` | RTL_ALTITUDE: RTL altitude |
| 2 | 0.738 | `chunk-1325` | RTL_CLIMB_MIN: RTL minimum climb |
| 3 | 0.694 | `chunk-1083` | Q_RTL_MODE: VTOL RTL mode |

**Top excerpt** (`chunk-1324`):

> ## RTL_ALTITUDE: RTL altitude RTL altitude Target altitude above home for RTL mode. Maintains current altitude if set to -1. Rally point altitudes are used if plane does not return to home. Units | meters | ### RTL_AUTOLAND: RTL auto land RTL auto land Automatically begin landing sequence after arriving at RTL locatio…

### 6. How is takeoff maximum throttle configured (TKOFF_THR_MAX)?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.909 | `chunk-1614` | TKOFF_THR_MAX: Maximum Throttle for takeoff |
| 2 | 0.842 | `chunk-1609` | TKOFF_LVL_ALT: Takeoff mode altitude level altitude |
| 3 | 0.823 | `chunk-1607` | TKOFF_ACCEL_CNT: Takeoff throttle acceleration count |

**Top excerpt** (`chunk-1614`):

> ## TKOFF_THR_MAX: Maximum Throttle for takeoff Maximum Throttle for takeoff Note: This parameter is for advanced users The maximum throttle setting during automatic takeoff. If this is zero then THR_MAX is used for takeoff as well. Increment | Range | Units | 1 | 0 to 100 | percent | ### TKOFF_THR_MAX_T: Takeoff throt…

### 7. What is LAND_TYPE for automatic landing?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.793 | `chunk-0685` | LAND_TYPE: Auto-landing type |
| 2 | 0.735 | `chunk-0079` | AUTOLAND_CLIMB: Minimum altitude above terrain before turning upon entry |
| 3 | 0.731 | `chunk-0675` | LAND_ABORT_DEG: Landing auto-abort slope threshold |

**Top excerpt** (`chunk-0685`):

> ## LAND_TYPE: Auto-landing type Auto-landing type Specifies the auto-landing type to use Values | Value | Meaning | 0 | Standard Glide Slope | 1 | Deepstall | | ### LAND_WIND_COMP: Headwind Compensation when Landing Headwind Compensation when Landing Note: This parameter is for advanced users This param controls how m…

### 8. What does Q_ENABLE do for QuadPlane?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.764 | `chunk-1055` | Q_ENABLE: Enable QuadPlane |
| 2 | 0.745 | `chunk-1037` | Q_ASSIST_DELAY: Quadplane assistance delay |
| 3 | 0.725 | `chunk-1036` | Q_ASSIST_ALT: Quadplane assistance altitude |

**Top excerpt** (`chunk-1055`):

> ## Q_ENABLE: Enable QuadPlane Enable QuadPlane Note: Reboot required after change This enables QuadPlane functionality, assuming multicopter motors start on output 5. If this is set to 2 then when starting AUTO mode it will initially be in VTOL AUTO mode. Values | Value | Meaning | 0 | Disable | 1 | Enable | 2 | Enabl…

### 9. How do I set compass declination (COMPASS_DEC)?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.831 | `chunk-0378` | COMPASS_DEC: Compass declination |
| 2 | 0.777 | `chunk-0376` | COMPASS_AUTODEC: Auto Declination |
| 3 | 0.723 | `chunk-0377` | COMPASS_CUS_PIT: Custom orientation pitch offset |

**Top excerpt** (`chunk-0378`):

> ## COMPASS_DEC: Compass declination Compass declination An angle to compensate between the true north and magnetic north Increment | Range | Units | 0.01 | -3.142 to 3.142 | radians | ### COMPASS_DEV_ID: Compass device id Compass device id Note: This parameter is for advanced users Compass device id. Automatically det…

### 10. What is COMPASS_AUTODEC?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.768 | `chunk-0376` | COMPASS_AUTODEC: Auto Declination |
| 2 | 0.690 | `chunk-0378` | COMPASS_DEC: Compass declination |
| 3 | 0.688 | `chunk-0382` | COMPASS_ENABLE: Enable Compass |

**Top excerpt** (`chunk-0376`):

> ## COMPASS_AUTODEC: Auto Declination Auto Declination Note: This parameter is for advanced users Enable or disable the automatic calculation of the declination based on gps location Values | Value | Meaning | 0 | Disabled | 1 | Enabled | | ### COMPASS_AUTO_ROT: Automatically check orientation Automatically check orien…

### 11. What does ARMING_SKIPCHK allow you to skip?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.792 | `chunk-0037` | ARMING_SKIPCHK: Arm Checks to Skip (bitmask) |
| 2 | 0.670 | `chunk-0036` | ARMING_REQUIRE: Require Arming Motors |
| 3 | 0.651 | `chunk-0033` | ARMING_ACCTHRESH: Accelerometer error threshold |

**Top excerpt** (`chunk-0037`):

> ## ARMING_SKIPCHK: Arm Checks to Skip (bitmask) Arm Checks to Skip (bitmask) Checks to skip prior to arming motor. This is a bitmask of checks before allowing arming that will be skipped. For most users it is recommended to leave this at the default of 0 (no checks skipped). In extreme circumstances, a value of -1 can…

### 12. What is FLIGHT_OPTIONS used for?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.731 | `chunk-0518` | FLIGHT_OPTIONS: Flight mode options |
| 2 | 0.682 | `chunk-1070` | Q_OPTIONS: quadplane options |
| 3 | 0.668 | `chunk-0517` | FLIGHT parameters (ArduPilot Plane) |

**Top excerpt** (`chunk-0518`):

> ## FLIGHT_OPTIONS: Flight mode options Flight mode options Note: This parameter is for advanced users Flight mode specific options Bitmask | Bit | Meaning | 0 | Rudder mixing in direct flight modes only (Manual/Stabilize/Acro) | 1 | Use centered throttle in Cruise or FBWB to indicate trim airspeed | 2 | Disable attitu…

### 13. What do THR_MAX and related throttle limits control?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.825 | `chunk-1602` | THR_MAX: Maximum Throttle |
| 2 | 0.748 | `chunk-1614` | TKOFF_THR_MAX: Maximum Throttle for takeoff |
| 3 | 0.723 | `chunk-1603` | THR_SLEWRATE: Throttle slew rate |

**Top excerpt** (`chunk-1602`):

> ## THR_MAX: Maximum Throttle Maximum Throttle Maximum throttle percentage used in all modes except manual, provided THR_PASS_STAB is not set. Increment | Range | Units | 1 | 0 to 100 | percent | ### THR_MIN: Minimum Throttle Minimum Throttle Minimum throttle percentage used in all modes except manual, provided THR_PAS…

### 14. What does AUTOTUNE_AXES select?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.795 | `chunk-0082` | AUTOTUNE_AXES: Autotune axis bitmask |
| 2 | 0.721 | `chunk-1038` | Q_AUTOTUNE_AGGR: Autotune aggressiveness |
| 3 | 0.700 | `chunk-1105` | QWIK_AXES: Quicktune axes |

**Top excerpt** (`chunk-0082`):

> ## AUTOTUNE_AXES: Autotune axis bitmask Autotune axis bitmask 1-byte bitmap of axes to autotune Bitmask | Bit | Meaning | 0 | Roll | 1 | Pitch | 2 | Yaw | | ### AUTOTUNE_LEVEL: Autotune level Autotune level Level of aggressiveness of pitch and roll PID gains. Lower values result in a 'softer' tune. Level 6 recommended…

### 15. What is ARSPD_TYPE (airspeed sensor type)?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.862 | `chunk-0045` | ARSPD_TYPE: Airspeed type |
| 2 | 0.841 | `chunk-0065` | ARSPD4_TYPE: Airspeed type |
| 3 | 0.841 | `chunk-0059` | ARSPD3_TYPE: Airspeed type |

**Top excerpt** (`chunk-0045`):

> ## ARSPD_TYPE: Airspeed type Airspeed type Type of airspeed sensor Values | Value | Meaning | 0 | None | 1 | I2C-MS4525D0 | 2 | Analog | 3 | I2C-MS5525 | 4 | I2C-MS5525 (0x76) | 5 | I2C-MS5525 (0x77) | 6 | I2C-SDP3X | 7 | I2C-DLVR-5in | 8 | DroneCAN | 9 | I2C-DLVR-10in | 10 | I2C-DLVR-20in | 11 | I2C-DLVR-30in | 12 |…

---

Machine twin: [`demos/ardupilot_plane_params_eval.json`](demos/ardupilot_plane_params_eval.json)  
Ops wiki twin: [RETRIEVAL_DEMO_ArduPilot_Plane.md](RETRIEVAL_DEMO_ArduPilot_Plane.md)  
Composition: [COMPOSITION_ArduPilot_Plane.md](COMPOSITION_ArduPilot_Plane.md)

*Generated against published brick embeddings (nomic-embed-text v1.5). Residual craft notes live on the brick card.*
