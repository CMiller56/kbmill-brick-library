# What actually runs behind the hopper?

# What actually runs behind the hopper?

      
Note · KBMill · plain English · legitimacy · manufacturing

      
Short answer:
        If you only read the philosophy Notes, you might think this is a thoughtful
        indie with good language about honesty and bricks.
        Look under the hopper and you should see something else:
        infrastructure-class manufacturing for AI-ready document packages —
        a process built to scale, and to be stood up with
        minimal pain next to the stack you already run.
        Regular visitors may not care. The people who own on-prem ROMs and write
        real checks will.

      
## Why this note exists

      
Teaching about wrong answers, mutes, and “not another RAG product” is necessary.
        It is not sufficient for the audience that matters commercially.
        Serious money does not fund a manifesto.
        It diligences whether there is a line —
        stations, ship gates, fail-closed paths, leave-behinds you can open —
        or just a wrapper around “extract text and hope.”

      
This page is the legitimacy clue:
        there is a plant under the hood —
        not a one-off script, not a hosted chat demo.
        The public site is the door to that plant, not the whole story.

      
## The plant in one paragraph

      
Behind the hopper is an offline-first manufacturing plant.
        Jobs do not share working space: each run gets its own directory,
        finishes or fails cleanly, and does not leave a hosted chatbot sitting on your documents.
        Idempotent: no double-build, no double charge —
        the same job identity reuses the same work root; steps no-op if the artifact is already there.
        On success you get a portable package plus plant-authored paperwork —
        residual / mute board, SECURITY_REPORT.md, and
        MILL_RECEIPT.md.
        On failure you are not charged.
        Closed fail path: a job ends in a terminal state
        (done, failed, or timeout) with a clear ship cue
        (ready to ship, warnings, or blocked).
        Failed jobs clear within 24 hours.
        Receive → extract → structure → package is not marketing wallpaper;
        it is how the line is built.
        This public mill at
        kbmill.com
        is the unattended door to that plant.

      
## Three manufacturing jobs (not one mega-index)

      
        - Make packages.
          Turn a bounded pile of documents into a brick you keep —
          readable text, chunks, embeddings when produced, listed exclusions.

        - Organize a shelf.
          Point related packages at each other when you need more than one domain.
          Composition — not melting everything into one giant unreliable index.

        - Serve one package at a time.
          Load a brick into your model stack and answer from it.
          We do not replace your RAG or host your corpus as a product.

      
      
Related:
        packages, not one giant pile,
        keep your RAG,
        why a mill.

      
## Infrastructure-class: scale without reinventing the line

      
Small / Medium / Hard are compute classes for plant work —
        clean text vs OCR, tables, and denser structure —
        not “tiers of chatbot minutes.”
        Caps (50 files / 500 MB, one job at a time on this public door) are process limits,
        not an apology.
        Data boundaries
        and the
        FAQ
        state purge windows and pay-on-success as operating rules.

      
Scale is not “one smarter API in someone else’s cloud.”
        Scale is more copies of the same plant —
        the design that runs on a roughly $1,500-class tower today
        is built to mirror when you need throughput, including heavier GPU boxes.
        A written SOP can drive the line; capable models can operate it;
        the manufacturing process stays the manufacturing process.
        That is what “infrastructure class” means here:
        repeatable manufacture, not a hero demo that cannot be copied.

      
## Minimal pain next to your stack

      
Implementation pain is where most “AI document” products lose serious buyers.
        The plant is shaped to avoid that:

      
        - You keep the ZIP.
          No lock-in to our hosted corpus. Point your model and RAG at the package.

        - Keep your retrieval.
          We manufacture upstream of RAG — we do not force you to rip out what already works.
          See keep your RAG.

        - Pay only if we deliver.
          Pilot a bounded pile through the
          public door
          before you commit to a program.

        - Open samples first.
          Inspect a
          real package
          — residual board, receipt, structure — before you upload anything sensitive.

      
      
If document preparation belongs on your on-prem cost slide —
        fourth leg —
        this is the diligence path:
        sample ZIP → one paid-on-success job → decide whether the plant belongs in the ROM.

      
## What this is not

      
        - Not another RAG product that retrieves over a dump.

        - Not a hosted knowledge base that locks your corpus behind our login.

        - Not “we ran an extractor and called it done.”

        - Not philosophy alone — though the honesty Notes still matter.

      
      
Residual honesty, bricks, and stalls explain why manufacture exists.
        The plant is what exists:
        stations, gates, a closed fail path, and a package you can hold.
        That is the legitimacy signal.

      
## What to do

      
If you are evaluating for real spend: inspect a
        sample package,
        read
        how files are handled,
        read /architecture,
        then
        run one bounded job
        through the door.
        Category context:
        why a mill instead of another RAG layer,
        why prep belongs on the cost slide,
        when the web runs out of training data.

---
Canonical HTML: https://kbmill.com/notes/what-runs-behind-the-hopper
Public shelf: https://github.com/CMiller56/kbmill-brick-library
