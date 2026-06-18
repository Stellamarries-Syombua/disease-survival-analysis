#  Disease Survival Analysis – Breast Cancer Recurrence

**Survival Analysis of Time-to-Recurrence in Node-Positive Breast Cancer Patients**

---

## Project Overview

This repository presents a complete **survival analysis** workflow on the **German Breast Cancer Study Group (GBSG2)** dataset using the `lifelines` library in Python. 

The focus is on modeling **recurrence-free survival time** - how long patients remain free from cancer recurrence after treatment, and identifying key clinical factors that influence prognosis. This is a classic time-to-event analysis that properly handles censored data (patients who did not experience recurrence by the end of follow-up).

**Dataset**: GBSG2 (1984–1989 clinical trial)  
**Patients**: 686 women with node-positive breast cancer  
**Key Outcome**: `time` (days to recurrence or censoring) + `cens` (event indicator)

---

## Objectives

- Perform exploratory data analysis with a survival lens (distributions, censoring patterns, group comparisons).
- Estimate survival curves using the **Kaplan-Meier estimator**.
- Build and interpret a **Cox Proportional Hazards (PH)** multivariable model.
- Validate model assumptions (proportional hazards) and assess discrimination (concordance index).
- Generate interpretable visualizations and predictions for clinical insight.
- Deploy an interactive Streamlit application for exploring patient risk profiles.

---

## Dataset – GBSG2

**Source**: German Breast Cancer Study Group 2 (available via `lifelines.datasets`)

**Features**:
- `horTh`: Hormonal therapy (yes/no)
- `age`: Age at diagnosis (years)
- `menostat`: Menopausal status (Pre/Post)
- `tsize`: Tumor size (mm)
- `tgrade`: Tumor grade (I/II/III)
- `pnodes`: Number of positive lymph nodes
- `progrec`: Progesterone receptor level
- `estrec`: Estrogen receptor level
- `time`: Time to event or censoring (days)
- `cens`: Event indicator (1 = recurrence, 0 = censored)

**Key Statistics**:
- 686 patients
- ~44% experienced recurrence during follow-up
- Median follow-up time: ~1084 days
- Significant right-censoring present

---

## Methodology

### 1. Data Preparation & EDA
- Loaded raw GBSG2 data
- Feature engineering (log transformations for skewed variables like receptor levels)
- Visualized distributions, correlations, and event rates by clinical subgroups
- Explored impact of hormonal therapy, tumor grade, lymph nodes, etc.

### 2. Non-Parametric Survival Analysis
- **Kaplan-Meier** overall survival curve
- Stratified KM curves by:
  - Hormonal therapy status
  - Tumor grade
  - Menopausal status
  - Age groups
  - Number of positive nodes

### 3. Semi-Parametric Modeling
- **Cox Proportional Hazards Model** (multivariable)
- Checked proportional hazards assumption using Schoenfeld residuals
- Generated forest plot for hazard ratios

### 4. Model Diagnostics & Predictions
- Concordance Index (C-index) evaluation
- Individual patient survival probability predictions
- Adjusted survival curves

### 5. Deployment
Interactive Streamlit app (`app.py`) for dynamic exploration.

---

## Key Findings & Results

### Survival Estimates
- Overall median recurrence-free survival: **~1,800+ days** (varies by subgroups)
- Hormonal therapy (`horTh = yes`) significantly improves survival curves
- Higher tumor grade and more positive lymph nodes strongly associated with worse prognosis

### Cox PH Model Highlights
- **Strongest predictors** (from hazard ratios):
  - Number of positive lymph nodes (`pnodes`) → higher risk
  - Tumor size (`tsize`)
  - Tumor grade
  - Hormonal therapy (protective effect)
  - Receptor levels (progrec, estrec)

- **Model Performance**: Concordance Index (C-index) shown in comparison plots (typically 0.65–0.70 range for this dataset)

**Clinical Insights**:
- Hormonal therapy provides clear protective benefit: visible in both KM and adjusted survival curves.
- Lymph node involvement remains one of the most powerful prognostic factors.
- Receptor status and menopausal status also play important roles.

---

## 📁 Repository Structure
