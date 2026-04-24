# Contributing to Bluprynt Docs

Thanks for improving the docs. This guide covers the contribution workflow and writing conventions.

## Quick contribution flow

1. Fork or branch off `main`.
2. Run `mint dev` and make your changes.
3. Run `mint broken-links` and fix any regressions.
4. Open a PR against `main`. The Mintlify preview builds automatically.
5. A reviewer merges and the site auto-deploys.

## When to open an issue vs a PR

- **Issue** — typo, broken link, conceptual error, missing topic, suggestion for a new page.
- **PR** — any of the above where you have the fix ready.

## Kinds of contribution we welcome

<!-- What to optimize for -->

- **Onboarding clarity.** Is something confusing on the first read? Fix it or tell us.
- **Code examples.** Real, runnable snippets beat prose every time.
- **Missing content.** Each empty stub page has a TODO — pick one.
- **API accuracy.** If an endpoint's behavior drifted, reflect it in the reference.
- **Diagrams.** Replace ASCII with SVG if you can improve clarity.

## Writing conventions

- **Voice.** Active, second person (`you`). Not royal plural.
- **Tense.** Present. `"Bluprynt returns…"`, not `"Bluprynt will return…"`.
- **Headings.** Sentence case. One H1 per page (set via frontmatter `title:`). H2 for major sections, H3 for subsections.
- **Sentence length.** One idea per sentence. Break long clauses.
- **Terminology.** See [`AGENTS.md`](./AGENTS.md) for product-specific terms.
- **Callouts.** Use them sparingly:
  - `<Note>` — neutral information.
  - `<Tip>` — optional, helpful advice.
  - `<Warning>` — something the user must know to avoid damage.
  - `<Info>` — context / caveat.
  - `<Check>` — checklist item.
- **Code blocks.** Always annotate language. Always include filename for multi-file examples.
- **Links.** Use relative paths for internal docs, full URLs for external.

## Components cheat sheet

| Component | Use |
|---|---|
| `<Card>` | Entry-point tile with icon + description |
| `<Columns cols={N}>` | Grid of Cards |
| `<CardGroup cols={N}>` | Same — legacy alias |
| `<AccordionGroup>` / `<Accordion>` | Progressive disclosure |
| `<Steps>` / `<Step>` | Sequential walkthrough |
| `<Tabs>` / `<Tab>` | Language / platform variants |

## Style

- Formatting is Prettier-style markdown. Wrap at natural paragraph boundaries, not at column limits.
- Use **en-dashes** (`–`) for ranges, **em-dashes** (`—`) for asides. `-` is only for hyphens and code.
- No trailing whitespace.
- One blank line between sections.

## Review

All PRs need one reviewer. For substantive content changes, cc an engineer in the product area you're documenting.

## Questions

[support@bluprynt.com](mailto:support@bluprynt.com) for content questions. [partners@bluprynt.com](mailto:partners@bluprynt.com) for partner-specific examples.
