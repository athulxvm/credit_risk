# Macroeconomic Scenario Credit Risk Demo

This mini‑project demonstrates how macroeconomic conditions can affect
credit risk.  It uses a small fictional dataset of five counterparties,
assigns each a base probability of default (PD) based on its credit
rating and then applies stress factors for *mild* and *severe* recession
scenarios.  The script outputs expected losses under each scenario and
generates bar charts that you can import into Power BI to build an
interactive dashboard.

## Contents

```
macro_credit_risk_scenarios/
├─ README.md                 – project overview and instructions
├─ data/
│  └─ counterparty.csv        – sample counterparty data
├─ src/
│  └─ risk_scenario.py        – Python script to compute scenarios
└─ outputs/
   ├─ scenario_results.csv    – results table with PDs and expected losses
   ├─ exposure_by_counterparty.png
   ├─ expected_loss_base.png
   ├─ expected_loss_mild_recession.png
   └─ expected_loss_severe_recession.png

```

## Data

The **data/counterparties.csv** file contains five fictional
companies with their sector, credit rating and an approximate
exposure in EUR millions.  A simple mapping converts credit ratings
to base PDs:

| Rating|  PD  |
|-------|------|
| A     | 0.30%|
| A‑    | 0.40%|
| BBB   | 0.60%|
| BBB‑  | 0.70%|
| BB+   | 1.50%|

This mapping is **illustrative**; the focus of the exercise is on the
relative impact of macro scenarios, not on exact PDs.

## Scenarios

Three macroeconomic scenarios are defined:

1. **Base:** no stress – PD unchanged.
2. **Mild recession:** PD is increased by 25 % (PD × 1.25).
3. **Severe recession:** PD is increased by 75 % (PD × 1.75).

In all cases the **Loss Given Default (LGD)** is assumed to be 45 %.
Expected loss is calculated as:

\[\mathrm{EL} = \mathrm{PD} \times \mathrm{LGD} \times \mathrm{Exposure}\]

## Running the script

1. Make sure Python 3.10+ and `pandas` & `matplotlib` are installed. In a
   fresh environment you can run:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install pandas matplotlib
   ```

2. Execute the script from the repository root:

   ```bash
   python src/risk_scenario.py
   ```

   This will generate `scenario_results.csv` in the **outputs** folder
   along with four bar charts.

3. Inspect the printed summary in the console or open the CSV in the outputs directory to see
   PD and expected loss for each counterparty under every scenario.


