# Look, don't trust me — NASA_Skylab_History_Living_Working_Space retrieval demo

**Brick:** [`NASA_Skylab_History_Living_Working_Space`](bricks/NASA_Skylab_History_Living_Working_Space/)  
**Generated:** 2026-07-31  
**Method:** cosine top-k over brick embeddings (nomic-embed-text), query embed via EmbeddingSystem

This page is a **published, verifiable demonstration** that the brick retrieves real content — not a marketing claim.

## What this is (and is not)

| This demo shows | This demo is not |
|----------------|------------------|
| **15 real questions** run against the **published brick embeddings** | An LLM “chat” transcript (no model invented these excerpts) |
| **Top-3 hits** with **cosine score**, **chunk id**, **heading**, and **excerpt** | A guarantee of perfect answers or formal citation |
| Evidence you can **re-run yourself** after unzipping the brick | A substitute for reading the original NASA history |

Anyone with the portable ZIP + the same embed model can reproduce these rankings.

Machine-readable twin: [`demos/nasa_skylab_history_eval.json`](demos/nasa_skylab_history_eval.json).

Paper-capture OCR history after residual craft (post-promote soft-hyphen, figure magazine). Retrieval is text-first; figure plates may be slimmed from the portable ZIP for gallery size.

## How to re-run (reproduce)

1. Download the portable ZIP under [`NASA_Skylab_History_Living_Working_Space`](bricks/NASA_Skylab_History_Living_Working_Space/) and unzip.
2. Load `embeddings.npy` + chunk list from `kb.json` / `chunks.jsonl`.
3. Embed each question with **nomic-embed-text** (same family as the brick).
4. Cosine-rank against the matrix; compare top hits to the tables below.

Scores below are **cosine similarity** (higher is better). Excerpts are truncated source text from the hit chunk — not model paraphrases.

## 15 questions

### 1. What was Skylab and why was it built?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.732 | `chunk-0931` | Figures |
| 2 | 0.723 | `chunk-0929` | RESULTS |
| 3 | 0.722 | `chunk-0955` | The engineers in Bermuda made their first contact with Skylab the |

**Top excerpt** (`chunk-0931`):

> ## RESULTS ![Figure from page 368](images/p368_img00.png) RESULTS SKYLAB SCIENCE: AN ASSESSMENT For all the vagaries of its early development, Skylab held to its primary purpose of putting man into orbit to perform scientific work, and in that aim it was indisputably successful. Some scientists even felt that a second…

### 2. What was the Apollo Applications Program?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.833 | `chunk-0136` | Figures |
| 2 | 0.821 | `chunk-0147` | Figures |
| 3 | 0.812 | `chunk-0165` | Figures |

**Top excerpt** (`chunk-0136`):

> ## APOLLO APPLICATIONS ![Figure from page 56](images/p056_img00.png) APOLLO APPLICATIONS missions were scheduled to fly excess hardware from the lunar landing program; the remaining 25 represented new Saturn-Apollo purchases. The missions fell into four categories (earth orbital, synchronous, lunar orbital, and lunar…

### 3. How did astronauts live and work in space on Skylab?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.848 | `chunk-0470` | Figures |
| 2 | 0.844 | `chunk-0383` | Figures |
| 3 | 0.831 | `chunk-0468` | LIVING AND WORKING IN SPACE |

**Top excerpt** (`chunk-0470`):

> ## LIVING AND WORKING IN SPACE ![Figure from page 178](images/p178_img00.png) LIVING AND WORKING IN SPACE Skylab’s size and shape, was configured to duplicate the orbital workshop as nearly as possible. The lower level was laid out with the wardroom and food preparation area, the medical experiments, and the waste man…

### 4. What happened to Skylab's solar array and heat shield after launch?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.813 | `chunk-0686` | Figures |
| 2 | 0.812 | `chunk-0684` | SAVING SKYLAB |
| 3 | 0.801 | `chunk-0738` | The repaired Skylab. The sunshade, |

**Top excerpt** (`chunk-0686`):

> ## ° SAVING SKYLAB ![Figure from page 270](images/p270_img00.png) ° SAVING SKYLAB mands from both Goldstone, California, and Madrid seemed to confirm the worst fears. The solar panels were the main topic of discussion at the postlaunch briefing at Kennedy.’ By late afternoon, it appeared that Skylab had at least two m…

### 5. What was the Apollo Telescope Mount?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.771 | `chunk-0255` | An early version of the Apollo telescope mount. The solar array on the |
| 2 | 0.767 | `chunk-0478` | The Apollo telescope m |
| 3 | 0.761 | `chunk-0485` | Figures |

**Top excerpt** (`chunk-0255`):

> ## An early version of the Apollo telescope mount. The solar array on the An early version of the Apollo telescope mount. The solar array on the right is partially deployed. contractor modify spacecraft for AAP so that North American could concentrate on Apollo deficiencies. He also gave the Apollo program director so…

### 6. What medical and life sciences experiments ran on Skylab?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.764 | `chunk-0894` | Figures |
| 2 | 0.755 | `chunk-0893` | Results |
| 3 | 0.749 | `chunk-0929` | RESULTS |

**Top excerpt** (`chunk-0894`):

> ## Results ![Figure from page 354](images/p354_img00.png) Results As Schneider had said, the missions were only the first phase of Skylab’s science program. Principal investigators immediately began processing the staggering amount of material the crews had collected (table 2). From the five solar telescopes, astronom…

