# Changelog

All notable changes to the **brief** marketing skill. Each entry links to the full
GitHub release notes. Versioning is semantic-ish: minor bumps for new modules,
behaviors, or tooling; the installed skill reports its version in
`~/.claude/skills/marketing/VERSION`.

## [1.8.0] — 2026-07-01

- `VERSION` file ships inside the installed skill — installed users can finally tell
  what they're running.
- `install.sh` / `install.ps1` now install the **latest release by default** (instead
  of tracking `main`) and support pinning: `--ref v1.7.0` (bash) or `$env:BRIEF_REF`
  (PowerShell). Both print the installed version.
- This `CHANGELOG.md`.

## [1.7.0] — 2026-07-01 · [release](https://github.com/inerrata/brief/releases/tag/v1.7.0)

- Format adapters generated from `SKILL.md`: `dist/AGENTS.md` (Codex CLI / Gemini CLI)
  and `dist/.cursorrules` (Cursor), preserving progressive disclosure outside Claude.
- `build/build_adapters.py` + CI `adapters-in-sync` job that fails on any drift
  between `SKILL.md` and the committed adapters.

## [1.6.0] — 2026-06-25 · [release](https://github.com/inerrata/brief/releases/tag/v1.6.0)

- Deterministic (grader-free) eval layer: 52 code-checked assertions across v3/v4/v5
  (30 triggering + 22 structural) — no model grades anything.
- GitHub Actions CI gate runs the checks + JSON validity on every push/PR.

## [1.5.0] — 2026-06-23 · [release](https://github.com/inerrata/brief/releases/tag/v1.5.0)

- New modules: `localization.md` (transcreation, locale mechanics, native review) and
  `compliance.md` (substantiation, disclosure law, CAN-SPAM/GDPR, regulated
  categories, dark patterns). 17 modules total.
- v5 eval set (8 prompts): first post-v2 set with a real delta — 100% vs 92.1%
  baseline (+7.9 pp), driven by three load-bearing compliance/localization steps.

## [1.4.0] — 2026-06-17 · [release](https://github.com/inerrata/brief/releases/tag/v1.4.0)

- New modules: `social-media.md`, `paid-media.md`, `pr-comms.md`, `partnerships.md`.
  15 modules total.
- v4 eval set (10 prompts): honest +0 delta vs a strong agentic baseline — confirmed
  routing (10/10) and no regression; documented transparently.

## [1.3.0] — 2026-06-15 · [release](https://github.com/inerrata/brief/releases/tag/v1.3.0)

- Agentic Gate B: audits fetch the URL / find the asset in-repo before asking for a paste.
- Step 0.5 product-truth grounding; `brand.md` generation offer (strengthened after an
  eval caught it firing inconsistently — 0.80 → 1.00).
- New modules: `product-marketing.md`, `specs.md`. 11 modules total.
- v3 eval set (12 prompts): 100% vs 92.6% baseline (+7.4 pp).

## [1.2.0] — 2026-06-09 · [release](https://github.com/inerrata/brief/releases/tag/v1.2.0)

- `brand.md` standing brand profile read at Step 0 + `brand.template.md`.
- Working `install.sh` / `install.ps1`; wider implicit trigger phrases; honest eval
  badges with caveats.

## [1.1.0] — 2026-06-02 · [release](https://github.com/inerrata/brief/releases/tag/v1.1.0)

- Iteration-3 fixes for over-gating and honesty/measurement weak spots (six weak evals
  re-benchmarked to 1.00; projected 98.9%).
- Held-out v2 eval set: 24 AI-generated prompts, 122/122 assertions.

## [1.0.0] — 2026-05-29 · [release](https://github.com/inerrata/brief/releases/tag/v1.0.0)

- Initial release: `SKILL.md` routing layer + 9 reference modules, brief-first
  gates (A: strategy statements, B: audits), deliver-first rules, universal quality
  bar, 26-prompt eval suite with benchmarks (iteration-1: 82.7% vs 62.3% baseline).
