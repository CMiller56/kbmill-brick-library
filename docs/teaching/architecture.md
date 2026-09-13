# Architecture

Architecture — plant boundaries, not a script — KBMill
  - Payments: Sep 14
      Invite coupons available · Workspace open
    
  
  
    
      
        
        KBMILL
        architecture
      
      
      Enter the plant
    
  

  
    
      
Diligence · Level 3

      
# Architecture

      
In plain English:
        KBMill receives a bounded document pile, processes it in isolation,
        removes unreliable material from the answer path, records what happened,
        and returns a package you can use without KBMill.

      
KBMill performs corpus manufacture:
        messy source documents → residual-honest knowledge bricks ready for retrieval.
        Unreliable parts are listed, not silently quoted as fact.

      
What runs behind the hopper
        states there is a plant.
        This page is the artifact that kills “just a script” —
        system boundaries, real station names with failure modes attached,
        a closed fail path, and a snippet from a real package.
        It is not source code and
        not the closed magazine.

      
        
## System boundary (public-safe)

        
[ Hopper / public door ]
        │
        ├─► Receive   — isolated per-job dir, idempotent, caps refuse before run
        ├─► Extract   — layout + table recovery + OCR trap handling
        ├─► Structure — brick plan → build → link (composition, not mega-melt)
        ├─► Package   — ZIP + residual board + SECURITY_REPORT + MILL_RECEIPT
        │
        └─► 72h download window · fail closed · no charge on fail
            = more copies of the same plant (commodity tower → heavier mirrors)
        
          Host owns the clock. Kitchen work can detach.
          Terminal envelope: done | failed | timeout.
          Ship cue: ready to ship | warnings | blocked.

      

      
        
## Three mouths (same plant)

        
          
            Factory — manufactures the package (brick).

          - Constructor — federates a shelf: link related bricks;
            open set stays small on purpose — composition, not one melt.

          - Connect — serves one brick into your stack.

        
        
Vocabulary for diligence readers.
          Implementation details of cutters and the closed magazine stay internal.

      

      
        
## Stations as systems (real names, real gates)

        
A script can do “extract PDF → chunk → embed.”
          A script does not carry years of trap handling and a closed fail class
          that still authors a residual board when the model times out.

        
          - Receive
            File checks and nested-archive unpack happen in an
            isolated per-job directory.
            Ceiling on this public door: 50 files / 500 MB —
            refuse before processing, no charge.
            Idempotent: same job identity → same work root; no double-build, no double charge.

          - Extract
            Dual-path layout work, table recovery, OCR trap handling.
            Image-heavy manuals are a known failure class —
            the plant is built to ship text-first packages plus a
            SECURITY_REPORT.md, not a silent dump of figure shells.

          - Structure
            Plan bricks → build → link related packages.
            Multi-brick programs are composition with an intentional small open set —
            not melting the estate into one unreliable mega-index.
            See packages, not monoliths.

          - Package
            Deterministic portable ZIP: primary markdown, bundle_manifest.json,
            chunks.jsonl (with per-chunk content_hash),
            embeddings + provenance when produced, craft_brief.md,
            residual / mute board (listed exclusions + muted chunk flags),
            SECURITY_REPORT.md, MILL_RECEIPT.md.

        
      

      
        
## Failure path is the moat

        
“On failure you are not charged” is table stakes.
          The plant difference is a closed fail path:
          fail once, cleanly; ship cue and fail class are enumerated;
          the leave-behind still tells you what was muted or blocked.
          Failures on this door clear within 24 hours.

        
One public trap class:
          figure-shell / image-only extracts.
          They look like “content” to a naive chunker and poison retrieval or training feed.
          The plant mutes them and lists the mute —
          see the snippet below from a real package
          (public shelf lineage).
          That class of trap is why “PyMuPDF + generic chunker” is not a plant.

      

      
        
## Compiler proof — real package snippets

        
Collapsed from a manufactured portable ZIP (US Army TM 11-666 lineage).
          Open full samples on the public shelf.

        
bundle_manifest.json (trimmed)

        
{
  "format": "vectorforge_portable_bundle_v1",
  "schema_version": "vectorforge_kb_v1",
  "kb_name": "TM_11_666_Antennas_Radio_Propagation",
  "kb_version": 1,
  "total_chunks": 530,
  "artifacts": {
    "primary_markdown": "TM_11_666_Antennas_Radio_Propagation.md",
    "kb_json": "kb.json",
    "chunks_jsonl": "chunks.jsonl",
    "embeddings": "embeddings.npy",
    "embedding_provenance": "embedding_provenance.json",
    "security_report": "SECURITY_REPORT.md",
    "craft_brief": "craft_brief.md"
  },
  "exported_at": "2026-08-19T20:12:14.007320"
}
        Muted chunk flag (from chunks.jsonl)

        
{
  "chunk_id": "chunk-0004",
  "muted": true,
  "mute_reason": "Figure-shell / image-only extract — excluded from RAG",
  "page_number": 4,
  "source_document": "TM11-666.pdf",
  "content_hash": "b93a05d0c66e8462",
  "token_count": 8
}
        
          When an architect sees manifest + per-chunk hash + listed mute,
          they are looking at a manufactured artifact — not a chat export.

      

      
        
## What this page deliberately does not publish

        
          - Closed cutter magazine / enzyme internals

          - Full operator SOP and agent loop budgets

          - Hardware mirror counts and GPU SKU plans (NDA / data room)

        
        
We show enough that a serious buyer believes manufacturing exists.
          We do not show enough that a serious engineer can stand up a twin from the website.
          Naming stations with failure modes attached raises the diligence bar for
          wrapper competitors — it does not ship them our edge-case code.

      

      
        
## Where to go next

        
Behind the hopper
          ·
          Data boundaries
          ·
          Sample packages
          ·
          Enter the plant
          ·
          /llms

---
Canonical HTML: https://kbmill.com/architecture
Public shelf: https://github.com/CMiller56/kbmill-brick-library
