# RAG retrieves. Something has to make the corpus worth retrieving.

# RAG retrieves. Something has to make the corpus worth retrieving.

      
Note · KBMill · category · the missing layer

      
Your local model is fine. The corpus is not. Teams often blame
        “RAG” or buy another retriever. Retrieval usually did its job:
        it searched what you gave it. The skipped job is
        knowledge-base manufacture — making a corpus
        worth retrieving from, and being honest about its limits. We
        are upstream of RAG, not opposed to it.

      
## Three jobs people conflate

      
The market conflates three different jobs into one word.
        Separating them is the teaching move:

      
### 1 · Extraction

      
“Get the words out of the file.” Tools people know: LlamaParse,
        Docling, house scripts. Yield: raw text / markdown. Sound for
        that job.
        Not a knowledge base by itself.

      
### 2 · Retrieval

      
RAG in the strict sense — “Find the relevant passage at query
        time and put it in context.” Tools people know: vector search,
        hybrid RAG, rerankers. Yield: a passage in the prompt. Sound
        after the corpus is fit to search.

      
### 3 · Manufacture — almost none

      
“Make a durable corpus worth retrieving from — mute what must
        not be quoted, list the holes, leave a package you can keep.”

      
Tools people know for this box:
        almost none.
        That empty cell is the argument. It is why
        answers stay junk after the box is up.

      
You already own the first two boxes. We are pointing at the
        third. Brand words for that box on our door:
        mill, brick, plant. Learn the
        category in plain language first; the brand is flavor on top.

      
A skeptic will say manufacture is “just good ingestion” that
        RAG guides already cover. Cleaning and chunking are real — and
        not enough. The wedge is the
        owned leave-behind: a portable ZIP with junk
        muted and listed on the LIBRARY_CARD and in chunk flags
        (that listed mute story is the residual board), not a hosted
        index you rent and hope. Prep folded into a pipeline is still
        a service. A brick is an artifact you keep.

      
## What “dump RAG” gets wrong

      
People stretch “RAG” to mean the whole pipeline: ingest,
        chunk, embed, search. Under that umbrella, dumping the
        SharePoint into an index is “doing RAG.” Strictly,
        retrieval only searches. The failure mode we refuse is
        dump-RAG — treat the raw share as if it were
        already a knowledge base. That path feeds
        ghost data and hallucination fuel
        into the prompt with confidence.

      
So we do not teach “not RAG.” We teach
        not dump-RAG: do not skip manufacture.
        Companion page:
        Keep your RAG. Point it at a brick.

      
## Why an artifact, not another index

      
Manufacture yields a knowledge brick you
        own — not another vector DB you subscribe to. You can
        hand the ZIP to any model you already run, read its documented
        limits, mute one locus without boiling a company index, and
        keep the packet when the vendor relationship ends. That is what
        folder-plus-dump-RAG does not give you.

      
## Argue with the package

      
Same mill:
        Public brick shelf
        ·
        HF retrieval eval.
        Open a ZIP. Re-run the cosine hits. If you disagree, argue with
        the package — not with our adjectives. We are not the only plant
        that could mill; we claim the method is sound and competitive.

      
## Simple at the door

      
Complexity stays in the automated plant. You
        drop files in the bin
        on the
        mill.
        No priesthood.
        Small / Medium / Hard
        are manufacture difficulty.
        Why bricks, not one melt: so you can
        compose and swap them
        — human-sized blast radius, not one unbounded soup.

---
Canonical HTML: https://kbmill.com/notes/not-rag
Public shelf: https://github.com/CMiller56/kbmill-brick-library
