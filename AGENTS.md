# Documentation project instructions

Context for AI writing assistants (and humans skimming for conventions) working on this docs repo.

## About this project

- Mintlify-backed docs at [docs.bluprynt.com](https://docs.bluprynt.com).
- Pages are MDX with YAML frontmatter (`title:`, `description:`).
- Configuration lives in [`docs.json`](./docs.json) — navigation, theme, colors, footer.
- Run `mint dev` to preview.
- Run `mint broken-links` before shipping.

## Mintlify knowledge

Install the Mintlify skill for component reference and conventions:
```
npx skills add https://mintlify.com/docs
```

## Terminology

Preferred terms across Bluprynt docs:

| Use | Not |
|---|---|
| **Organization** | account, workspace, team |
| **Member** | user, employee |
| **Identity** (with type: asset/issuer/regulator) | user, entity, account |
| **CCID** | Bluprynt ID, identifier, identity ID |
| **Attestation** | certificate, assertion, credential (credential is distinct — see below) |
| **Credential** | attestation (credentials are a *kind* of attestation) |
| **Smart Disclosure** | disclosure (when referring to Bluprynt's specific product), filing, document |
| **Policy module** | smart contract, rule, logic |
| **Compliance Hub** | dashboard, supervisor UI |
| **KYI** (Know Your Issuer) | not to be confused with KYC |
| **On-chain** (hyphenated) | onchain |
| **Web3** (capitalized) | web3 |

## Style preferences

- Active voice, second person (`you`). Not `we` for Bluprynt-authored content (ambiguous).
- Sentence case for headings.
- One idea per sentence.
- Bold for UI elements: `Click **Settings**`.
- Code formatting for file names, env vars, commands, paths, identifiers.
- Prefer concrete examples over abstract description.
- When a page references a product, link to its section the first time.
- Use en-dash `–` for ranges, em-dash `—` for asides.
- Use British / American spelling consistently within a page — default American.

## What to document

- Customer-visible product behavior.
- Integrator-facing APIs, SDKs, widgets.
- Conceptual explanations of CCIDs, attestations, policy modules.
- Regulatory frameworks Bluprynt operates under.

## What NOT to document

- Internal admin endpoints (`/api/admin/*` in `bluprynt-api`) — not partner-facing.
- Infrastructure details only Bluprynt ops need — those live in the individual repo READMEs.
- Work-in-progress features not yet in production.
- Specific customer names, prices, or commercial terms — those belong on [bluprynt.com](https://bluprynt.com).

## Writing new pages

1. Add the MDX file in the right directory.
2. Include frontmatter: `title:` (sentence case), `description:` (one line, end with period).
3. Add the page to the appropriate group in `docs.json`.
4. Cross-link from parent + sibling pages.
5. Preview with `mint dev`.
6. Run `mint broken-links`.

## Stubs

Scaffolded pages may have TODOs or `<Note>` placeholders for content not yet migrated. Flag these as they're found and either expand or remove.
