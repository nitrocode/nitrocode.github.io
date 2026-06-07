# Claude preferences

## Writing style

- No em dashes (U+2014, the character that looks like a long dash: —). Use a comma, period, or restructure the sentence instead.
- No other AI writing artifacts: no "delve", no "it is worth noting", no "in conclusion", no filler throat-clearing.
- Keep prose direct, short, and conversational. Plain language over formal.
- Avoid hedging phrases like "I cannot", "please note that", "as an AI".

## Blog posts

- Use `BLOG_POST_TEMPLATE.md` at repo root as the skeleton for new posts.
- Audience is mixed (leaders + engineers). TL;DR plus a callout table near the
  top gives leaders a stop point; deeper sections serve engineers.
- Standard section order: TL;DR → Why this matters → What I did → How I did it
  → What I would do differently → Takeaways.
- STAR is implicit in the structure. Situation = "Why this matters", Task =
  the `**Goal**:` line at the top of "What I did", Action = "What I did" +
  "How I did it", Result = TL;DR + callout table. Recruiters can lift each
  letter in a 60-second skim.
- Voice is first-person, retrospective.
- Fully generic content. No employer name, no commercial vendor names unless
  the post is explicitly about a public OSS tool. Use category descriptors
  (e.g. "CNAPP", "policy-as-code engine", "database access proxy").
- Numbers as orders of magnitude (tens, hundreds, a petabyte). No dollar
  figures tied to an employer.
- Length target: 5-10 minute read (~1000-2500 words). Each line must earn
  its place. Cut filler ruthlessly. "Every line justified" is the bar.
- Executive readability: a non-technical executive should be able to read
  the TL;DR, callout table, and "Why this matters" sections and walk away
  with the headline and the business value. Technical depth belongs in
  "How I did it."
- No redundancies across the suite. Before writing a new post, scan
  existing `_drafts/` and `_posts/` content; if the lesson overlaps
  meaningfully with an existing post, either cut the redundancy or fold
  the new content into the existing post.
- Section budget (devil's-advocate rules):
  - "What I would do differently": 2-4 bullets, forward-looking framing
    ("Ship X first" not "I should have shipped X first"). Cut filler. If you
    cannot get to 2 genuine lessons, the section should not exist.
  - "Takeaways": 3-6 bullets, each unique to the post. Cut anything that
    restates another section or reads as generic industry advice.
- Self-score and grade at the end of every draft, in an HTML comment
  block (`<!-- ... -->`) so the rubric survives in markdown source but
  does not render. Rubric (out of 100):
  - Tone (15)          : matches voice, no AI-isms, no em dashes
  - Clarity (20)       : STAR is cleanly identifiable
  - Brevity (15)       : hits the 5-10 minute target
  - Evidence (20)      : concrete numbers, patterns, outcomes
  - Uniqueness (15)    : does not overlap with other posts in the suite
  - Narrative fit (15) : advances the professional story arc
  - Grades: A 90+, B 80-89, C 70-79, D <70.
- Address gaps identified in the self-score before promoting to
  `_posts/`. List the gaps explicitly in the comment block and either
  fix them or note why they were left.
- Workflow: draft into `_drafts/` (Jekyll ignores it for deploy), review, then
  `mv` to `_posts/` once approved. Filename for `_posts/` must be
  `YYYY-MM-DD-slug.md`. Permalink convention is `/blog/<slug>/`.
- Preview locally with `bundle exec jekyll serve --drafts`.

