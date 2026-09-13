# Stop wasting AI power cleaning the same documents

# Stop wasting AI power cleaning the same documents

      
Note · KBMill · plain English · tokens, context, and electricity

      
Short answer:
        Running AI costs electricity and money billed as
        tokens — the units providers charge for every
        piece of text the model reads or writes.
        If every question forces the model to re-read messy PDFs, scans, and
        broken tables, you burn expensive tokens again and again, and you
        fill the model’s limited context window with
        cleanup work instead of the answer.
        Preparing the documents once into a clean package you keep
        means later questions spend fewer tokens, leave more room in that
        window for useful material — and get better answers.

      
## The simple problem

      
Companies are buying more AI chips. Power plants and power lines
        cannot keep up forever. Leaders are saying out loud: we may not be
        able to “just add more electricity” as fast as we want.

      
So the question changes. It is not only “how smart is the model?”
        It is also “how much useful work do we get from each dollar, each
        token, and each watt we already spend?”

      
## Tokens and the context window (in everyday terms)

      
Two ideas show up on almost every AI bill and product page.
        Worth knowing them by name:

      
        - Tokens are how providers meter usage.
          Roughly: chunks of words. You pay for what goes in
          (your question plus the documents or notes you attach) and what
          comes out (the answer). Bigger models usually mean
          more expensive tokens.

        - The context window is how much text the model
          can hold at once for a single turn — question, attached material,
          and answer together. It is finite. Space spent re-cleaning the
          same PDF is space you cannot spend on the facts that matter.
          And the problem is not only running out of room: stuffing a huge
          messy pile into a big window often means the model
          misses the fact you care about in the middle of
          the noise.

      
      
When people say “we’re burning tokens” or “we ran out of context,”
        this is what they mean.

      
## What people usually do (and why it wastes tokens)

      
A common habit is to throw the messy folder at a powerful model and
        hope:

      
        - “Read this PDF and answer my question.”

        - “Clean up this scan.”

        - “Find the right table cell.”

      
      
That can work for a demo. In daily use it is expensive. The model
        keeps rediscovering the same empty pages, broken tables, and
        unreadable scans. Every retry, every longer attachment, every
        “try again” spends more tokens — and more electricity.
        The context window fills with repeating document-processing work
        instead of the clean material you actually need to answer.
        Using a top-dollar model to figure out where a table column ends
        is the wrong tool for the job: expensive power pointed at
        janitorial work.

      
Related notes:
        where wrong answers come from,
        tables that invent numbers,
        scanned manuals.

      
## The better pattern: prepare once, ask often

      
KBMill is built for a different pattern:

      
        - Once: turn your documents into a portable ZIP —
          readable text, searchable pieces, and a clear list of material
          that should not be trusted or quoted.

        - Often: point your own AI at that package.
          The model answers questions instead of re-cleaning the pile.

      
      
You keep the ZIP. We do not host a chatbot on your documents.
        You pay only if we deliver a usable package.

      
That is not only a quality story. It is a
        token, context, and power story: do the hard
        document work once in a tool built for it, instead of paying a
        giant model — in expensive tokens — to do janitorial work on every
        question, while that same work crowds the context window.

      
## Two bills to compare

      
        - Upfront bill (once per package).
          Preparing a bounded set of files — Small, Medium, or Hard.
          Real cost, but finite. Under our door you pay only if we produce.

        - Ongoing bill (every question).
          Token spend each time the AI reads attached material and answers.
          If that material is full of noise and half-done cleanup, you pay
          for noise forever — and you waste context-window space on work
          that should already be finished.

      
      
A list of “do not quote this” material — the mute list — is not
        only honesty. It is a permanent token filter:
        corrupt or empty pages are kept off the answer path, so those
        tokens are never bought again, and that window stays available
        for useful content.

      
Some providers discount re-reading the same long text (caching);
        cheaper noise is still noise.

      
## What we are not claiming

      
We are not publishing a fake “% tokens saved” or “% electricity
        saved” scorecard. Your savings depend on how bad the pile was and
        how often you ask. The claim is simpler: when electricity, tokens,
        and context are scarce, re-cleaning messy documents on every
        question is the wasteful path; preparing them once is the
        efficient path.

      
Prove it on your own work: same questions, same model, messy folder
        vs prepared package. Compare retries, token usage, and how much
        text you have to stuff into each turn. You can also re-run our
        public retrieval checks.

      
## What to do

      
Open the
        workspace
        and try a bounded set of documents.
        Or inspect
        sample packages
        first.
        Deeper category notes:
        this is not another chatbot/RAG product,
        why document prep belongs on the cost slide.

---
Canonical HTML: https://kbmill.com/notes/efficiency-when-watts-bind
Public shelf: https://github.com/CMiller56/kbmill-brick-library
