# US Founding Documents

**First federated shelf** for VectorForge public library dogfood.

Primary-source bricks (public domain texts), not modern commentary.  
**Not legal advice.** Historical instruments for study, retrieval, and multi-brick open-set.

## Series bricks

| Brick id | Content |
|----------|---------|
| `Declaration_of_Independence` | Declaration of Independence (1776) |
| `US_Constitution` | Constitution (1787) + Amendments I–XXVII |
| `Articles_of_Confederation` | Articles of Confederation (predecessor frame) |
| `Federalist_Papers` | The Federalist Nos. 1–85 (Hamilton, Madison, Jay) |
| `Anti_Federalist_Selections` | Curated Anti-Federalist essays (Brutus, Centinel, Cato, Federal Farmer, Agrippa) |

## Federation

Use Constructor `link_bricks` / `search_shelf` / open set ≤4.  
Suggested seeds: Constitution + Federalist for ratification themes; Articles + Constitution for “what changed.”

## Provenance

- Declaration: Project Gutenberg eBook #1  
- Constitution articles: Project Gutenberg eBook #5; amendments: US public domain  
- Articles of Confederation: Yale Avalon Project (public domain instrument)  
- Federalist: Project Gutenberg eBook #1404  
- Anti-Federalist selections: constitution.org AFP collection (public-domain 18th-c. essays; curated reader)  


## Build

```bash
cd VectorForge-Pro
export PYTHONPATH="$PWD:../VectorForge-Project:$PYTHONPATH"
export VECTORFORGE_EMBEDDING_DEVICE=cpu
python scripts/build_us_founding_documents_shelf.py --force
```
