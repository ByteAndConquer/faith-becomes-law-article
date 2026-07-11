# When Faith Becomes Law: Christianity, Political Power, and the Limits of Religious Authority

## Overview

This repository contains the working manuscript and source files for **“When Faith Becomes Law: Christianity, Political Power, and the Limits of Religious Authority.”** Git records the article’s drafting and revision history, while the Gitea Actions workflow produces versioned PDF and submission-package artifacts from release tags.

## Project structure

```text
.
├── .gitea/workflows/
│   └── build-article.yml
├── .github/workflows/
│   └── article-stats.yml
├── sections/
│   ├── 01-introduction.md
│   ├── 02-christianity-as-cultural-and-moral-force.md
│   ├── 03-from-moral-persuasion-to-legal-control.md
│   ├── 04-when-doctrine-polices-knowledge.md
│   ├── 05-selective-literalism-and-moral-convenience.md
│   ├── 06-performative-christianity-and-political-legitimacy.md
│   ├── 07-politicized-evangelicalism-and-christian-nationalism.md
│   ├── 08-the-limits-of-religious-authority.md
│   ├── 09-consequences-for-those-outside-the-dominant-faith.md
│   ├── 10-global-and-interreligious-comparison.md
│   ├── 11-religious-participation-vs-religious-domination.md
│   └── 12-conclusion-protecting-faith-by-limiting-power.md
├── tools/
│   └── validate_article.py
├── abstract.md
├── main.md
├── outline.md
├── references.bib
└── Makefile
```

## Local validation and build

### Prerequisites

- Python 3
- Pandoc
- XeLaTeX, normally provided by TeX Live or MiKTeX

### Commands

```bash
make validate   # Check section synchronization and citation integrity
make            # Validate and build output/main.pdf
make clean      # Remove generated output
```

Pandoc’s built-in author-date citation style is used, so no external CSL file is required.

## Tagged draft builds

The Gitea workflow runs for tags matching `draft-*`, `v*`, or `submission-*`. A first draft build can be started with:

```bash
git tag -s draft-0.1.0 -m "First complete tagged draft"
git push origin draft-0.1.0
```

Use `git tag -a` instead of `git tag -s` when a signing key is not configured. The runner validates the manuscript, builds a versioned PDF, creates a clean submission ZIP, and uploads both as Gitea Actions artifacts.

_Last updated: July 2026_
