# Look, don't trust me — NASA_Skylab_History_Living_Working_Space retrieval demo

**Brick:** [`NASA_Skylab_History_Living_Working_Space`](bricks/NASA_Skylab_History_Living_Working_Space/)  
**Generated:** 2026-10-02  
**Method:** cosine top-3 over brick embeddings (nomic-embed-text v1.5); query embed with `search_query:` prefix via EmbeddingSystem

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

**Package this ranking used:** 1260 chunks, 120 muted, 1140 eligible. Muted chunks are not ranked.

## How to re-run (reproduce)

1. Download the portable ZIP under [`NASA_Skylab_History_Living_Working_Space`](bricks/NASA_Skylab_History_Living_Working_Space/) and unzip.
2. Load `embeddings.npy` + chunk list from `kb.json` / `chunks.jsonl`.
3. Embed each question with **nomic-embed-text** v1.5 using the brick’s **query** task prefix (`search_query: `).
4. Cosine-rank against the eligible rows (skip `muted` / `exclude_from_rag`); compare top hits to the tables below.

Scores below are **cosine similarity** (higher is better). Excerpts are truncated source text from the hit chunk — not model paraphrases.

## 15 questions

### 1. What was Skylab and why was it built?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.732 | `chunk-0972` | A COMET FOR CHRISTMAS |
| 2 | 0.718 | `chunk-0099` | Part I |
| 3 | 0.718 | `chunk-0996` | A COMET FOR CHRISTMAS |

**Top excerpt** (`chunk-0972`):

> ## RESULTS ![Figure from page 368](images/p368_img00.png) RESULTS SKYLAB SCIENCE: AN ASSESSMENT For all the vagaries of its early development, Skylab held to its primary purpose of putting man into orbit to perform scientific work, and in that aim it was indisputably successful. Some scientists even felt that a second…

### 2. What was the Apollo Applications Program?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.833 | `chunk-0145` | part of long-duration workshop flights. As the months passed and some |
| 2 | 0.821 | `chunk-0157` | part of long-duration workshop flights. As the months passed and some |
| 3 | 0.812 | `chunk-0175` | part of long-duration workshop flights. As the months passed and some |

**Top excerpt** (`chunk-0145`):

> ## APOLLO APPLICATIONS ![Figure from page 56](images/p056_img00.png) APOLLO APPLICATIONS missions were scheduled to fly excess hardware from the lunar landing program; the remaining 25 represented new Saturn-Apollo purchases. The missions fell into four categories (earth orbital, synchronous, lunar orbital, and lunar…

### 3. How did astronauts live and work in space on Skylab?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.848 | `chunk-0490` | part of the documents system that Skylab inherited from Apollo. Paper |
| 2 | 0.844 | `chunk-0398` | part of the documents system that Skylab inherited from Apollo. Paper |
| 3 | 0.819 | `chunk-0397` | part of the documents system that Skylab inherited from Apollo. Paper |

**Top excerpt** (`chunk-0490`):

> ## LIVING AND WORKING IN SPACE ![Figure from page 178](images/p178_img00.png) LIVING AND WORKING IN SPACE Skylab’s size and shape, was configured to duplicate the orbital workshop as nearly as possible. The lower level was laid out with the wardroom and food preparation area, the medical experiments, and the waste man…

### 4. What happened to Skylab's solar array and heat shield after launch?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.816 | `chunk-0716` | Part I11 |
| 2 | 0.813 | `chunk-0718` | Part I11 |
| 3 | 0.793 | `chunk-0773` | part of the area facing the sun would bring temperatures within satis- |

**Top excerpt** (`chunk-0716`):

> SAVING SKYLAB mands from both Goldstone, California, and Madrid seemed to confirm the worst fears. The solar panels were the main topic of discussion at the postlaunch briefing at Kennedy.2 By late afternoon, it appeared that Skylab had at least two major problems. If the workshop solar panels were indeed gone, Skylab…

### 5. What was the Apollo Telescope Mount?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.761 | `chunk-0506` | part of the documents system that Skylab inherited from Apollo. Paper |
| 2 | 0.760 | `chunk-0132` | Part I |
| 3 | 0.758 | `chunk-0499` | part of the documents system that Skylab inherited from Apollo. Paper |

**Top excerpt** (`chunk-0506`):

> ## STUDYING THE SUN ![Figure from page 184](images/p184_img00.png) STUDYING THE SUN APOLLO TELESCOPE MOUNT The solar telescopes were massive—the entire collection weighed over a ton and some of them were three meters long—but they were still precision optical devices, requiring elaborate support systems. Primary among…

### 6. What medical and life sciences experiments ran on Skylab?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.764 | `chunk-0934` | A COMET FOR CHRISTMAS |
| 2 | 0.760 | `chunk-0486` | part of the documents system that Skylab inherited from Apollo. Paper |
| 3 | 0.750 | `chunk-0932` | A COMET FOR CHRISTMAS |

**Top excerpt** (`chunk-0934`):

> ## Results ![Figure from page 354](images/p354_img00.png) Results As Schneider had said, the missions were only the first phase of Skylab’s science program. Principal investigators immediately began processing the staggering amount of material the crews had collected (table 2). From the five solar telescopes, astronom…

### 7. How many crewed Skylab missions were there?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.774 | `chunk-0709` | Part I11 |
| 2 | 0.756 | `chunk-1020` | A COMET FOR CHRISTMAS |
| 3 | 0.755 | `chunk-1015` | A COMET FOR CHRISTMAS |

**Top excerpt** (`chunk-0709`):

