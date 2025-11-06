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
├─ outputs/
│  ├─ scenario_results.csv    – results table with PDs and expected losses
│  ├─ exposure_by_counterparty.png
│  ├─ expected_loss_base.png
│  ├─ expected_loss_mild_recession.png
│  └─ expected_loss_severe_recession.png
└─ LinkedIn_post.md           – ready‑made post summarising the project
```

## Data

The **data/counterparties.csv** file contains five fictional
companies with their sector, credit rating and an approximate
exposure in EUR millions.  A simple mapping converts credit ratings
to base PDs:

| Rating | PD   |
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

3. Inspect the printed summary in the console or open the CSV to see
   PD and expected loss for each counterparty under every scenario.

## Building a Power BI dashboard

While this repository does not include a `.pbix` file, you can quickly
create a dashboard using the output data:

1. **Open Power BI Desktop** and choose **Get data → Text/CSV**.
2. **Select** `scenario_results.csv` from the `outputs` folder.
3. In the **Fields** pane, drag `name` to the *Axis* and select one
   of the expected loss columns (e.g. `el_mild_recession_eur_m`) for
   the *Values* to create a bar chart.  Repeat with the other
   expected loss columns to create additional visuals.
4. Add a **slicer** for `scenario` if you transform the data into a
   long format (not shown here) or simply create separate charts for
   each scenario as in the provided images.
5. Optionally add a **card** visual showing the **total expected
   loss** by summing the selected expected loss column.

This simple dashboard will let you interactively explore how
expected losses change when macro conditions worsen.  Use colours
and additional filters to make the report more engaging.

## How to explain this in an interview

- **Business context:** Explain that banks and corporates monitor
  counterparties’ credit risk.  Macroeconomic downturns tend to
  increase defaults, so stress testing is essential.
- **Your approach:** “I took a handful of counterparties, assigned base
  default probabilities from their ratings and simulated how those
  probabilities rise during a mild or severe recession.  Using a
  constant LGD, I converted PDs into expected losses.”
- **Key insight:** Demonstrate that even a modest rise in PD (25 %) can
  significantly boost expected losses, highlighting the importance
  of preparing for downturns.
- **Digital skills:** Emphasise that you automated the calculations in
  Python and prepared a dataset ready for a Power BI dashboard.  This
  shows both analytical thinking and a simple form of
  digitalisation, which are valuable in modern finance teams.

## LinkedIn post

A ready‑to‑use LinkedIn summary of this project can be found in
`LinkedIn_post.md`.