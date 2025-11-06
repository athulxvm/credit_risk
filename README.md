# Macroeconomic Scenario Credit Risk Demo

This mini‑project demonstrates how macroeconomic conditions can affect
credit risk.  It uses a small fictional dataset of five counterparties,
assigns each a base probability of default (PD) based on its credit
rating and then applies stress factors for *mild* and *severe* recession
scenarios.  The script outputs expected losses under each scenario and
generates charts.

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



