# Detecting Critical Transitions in the Human Innate Immune System

## Introduction
Critical transitions refer to sudden or abrupt shifts in the state of complex dynamical systems that happens when certain conditions of the system pass through a critical or bifurcation point. In this section of the report, we investigate if critical transitions also occur in the human innate immune system. By using the baseline model of the innate immunity for patients undergoing cardiac surgery, we perturb the system by adding stochasticity to the concentration of inflammation triggering moieties by introducing various types of noise. We then use Early Warning Signals to detect critical transitions in the stochastic human innate immune system. 


## Files Included

The repository contains 6 folders: 
1. `datasets` : contains patient data
2. `images` : contains generated gif images
3. `notebooks` : does the heavy lifting in computational modeling
4. `result` : contains results of the simulations
5. `scratch` : contains test codes
6. `utils` : contains codes of helper functions

The science happens in the notebooks. Below is a short list and description of each one of them.

1. `Part 0 - 3D Plots.ipynb` : plots the time series data of patients in 3D
2. `Part 0 - Dimensionality Reduction.ipynb` : deals with dimensionality reduction using different methods
3. `Part 1 - Bifurcation (Deterministic Model of HIIS).ipynb` : looks into the bifurcation analyses of the time series
4. `Part 1 - PCA.ipynb` : focuses on PCA
5. `Part II - Stochastic Immunity (Manual Run).ipynb` : adding different types of noise, where each experiment is run manually
7. `Part II - Stochastic Immunity (On-Off).ipynb` : explores switching off/probability of nonproduction of certain concentrations
9. `Part III - EWS.ipynb` : code for early warning signals
10. `Part IV - EWS on Data.ipynb` : explores early warning signals on data

## References
1. Detecting Critical Transitions in the Human Innate Immune System Post-cardiac Surgery [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7302275/]