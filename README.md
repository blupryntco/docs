# Bluprynt Docs

The source for [docs.bluprynt.com](https://docs.bluprynt.com) — the public documentation site for the Bluprynt compliance platform.

Built with [Mintlify](https://mintlify.com) and deployed automatically on push to `main` via the Mintlify GitHub app.

## What's here

- **Product docs** — Overview, KYI, Smart Disclosures, Compliance Hub, MiCA Checker.
- **Architecture** — System overview, attestation schemas, CCID, Policy Engine thesis.
- **Integration guides** — KYI widget embedding, public API, on-chain reads.
- **API reference** — Every endpoint, grouped by resource.
- **Getting started** — Account creation, first attestation walkthrough.

## Local development

```bash
# Install the Mintlify CLI
npm i -g mint

# Preview locally
mint dev
# → http://localhost:3000

# Check for broken links before pushing
mint broken-links
```

## File layout

```
docs/
├── docs.json                     # Mintlify config — navigation, theme, colors, logo
├── index.mdx                     # Home page
├── quickstart.mdx                # 15-minute first-time walkthrough
├── overview/                     # What Bluprynt is, architecture, key concepts
├── getting-started/              # Account creation + first attestation
├── core-products/
│   ├── kyi/                      # Know Your Issuer
│   ├── smart-disclosures/        # Smart Disclosures
│   ├── compliance-hub/           # Compliance Hub
│   └── mica-checker/             # MiCA Checker
├── architecture/                 # System overview, schemas, CCID, Policy Engine
├── integration-guides/           # KYI widget, public API, on-chain reads
├── api-reference/                # REST API reference per resource
├── logo/                         # light.svg + dark.svg
├── images/                       # Screenshots and diagrams
├── snippets/                     # Reusable MDX
└── favicon.svg
```

## Writing conventions

- Use **sentence case** for page titles and H2 headings.
- Active voice + second person (`you`).
- One idea per sentence.
- Bold for UI elements (`Click **Submit**`).
- Code formatting for identifiers (`bluprynt-api`), env vars (`API_KEY`), commands, and paths.
- Every new page adds a link from its parent to avoid orphans.

See [`AGENTS.md`](./AGENTS.md) for the full style guide (also loaded by AI writing assistants).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Links

- **Live docs:** [docs.bluprynt.com](https://docs.bluprynt.com)
- **Product:** [bluprynt.com](https://bluprynt.com)
- **Sign in:** [app.bluprynt.com](https://app.bluprynt.com)
- **Support:** [support@bluprynt.com](mailto:support@bluprynt.com)
- **GitHub org:** [github.com/blupryntco](https://github.com/blupryntco)
