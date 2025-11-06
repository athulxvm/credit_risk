"""
Demonstration of credit risk stress testing with macroeconomic scenarios.

This script reads a small dataset of fictional counterparties and assigns
a base probability of default (PD) based on each company's credit rating.
It then applies macroeconomic stress factors—representing mild and severe
recessions—by multiplying the base PD by a scenario factor. Expected loss
is computed as:

    Expected Loss (EL) = PD × LGD × Exposure

where LGD (loss given default) is assumed to be 45%.  The results are
written to a CSV file, and simple bar charts are generated to visualise
exposure and expected losses under each scenario. These charts can be
imported into Power BI or another tool for further analysis.

Usage:
    python risk_scenario.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load the counterparty dataset from a CSV file."""
    return pd.read_csv(path)


def map_ratings_to_pd(df: pd.DataFrame) -> pd.DataFrame:
    """Assign a base probability of default (PD) based on credit rating.

    Ratings are mapped to simple PDs (expressed as decimals).  Unknown
    ratings default to 5%.
    """
    rating_pd = {
        "AAA": 0.001,
        "AA": 0.002,
        "A+": 0.0025,
        "A": 0.003,
        "A-": 0.004,
        "BBB+": 0.005,
        "BBB": 0.006,
        "BBB-": 0.007,
        "BB+": 0.015,
        "BB": 0.020,
    }
    df = df.copy()
    df["pd_base"] = df["rating"].map(rating_pd).fillna(0.05)
    return df


def apply_scenarios(df: pd.DataFrame, lgd: float = 0.45) -> pd.DataFrame:
    """Apply macroeconomic scenarios to compute PD and expected loss.

    Two stress scenarios are applied:
      - mild_recession: PD × 1.25
      - severe_recession: PD × 1.75
    """
    df = df.copy()
    scenarios = {
        "base": 1.0,
        "mild_recession": 1.25,
        "severe_recession": 1.75,
    }
    for scenario, factor in scenarios.items():
        pd_col = f"pd_{scenario}"
        el_col = f"el_{scenario}_eur_m"
        df[pd_col] = df["pd_base"] * factor
        df[el_col] = df[pd_col] * lgd * df["exposure_eur_m"]
    return df


def save_results(df: pd.DataFrame, out_dir: str) -> None:
    """Save the scenario results to CSV."""
    os.makedirs(out_dir, exist_ok=True)
    df.to_csv(os.path.join(out_dir, "scenario_results.csv"), index=False)


def plot_bar_chart(x, y, title: str, ylabel: str, out_path: str) -> None:
    """Generate and save a bar chart."""
    plt.figure(figsize=(8, 4))
    plt.bar(x, y)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path, dpi=150)
    plt.close()


def generate_charts(df: pd.DataFrame, out_dir: str) -> None:
    """Generate exposure and expected loss charts for each scenario."""
    # Exposure chart (same for all scenarios)
    plot_bar_chart(
        x=df["name"],
        y=df["exposure_eur_m"],
        title="Exposure by Counterparty",
        ylabel="Exposure (EUR million)",
        out_path=os.path.join(out_dir, "exposure_by_counterparty.png"),
    )
    # Expected loss charts per scenario
    scenarios = ["base", "mild_recession", "severe_recession"]
    for scenario in scenarios:
        el_col = f"el_{scenario}_eur_m"
        plot_bar_chart(
            x=df["name"],
            y=df[el_col],
            title=f"Expected Loss ({scenario.replace('_', ' ').title()})",
            ylabel="Expected Loss (EUR million)",
            out_path=os.path.join(out_dir, f"expected_loss_{scenario}.png"),
        )


def main() -> None:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(repo_root, "data", "counterparties.csv")
    out_dir = os.path.join(repo_root, "outputs")
    # Load data and map ratings
    df = load_data(data_path)
    df = map_ratings_to_pd(df)
    df = apply_scenarios(df)
    # Save results and generate charts
    save_results(df, out_dir)
    generate_charts(df, out_dir)
    # Print a summary to console
    summary_cols = [
        "counterparty_id",
        "name",
        "rating",
        "exposure_eur_m",
        "pd_base",
        "el_base_eur_m",
        "el_mild_recession_eur_m",
        "el_severe_recession_eur_m",
    ]
    print(df[summary_cols])


if __name__ == "__main__":
    main()