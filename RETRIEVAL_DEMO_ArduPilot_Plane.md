# Look, don’t trust me — ArduPilot Plane retrieval demo

**Brick:** [`ArduPilot_Plane`](bricks/ArduPilot_Plane/)  
**Generated:** 2026-07-23  
**Method:** cosine top-3 over brick embeddings (nomic-embed-text), query embed via EmbeddingSystem

This page is a **published, verifiable demonstration** that the brick retrieves real content — not a marketing claim.

## What this is (and is not)

| This demo shows | This demo is not |
|----------------|------------------|
| **20 real questions** run against the **published brick embeddings** | An LLM “chat” transcript (no model invented these excerpts) |
| **Top-3 hits** with **cosine score**, **chunk id**, **heading**, and **excerpt** | A guarantee of perfect answers or flight-critical advice |
| Evidence you can **re-run yourself** after unzipping the brick | A substitute for reading the original ArduPilot docs |

Anyone with the portable ZIP + the same embed model can reproduce these rankings.

## Brick vs raw dump (why packaging matters)

| | Raw multi-page wiki / HTML dump | This knowledge brick |
|--|-------------------------------|----------------------|
| **Unit of retrieval** | Whole files or messy scrape blobs | **Chunks** with headings + stable ids |
| **What you get for a question** | Hope Ctrl+F or a giant context window hits | Ranked passages with **citations** (chunk + section) |
| **Quality honesty** | Silent garbage, nav chrome, duplicate pages | Residual craft notes on the card; bad regions flaggable |
| **Facet** | One infinite site | **Ops brick** separate from **params** brick — right book for the job |

The point of **KBMill** is not “another chatbot.” It is **manufacturing packages** where strangers can **see** retrieval quality.

## How to re-run (reproduce)

1. Download [`ArduPilot_Plane_portable.zip`](bricks/ArduPilot_Plane/ArduPilot_Plane_portable.zip) and unzip.
2. Load `embeddings.npy` + chunk list from `kb.json` / `chunks.jsonl`.
3. Embed each question with **nomic-embed-text** (same family as the brick).
4. Cosine-rank against the matrix; compare top hits to the table below.

Scores below are **cosine similarity** (higher is better). Excerpts are truncated source text from the hit chunk — not model paraphrases.

## Twenty questions

### 1. What is ArduPilot Plane used for?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.734 | `chunk-0066` | — |
| 2 | 0.724 | `chunk-0151` | GPS for yaw |
| 3 | 0.708 | `chunk-0333` | — |

**Top excerpt** (`chunk-0066`):

> Selecting the right board depends on the physical constraints of the vehicle, features desired, and the applications that you want to run. Factors to consider are: Sensor Redundancy: ArduPilot supports redundant IMUS, GPS, etc. Many controllers have multiple IMUs integrated on board for applications requiring this leve

### 2. How do I set up a first fixed wing flight?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.740 | `chunk-0265` | — |
| 2 | 0.728 | `chunk-0298` | — |
| 3 | 0.710 | `chunk-0029` | — |

**Top excerpt** (`chunk-0265`):

> Commercial Support Development Team UAS Training Centers Stores About News History License Trademark Acknowledgments Wiki Editing Guide Partners Program Plane Introduction to Plane Choosing an Autopilot Ground Control Stations First Time Setup First Flight and Tuning Center of Gravity Starting up and calibrating Plane 

### 3. What is FBWA mode?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.678 | `chunk-0260` | — |
| 2 | 0.677 | `chunk-0263` | — |
| 3 | 0.664 | `chunk-0269` | Flight Mode List |

**Top excerpt** (`chunk-0260`):

> So to gain altitude you should raise the throttle, and to lose altitude you should lower the throttle. If you want Plane to take care of holding altitude then you should look at the FlyByWireB mode. In FBWA mode throttle is manually controlled, but is constrained by the THR_MIN and THR_MAX settings. In FBWA mode the ru

### 4. How does automatic takeoff work?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.770 | `chunk-0313` | NAV_TAKEOFF Mission Command |
| 2 | 0.742 | `chunk-0314` | TAKEOFF Heading |
| 3 | 0.741 | `chunk-0298` | — |

**Top excerpt** (`chunk-0313`):

> ## NAV_TAKEOFF Mission Command ### ¶ The takeoff mission command specifies a takeoff pitch and a target altitude. The takeoff mission item is considered complete when the plane has reached the target altitude specified in the mission. The mission will then execute its normal end of mission behavior if it runs out of co

### 5. What is RTL and when does it trigger?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.706 | `chunk-0287` | — |
| 2 | 0.697 | `chunk-0310` | RTL_AUTOLAND |
| 3 | 0.676 | `chunk-0309` | — |

**Top excerpt** (`chunk-0287`):

> For Plane the home position is initially established at the time the plane acquires its GPS lock. It is then continuously updated as long as the autopilot is disarmed. This means if you execute an RTL in Plane, it will return to the location where it was when it was armed - assuming it had acquired GPS lock. Consider t

