Draft all social posts for a completed module or Substack post. Produces ready-to-paste copy for X, LinkedIn, Reddit, and Substack Notes.

Module or post: $ARGUMENTS
(Format: "M07" for a module post, or "post-4" for a newsletter post)

Instructions:
1. Parse the input. If a module ID (M##):
   - Read modules/$ARGUMENTS-*/blog-post-seed.md (or the expanded draft if it exists)
   - Read modules/$ARGUMENTS-*/audit.md for real learning experience details
   - Read modules/$ARGUMENTS-*/theory.md for the core concepts
2. If a post reference (post-N):
   - Read the corresponding hub file: content/newsletter/posts/0N-*/substack.md

3. Draft the following, clearly separated:

**X / Twitter Thread (5–7 tweets):**
- Tweet 1: Hook — the most surprising or counterintuitive thing from this module
- Tweet 2: The concept — teach one idea in plain language
- Tweet 3: The project — what you built to demonstrate competency
- Tweet 4: The H&C connection — how this changes the platform you're building
- Tweet 5: CTA — link to Substack post + repo module + 3–5 hashtags on this tweet only
- Optional Tweet 6: Quote or question to invite engagement

**LinkedIn (~400 words):**
- Hook same as Tweet 1 or stronger for professional audience
- 2–3 paragraphs: what you learned, how it connects to H&C, why it matters for AI/education
- CTA: "Full writeup on Substack — link in bio"
- 5–8 hashtags at the end

**Reddit:**
- Target subreddit recommendation (r/learnmachinelearning, r/MachineLearning, r/ADHD, etc.)
- Title: "What I learned studying [topic] at doctoral depth — and one thing that surprised me"
- Body: lead with the insight, give curriculum context, link at end, ask a specific question to invite discussion

**Substack Note (2–3 sentences):**
- "Just completed M[XX]: [title]. [One surprising thing]. [How it changes H&C]. Full post: [link]"

4. After drafting, say:
   "All platform copy ready. Posting order: Substack → X thread → Notes → Reddit (same day) → LinkedIn (Day +1) → Medium (Day +14)."
   
5. Offer to update content-log.md in the hub with the pending publication entries.
