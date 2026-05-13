# Random Variables and Stochastic Processes

**Course Notes for EE 6513 — University of New Brunswick**

*Kevin Englehart, PhD, PEng · Faculty of Engineering · Fredericton, NB*
© 2026 Kevin Englehart, PhD, PEng. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
---

## Overview

This repository contains the full LaTeX source for the course notes used in **EE 6513: Random Variables and Stochastic Processes** at the University of New Brunswick. The notes provide a rigorous yet accessible treatment of probability theory, stochastic analysis, and their engineering applications — from foundational axioms through to Kalman filtering and time-series analysis.

## Contents

The notes are organized into seven chapters:

| Chapter | Topic |
|---------|-------|
| 1 | **Probability** — axioms, conditional probability, Bayes' Rule, Bernoulli trials |
| 2 | **Random Variables** — distributions, density functions, CLT, moments, functions of RVs |
| 3 | **Stochastic Processes** — stationarity, power density spectrum, ergodicity, autocovariance |
| 4 | **Estimation** — Bayesian, maximum likelihood, and minimum mean square estimation |
| 5 | **Detection** — binary detection, Bayesian detector, performance in Gaussian white noise |
| 6 | **Optimal Filtering** — LTI systems with stochastic inputs, Wiener filters, Kalman filter |
| 7 | **Time-Series Analysis** — stationarity tests, ergodicity criteria, PSD estimation |

## Building the PDF

### Prerequisites

A standard TeX distribution is required. The document uses the following packages, which are included in most full installations (e.g. TeX Live, MiKTeX):

- `mathpazo`, `fontenc`, `microtype`
- `amsmath`, `amssymb`, `amsthm`
- `tikz` (with `arrows.meta`, `positioning`, `shapes.geometric`, `calc`)
- `tcolorbox` (with `breakable`, `skins`)
- `geometry`, `hyperref`, `titlesec`, `tocloft`, `fancyhdr`
- `graphicx`, `float`, `wrapfig`, `listings`, `xcolor`

### Compile

```bash
pdflatex EE6513_Notes_formatted.tex
pdflatex EE6513_Notes_formatted.tex   # second pass for cross-references and TOC
```

A `figures/` directory is expected in the same folder as the `.tex` file for any embedded images.

## Repository Structure

```
.
├── EE6513_Notes_formatted.tex   # Main source file
├── figures/                     # Figure assets referenced in the notes
└── README.md
```

## Usage

These notes are intended for registered students of **EE 6513** at the University of New Brunswick. Please refer to the colophon inside the document for the full copyright notice.

© 2026 Kevin Englehart. All rights reserved.

## Contact

Kevin Englehart, PhD, PEng  
Faculty of Engineering, University of New Brunswick  
Fredericton, NB, Canada