### 6. How do I calibrate the airspeed sensor?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.826 | `chunk-0317` | Calibrate the airspeed sensor |
| 2 | 0.814 | `chunk-0009` | Checking operation |
| 3 | 0.795 | `chunk-0010` | Miscalibration Safeguards |

**Top excerpt** (`chunk-0317`):

> ## Calibrate the airspeed sensor ### ¶ This only applies if you are using an airspeed sensor. A properly installed and calibrated airspeed sensor enables your model to fly with much better control over its airspeed, which in turn enables lower speeds to be used safely, extending endurance. For this reason if you are in

### 7. What causes a prearm check failure?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.764 | `chunk-0213` | Disabling the Pre-arm Safety Check |
| 2 | 0.744 | `chunk-0192` | Recognising which Pre-Arm Check has failed using the GCS |
| 3 | 0.674 | `chunk-0191` | — |

**Top excerpt** (`chunk-0213`):

> ## Disabling the Pre-arm Safety Check ### ¶ Warning Disabling pre-arm safety checks is not recommended. The cause of the pre-arm failure should be corrected before operation of the vehicle if at all possible. If you are confident that the pre-arm check failure is not a real problem, it is possible to skip a failing che

### 8. How do I tune TECS for climb performance?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.763 | `chunk-0323` | Flight Testing |
| 2 | 0.758 | `chunk-0328` | Complete Parameter List |
| 3 | 0.741 | `chunk-0330` | Algorithm Overview |

**Top excerpt** (`chunk-0323`):

> If the speed is too high, then TECS_SINK_MAX should be reduced. If the demanded pitch angle is constantly at the limit set by PTCH_LIM_MIN_DEG , then either the pitch angle limit PTCH_LIM_MIN_DEG needs to be reduced (become more negative) or the maximum sink rate TECS_SINK_MAX needs to be reduced. If the height respons

### 9. What is the difference between MANUAL and FBWA?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.679 | `chunk-0263` | — |
| 2 | 0.659 | `chunk-0260` | — |
| 3 | 0.614 | `chunk-0268` | Overview |

**Top excerpt** (`chunk-0263`):

> As with FBWA, the rudder is under a combination of manual control and auto control for turn coordination. You should also have a look at CRUISE mode, as it is generally better than FBWB, especially if there is significant wind. In CRUISE mode the aircraft will hold a ground track as opposed to just leveling the wings w

### 10. How do I configure a parachute for emergency?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.749 | `chunk-0111` | Message Details (Copter specific) |
| 2 | 0.745 | `chunk-0112` | Message Details (Copter specific) |
| 3 | 0.744 | `chunk-0096` | Unexpected ERRORS including Failsafes |

**Top excerpt** (`chunk-0111`):