### 7. How many crewed Skylab missions were there?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.774 | `chunk-0678` | Part I11 |
| 2 | 0.762 | `chunk-0972` | MISSIONS AND RESULTS |
| 3 | 0.755 | `chunk-0974` | Figures |

**Top excerpt** (`chunk-0678`):

> ## Part I11 Part I11 The Missions and Results, 1973-1979 Skylab's debut as the sustaining mission for American manned spaceflight was a near-disaster. One minute into the flight the meteoroid shield-which also served as the primary means of thermal controlripped away, leaving the workshop exposed to searing solar heat…

### 8. What was the orbital workshop concept?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.806 | `chunk-0104` | Figures |
| 2 | 0.806 | `chunk-0102` | FROM CONCEPT THROUGH DECISION |
| 3 | 0.754 | `chunk-0124` | Figures |

**Top excerpt** (`chunk-0104`):

> ## 7 FROM CONCEPT THROUGH DECISION ![Figure from page 43](images/p043_img00.png) 7 FROM CONCEPT THROUGH DECISION : plan that had been presented to Management Council. Three | configurations of an orbital workshop were to be studied. (Orbital workshop was the official designation for the spent stage. As the program pro…

### 9. How was Skylab launched and what vehicle was used?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.828 | `chunk-0661` | LAUNCHING SKYLAB |
| 2 | 0.826 | `chunk-0663` | Figures |
| 3 | 0.819 | `chunk-0628` | Figures |

**Top excerpt** (`chunk-0661`):

> ## LAUNCHING SKYLAB LAUNCHING SKYLAB actual checkout of the telescope mount went very smoothly; afterward Debus recognized the test team's work with a letter of c~mmendation.~' When flight hardware arrived in mid-1972, the launch team moved to center stage, where it would remain for the next nine months. The first spa…

### 10. What food sleep and exercise routines did crews use?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.730 | `chunk-0810` | MISSIONS AND RESULTS |
| 2 | 0.730 | `chunk-0815` | Figures |
| 3 | 0.729 | `chunk-0812` | Figures |

**Top excerpt** (`chunk-0810`):

> ## MISSIONS AND RESULTS MISSIONS AND RESULTS daily scrubbing with washcloths. The bathroom's size precluded more than one occupant at a time, a limitation which posed some scheduling difficulties in the first hour. Paul Weitz eased the problem by shaving at night; Carr and Pogue of the third crew eventually quit shavi…

### 11. What was planned for Skylab rescue or reboost?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.738 | `chunk-0956` | Figures |
| 2 | 0.723 | `chunk-0954` | MISSIONS AND RESULTS |
| 3 | 0.697 | `chunk-0949` | ~ |

**Top excerpt** (`chunk-0956`):

> ## MISSIONS AND RESULTS ![Figure from page 379](images/p379_img00.png) MISSIONS AND RESULTS lab’s systems. If the derelict were to be reboosted for later use or brought out of orbit at a site of NASA’s choosing, it was necessary to determine how much control could be exercised from the ground. In the most favorable ci…

### 12. When and why did Skylab reenter the atmosphere?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.795 | `chunk-0973` | EDT, |
| 2 | 0.787 | `chunk-0976` | A |
| 3 | 0.777 | `chunk-0974` | Figures |

**Top excerpt** (`chunk-0973`):

> ## EDT, EDT, most probably on its 34 981st orbit. It was then at an altitude of 190 kilometers. The following day it dropped 17 km and the reentry time was bracketed between 7:02 a.m. and 5:02 p.m. EDT on the 1 ~ t h . ~ ~ In Houston, Charles Harlan and his team stood by to make their last decision. For some hours bef…

### 13. What Earth resources or remote sensing work did Skylab do?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.810 | `chunk-0910` | MISSIONS AND RESULTS |
| 2 | 0.806 | `chunk-0912` | Figures |
| 3 | 0.801 | `chunk-0908` | A huge solar eruption recorded by |

**Top excerpt** (`chunk-0910`):

> ## MISSIONS AND RESULTS MISSIONS AND RESULTS gions of the spectrum. Investigators at Purdue University used these and the multispectral photographs from S 190A in a computerized program of land-use determination; their project aimed at automatic classification of land into nine categories ranging from residential and…

### 14. How did Skylab differ from earlier Apollo lunar missions?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.812 | `chunk-0017` | Page intentionally left blank |
| 2 | 0.812 | `chunk-0019` | Figures |
| 3 | 0.793 | `chunk-0338` | Figures |

**Top excerpt** (`chunk-0017`):

> ## Page intentionally left blank Preface The program that became Skylab was conceived in 1963, when the Office of Manned Space Flight began to study options for manned programs to follow Apollo. Although America's lunar landing program was a long way from successful completion, it was not too soon to consider what sho…

### 15. What lessons from Skylab informed later space stations?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.789 | `chunk-0930` | Their ability to react to unexpected occurrences on the sun was a prime |
| 2 | 0.785 | `chunk-0679` | Figures |
| 3 | 0.783 | `chunk-0931` | Figures |

**Top excerpt** (`chunk-0930`):

> ## Their ability to react to unexpected occurrences on the sun was a prime Their ability to react to unexpected occurrences on the sun was a prime factor in the success of the A T M experiments. The same could be said for the earth-observations program; a man in orbit, trained to look for objects of interest and alert…

---

*Generated by VectorForge Pro manufacture (`vectorforge-maintain retrieval-demo`). Residual craft notes live on the brick card.*