> ## Part I11 Part I11 The Missions and Results, 1973-1979 Skylab's debut as the sustaining mission for American manned spaceflight was a near-disaster. One minute into the flight the meteoroid shield-which also served as the primary means of thermal controlripped away, leaving the workshop exposed to searing solar heat…

### 8. What was the orbital workshop concept?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.806 | `chunk-0112` | Part I |
| 2 | 0.804 | `chunk-0110` | Part I |
| 3 | 0.754 | `chunk-0133` | Part I |

**Top excerpt** (`chunk-0112`):

> ## 7 FROM CONCEPT THROUGH DECISION ![Figure from page 43](images/p043_img00.png) 7 FROM CONCEPT THROUGH DECISION : plan that had been presented to Management Council. Three | configurations of an orbital workshop were to be studied. (Orbital workshop was the official designation for the spent stage. As the program pro…

### 9. How was Skylab launched and what vehicle was used?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.826 | `chunk-0693` | part of the documents system that Skylab inherited from Apollo. Paper |
| 2 | 0.819 | `chunk-0657` | part of the documents system that Skylab inherited from Apollo. Paper |
| 3 | 0.817 | `chunk-0669` | part of the documents system that Skylab inherited from Apollo. Paper |

**Top excerpt** (`chunk-0693`):

> ## LAUNCHING SKYLAB ![Figure from page 258](images/p258_img00.png) LAUNCHING SKYLAB actual checkout of the telescope mount went very smoothly; afterward Debus recognized the test team’s work with a letter of commendation.” PROBLEMS OF NEW HARDWARE When flight hardware arrived in mid-1972, the launch team moved to cent…

### 10. What food sleep and exercise routines did crews use?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.744 | `chunk-0851` | part of the area facing the sun would bring temperatures within satis- |
| 2 | 0.730 | `chunk-0853` | part of the area facing the sun would bring temperatures within satis- |
| 3 | 0.729 | `chunk-0850` | part of the area facing the sun would bring temperatures within satis- |

**Top excerpt** (`chunk-0851`):

> SECOND MISSION brought more experiments. When the astronauts ran out of work, as Bean's crew sometimes did, flight controllers employed a "shopping list" of activities-experiments or repairs that crewmen could undertake with short notice.37 Dinner was at 6:00 p.m., after which the crew turned to household chores and a…

### 11. What was planned for Skylab rescue or reboost?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.738 | `chunk-0997` | A COMET FOR CHRISTMAS |
| 2 | 0.715 | `chunk-0995` | A COMET FOR CHRISTMAS |
| 3 | 0.698 | `chunk-1004` | A COMET FOR CHRISTMAS |

**Top excerpt** (`chunk-0997`):

> ## MISSIONS AND RESULTS ![Figure from page 379](images/p379_img00.png) MISSIONS AND RESULTS lab’s systems. If the derelict were to be reboosted for later use or brought out of orbit at a site of NASA’s choosing, it was necessary to determine how much control could be exercised from the ground. In the most favorable ci…

### 12. When and why did Skylab reenter the atmosphere?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.796 | `chunk-1014` | A COMET FOR CHRISTMAS |
| 2 | 0.787 | `chunk-1017` | A COMET FOR CHRISTMAS |
| 3 | 0.785 | `chunk-0714` | Part I11 |

**Top excerpt** (`chunk-1014`):

> EDT, most probably on its 34 981st orbit. It was then at an altitude of 190 kilometers. The following day it dropped 17 km and the reentry time was bracketed between 7:02 a.m. and 5:02 p.m. EDT on the 1 ~ t h . ~ ~ In Houston, Charles Harlan and his team stood by to make their last decision. For some hours before reen…

### 13. What Earth resources or remote sensing work did Skylab do?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.812 | `chunk-0949` | A COMET FOR CHRISTMAS |
| 2 | 0.806 | `chunk-0953` | A COMET FOR CHRISTMAS |
| 3 | 0.805 | `chunk-0951` | A COMET FOR CHRISTMAS |

**Top excerpt** (`chunk-0949`):

> A huge solar eruption recorded by the extreme-ultraviolet spectroheliograph S082A; helium has been ejected more than 800 000 km. For comparison, the earth is not much larger than the black dot near the rim of the sun and beneath the arch of helium. The instrument was constructed by the U.S. Naval Research Laboratory a…

### 14. How did Skylab differ from earlier Apollo lunar missions?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.812 | `chunk-0025` | Part I of the present volume details the background against which |
| 2 | 0.811 | `chunk-0023` | Page intentionally left blank |
| 3 | 0.796 | `chunk-0352` | part I1 of this history. Chapter 6 focuses on the program leaders, the |

**Top excerpt** (`chunk-0025`):

> ## Preface ![Figure from page 13](images/p013_img00.png) Preface The program that became Skylab was conceived in 1963, when the Office of Manned Space Flight began to study options for manned programs to follow Apollo. Although America’s lunar landing program was a long way from successful completion, it was not too s…

### 15. What lessons from Skylab informed later space stations?

| Rank | Score | Chunk | Heading |
|------|------:|-------|---------|
| 1 | 0.785 | `chunk-0710` | Part I11 |
| 2 | 0.783 | `chunk-0972` | A COMET FOR CHRISTMAS |
| 3 | 0.782 | `chunk-0709` | Part I11 |

**Top excerpt** (`chunk-0710`):

> ## Part II ![Figure from page 266](images/p266_img00.png) Part II The Missions and Results, Skylab’s debut as the sustaining mission for American manned spaceflight was a near-disaster. One minute into the flight the meteoroid shield—which also served as the primary means of thermal control— ripped away, leaving the w…

---

*Generated 2026-10-02 from the published ZIP embeddings (nomic-embed-text v1.5, `search_query:` prefix). Residual craft notes live on the brick card.*
