# CLAUDE.md — Heston Model Project

## Purpose

This is a solo personal project by Lucas Hutton, a second-year BEng Mathematics and Computer Science student at Imperial College London. The primary goal is a polished, public GitHub repository that serves as a strong CV/LinkedIn piece demonstrating quantitative finance knowledge, mathematical rigour, and clean Python implementation skills. The target audience for the repo is quant finance recruiters and technical interviewers.

## End Goal

A public GitHub repository containing:
- A well-written PDF writeup (LaTeX) covering the theory from Black-Scholes foundations through to Heston model calibration
- Clean, well-structured Python code implementing BS pricing, Heston Monte Carlo simulation, Fourier pricing, and market calibration
- Three Jupyter notebooks demonstrating the model interactively
- A polished README with a screenshot of the calibrated vol surface and a link to the compiled PDF

## Project Structure

```
heston-model/
├── src/
│   ├── black_scholes.py       # BS pricer + implied vol inversion (Phase 1)
│   ├── heston_model.py        # HestonModel dataclass (Phase 2)
│   ├── monte_carlo.py         # Euler-Maruyama MC simulator (Phase 2)
│   ├── characteristic_fn.py   # Albrecher et al. stable CF (Phase 3)
│   ├── fourier_pricing.py     # Gil-Pelaez + Carr-Madan FFT pricer (Phase 3)
│   └── calibration.py         # Market data fetch + calibration pipeline (Phase 4)
├── notebooks/
│   ├── 01_model_overview.ipynb
│   ├── 02_pricing_comparison.ipynb
│   └── 03_calibration.ipynb
├── writeup/
│   └── main.tex               # LaTeX writeup (compiled PDF to be added)
├── requirements.txt
└── README.md
```

## Current Status

**Phase 1 — in progress**

Writeup:
- [x] §2.1 — Probability space, almost surely, filtration, adapted process, martingale
- [x] §2.2 — Brownian motion definition, martingale theorem (with proof), quadratic variation theorem
- [x] §2.3 — Itô's lemma (1D and 2D)
- [ ] §3 — Black-Scholes (GBM, formula, implied vol smile)

Code: not started

Infrastructure:
- [x] `writeup/main.tex` — full section skeleton, theorem environments, notation macros
- [x] `writeup/refs.bib` — Shreve (2004) entry added

---

## Five-Phase Work Plan

### Phase 1 — Black-Scholes Foundations
- Implement `black_scholes_price` and `implied_vol` (Brent's method) in `src/black_scholes.py`
- Write §2 (Mathematical Preliminaries: Brownian motion, Itô's lemma) and §3 (Black-Scholes) in the LaTeX writeup
- Milestone: working BS code and written motivation for the project

### Phase 2 — Heston Model: Theory & Simulation
- Implement `HestonModel` dataclass with parameter validation and Feller condition check
- Implement Monte Carlo simulator: correlated Brownian increments, Euler-Maruyama for v_t (full truncation), log-Euler for S_t
- Write §4 (The Heston Model: SDEs, parameters, Feller condition, risk-neutral dynamics)
- Milestone: model specified and simulating

### Phase 3 — Characteristic Function & Fourier Pricing
- Implement characteristic function in Albrecher et al. numerically stable form
- Implement Gil-Pelaez inversion pricer (`scipy.integrate.quad`) and Carr-Madan FFT pricer
- Write §5 (Characteristic Function) and §6 (Fourier Pricing)
- Tests: put-call parity, CF(0)=1, CF(-i)=e^{rT}, MC vs Fourier agreement
- Milestone: fast, accurate Fourier pricer verified against Monte Carlo

### Phase 4 — Calibration to Market Data
- Fetch SPY/SPX options chain via yfinance; filter by liquidity and moneyness (0.85–1.15), 7–365 days
- Build implied vol surface using BS inverter
- Calibrate Heston parameters: MSE in implied vol space, differential_evolution then Nelder-Mead
- Write §7 (Calibration)
- Milestone: market data in, fitted Heston parameters out

### Phase 5 — Results, Writeup & GitHub Polish
- Hero plot: calibrated Heston surface overlaid on market implied vols
- Parameter sensitivity plots (κ, θ, ρ, ξ)
- Monte Carlo vs Fourier comparison table
- Write §8 (Results), §9 (Conclusion), §1 (Introduction — written last)
- Three Jupyter notebooks
- Polish README: compiled PDF link, vol surface screenshot, one-paragraph summary
- Milestone: public repo ready for CV

## Code Style & Conventions

- Python with type hints throughout
- NumPy for numerical work; SciPy for integration and optimisation; Matplotlib for plots; yfinance for market data
- Docstrings on all public functions (NumPy docstring style), but no inline comments unless the reason is non-obvious
- Module-level docstrings explain the role of each file (see `black_scholes.py` as template)
- No Jupyter notebooks used for implementation logic — notebooks are demonstration-only wrappers around `src/`
- The LaTeX writeup should be self-contained and mathematically rigorous: define every term, state every theorem used, and cite every external result

## Key References

- Heston (1993) — original paper
- Shreve, *Stochastic Calculus for Finance II* — mathematical foundations
- Gatheral, *The Volatility Surface* — intuition and calibration
- Rouah, *The Heston Model and Its Extensions in Finance and Insurance* — implementation details
- Carr & Madan (1999) — FFT pricing method
- Albrecher et al. (2007) — numerically stable characteristic function form

## Motivation

This is a personal project driven by genuine interest in mathematical finance and quantitative methods. The goal is to understand the Heston model deeply — from the measure-theoretic foundations through to calibration against real market data — not just to produce something that runs.

The three things I care about in this project:
1. **Mathematical depth** — every result stated precisely, proved or cited, and connected to the broader theory rather than treated as a black box
2. **Implementation quality** — clean, well-tested, well-documented Python written to a standard I'd be comfortable defending in a technical interview
3. **Practical grounding** — calibrating to real SPX options data, closing the loop between theory and market reality

This is the kind of project I'd want to build regardless of who reads it — but it is also intended to be a strong CV piece that gives an honest picture of how I approach a problem at the intersection of mathematics, computation, and finance.