> Normally vehicle is disarmed soon after 2 = Loss of control detected. Normally parachute is released soon after 13 = Flip mode 2 = Flip abandoned (not armed, pilot input or timeout) 15 = Parachute 2 = Not Deployed, vehicle too low 3 = Not Deployed, vehicle landed 16 = EKF Check 0 = Variance cleared (position estimate O

### 11. What parameters control stall prevention?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.743 | `chunk-0334` | — |
| 2 | 0.670 | `chunk-0324` | Fine Tuning |
| 3 | 0.667 | `chunk-0207` | Recognising which Pre-Arm Check has failed using the GCS |

**Top excerpt** (`chunk-0334`):

> When turning, the autopilot will monitor the demanded bank angle and airspeed and work out if there is a sufficient margin above the stall speed to turn at the demanded bank angle. If not the bank angle is limited to the safe value. The stall prevention system will always allow a bank of at least 25 degrees (to ensure 

### 12. How does geofence work on Plane?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.828 | `chunk-0272` | — |
| 2 | 0.778 | `chunk-0277` | Setting up geo-fencing |
| 3 | 0.777 | `chunk-0273` | Use for R/C training |

**Top excerpt** (`chunk-0272`):

> Appendix Archived Topics - Geo-Fencing in Plane Edit on GitHub ARCHIVED: See GeoFencing for info for firmware versions 4.1 and later # Geo-Fencing in Plane # ¶ The Geo-Fencing support in Plane firmware versions prior to 4.1, allows you to set a virtual ‘fence’ around the area you want to fly in, specified as an enclose

### 13. What is QSTABILIZE for VTOL?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.661 | `chunk-0025` | Failsafe Parameters and their Meanings |
| 2 | 0.651 | `chunk-0026` | Failsafe Parameters and their Meanings |
| 3 | 0.636 | `chunk-0161` | Commands supported by Plane |

**Top excerpt** (`chunk-0025`):

> No Action is ever taken for Short FailSafe in these modes: CIRCLE RTL TAKEOFF QRTL QLAND LOITER to Alt and QLAND FS_SHORT_ACTN = 3 disables taking action in ANY mode Note if in AutoLanding in AUTO or AUTOLAND, it will always continue to the landing In QuadPlanes, Short FailSafe will force QLAND by default, RTL if bit 2

### 14. How do I set up a mission with waypoints?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.752 | `chunk-0154` | Overview |
| 2 | 0.741 | `chunk-0159` | Commands supported by Plane |
| 3 | 0.736 | `chunk-0158` | Commands supported by Plane |

**Top excerpt** (`chunk-0154`):

> During a mission at most one “Navigation” command and one “Do” or “Condition” command can be running at one time. A typical mission might set a waypoint (NAV command), add a CONDITION command that doesn’t complete until a certain distance from the destination ( MAV_CMD_CONDITION_DISTANCE ), and then add a number of DO 

### 15. What is failsafe behavior if radio is lost?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.826 | `chunk-0015` | RC Failsafe |
| 2 | 0.762 | `chunk-0021` | Configuring for valid RC outputs while in RC Failsafe |
| 3 | 0.758 | `chunk-0018` | section below will be taken, if the |

**Top excerpt** (`chunk-0015`):

> ## RC Failsafe ### ¶ ### Radio Signal Failure ### ¶ If the received signal is lost or the control information corrupted for greater than RC_FS_TIMEOUT (default = 1 sec), or the receiver sets its “failsafe bit” in protocols which have this (like Sbus, FPort, etc.), or RC_OVERRIDES are lost if using a GCS only is being u

### 16. How do I log and review flight data?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.810 | `chunk-0102` | Downloading logs via MAVLink |
| 2 | 0.767 | `chunk-0103` | Downloading logs via MAVLink |
| 3 | 0.751 | `chunk-0099` | Logging Parameters |

**Top excerpt** (`chunk-0102`):

> ## Downloading logs via MAVLink ### ¶ Connect your vehicle to the ground station using the micro USB cable Open the Mission Planner’s Flight Data screen On the bottom left, select the “DataFlash Logs” tab and push the “Download DataFlash Log Via Mavlink” button Then, select the log you want to download. This will save 

### 17. What is the role of the flight controller compass?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.705 | `chunk-0314` | TAKEOFF Heading |
| 2 | 0.695 | `chunk-0077` | — |
| 3 | 0.692 | `chunk-0305` | Tuning waypoint transition behaviour |

**Top excerpt** (`chunk-0314`):

> ## TAKEOFF Heading ### ¶ Before takeoff it is important that the plane be pointing into the wind, and be aligned with the runway (if a wheeled takeoff is used). The plane will try to hold its heading during takeoff, with the initial heading set by the direction the plane is facing when the takeoff starts. It is highly 

### 18. How do I configure flaps or crow brakes?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.626 | `chunk-0096` | Unexpected ERRORS including Failsafes |
| 2 | 0.620 | `chunk-0220` | Flight modes configuration |
| 3 | 0.618 | `chunk-0026` | Failsafe Parameters and their Meanings |

**Top excerpt** (`chunk-0096`):

> Normally vehicle is disarmed soon after 2 = Loss of control detected. Normally parachute is released soon after 13 = Flip mode 2 = Flip abandoned (not armed, pilot input or timeout) 15 = Parachute 2 = Not Deployed, vehicle too low 3 = Not Deployed, vehicle landed 16 = EKF Check 0 = Variance cleared (position estimate O

### 19. What is loiter mode?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.635 | `chunk-0309` | — |
| 2 | 0.628 | `chunk-0159` | Commands supported by Plane |
| 3 | 0.617 | `chunk-0162` | Commands supported by Plane |

**Top excerpt** (`chunk-0309`):

> The loiter radius at home is determined by RTL_RADIUS , if it’s non-zero, otherwise WP_LOITER_RAD is used. Clock-wise or Counter-Clock-wise circling can be set by positive or negative values for the radius. Additionally, in firmware versions 4.0.6 and later, by setting RTL_CLIMB_MIN to a non-zero value, the plane will 

### 20. How does landing approach and flare work?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.822 | `chunk-0049` | Basic Autolanding |
| 2 | 0.804 | `chunk-0051` | Basic Autolanding |
| 3 | 0.784 | `chunk-0047` | Basic Autolanding |

**Top excerpt** (`chunk-0049`):

> Have a look at the TECS tuning page for more information. You should also be aware that many model aircraft can glide for long distances, and it may be that your requested glide slope and airspeed combination just isn’t achievable. ### Controlling the flare ### ¶ The final stage of the landing is called the “flare”. Du

## Honest notes

- Some headings are empty in metadata; the **excerpt and chunk id** still locate the passage.
- A few questions (e.g. VTOL-specific modes) may rank **related** ops/failsafe text rather than a perfect single page — that is useful signal for re-cuts, not something to hide.
- This is **retrieval evidence**, not an autopilot. Do not fly on library demos alone.

## Feedback

If a hit looks wrong, open an [Issue](../../issues) titled `ArduPilot_Plane: <your question>` and paste what you expected. That is how the library gets better.

---

*Demo produced from the same brick artifacts published in this repo. Method: local nomic embeddings + cosine top-3.*
