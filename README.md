# When Faith Becomes Law: Christianity, Political Power, and the Limits of Religious Authority

## Overview

This repository contains the working draft of the journal article **"When Faith Becomes Law: Christianity, Political Power, and the Limits of Religious Authority"**.

It tracks the complete writing and revision history using Git with PGP-signed commits for integrity and provenance.

---

## Project Structure

```text
.
├── main.md                 # Main document (combines everything)
├── abstract.md
├── outline.md
├── sections/
│   ├── 01-introduction.md
│   ├── 02-historical-context.md
│   ├── 03-theological-foundations.md
│   ├── 04-political-power-and-law.md
│   ├── 05-limits-of-religious-authority.md
│   └── 06-conclusion.md
├── figures/                # Images, charts, diagrams
├── references.bib          # Bibliography
├── Makefile                # Build instructions (Pandoc → PDF)
├── .gitattributes
├── .gitignore
└── output/                 # Generated PDFs (not tracked)
```

---

## Building the Paper

### Prerequisites

- [Pandoc](https://pandoc.org/installing.html)
- XeLaTeX (part of TeX Live or MiKTeX)

### Commands

```bash
make          # Build the PDF
make clean    # Remove temporary files
```

---

_Last updated: July 2026_
