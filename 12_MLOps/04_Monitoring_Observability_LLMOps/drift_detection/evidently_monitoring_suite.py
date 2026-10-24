"""Evidently AI Data Drift and Data Quality Monitoring Suite.

Generates visual HTML drift dashboards and extracts machine-readable JSON metrics
for Prometheus / Grafana ingestion.
"""

import json
from pathlib import Path
import numpy as np
import pandas as pd

try:
    from evidently.report import Report
    from evidently.metric_preset import DataDriftPreset, DataQualityPreset
    HAS_EVIDENTLY = True
except ImportError:
    HAS_EVIDENTLY = False


def generate_drift_report(
    reference_df: pd.DataFrame,
    current_df: pd.DataFrame,
    html_output_path: Path = Path("reports/data_drift_report.html"),
    json_output_path: Path = Path("reports/data_drift_metrics.json"),
) -> dict:
    """Generates comprehensive data drift analysis across all features."""
    html_output_path.parent.mkdir(parents=True, exist_ok=True)

    if HAS_EVIDENTLY:
        print("Generating Evidently AI Data Drift & Quality Report...")
        report = Report(metrics=[
            DataDriftPreset(),
            DataQualityPreset(),
        ])
        report.run(reference_data=reference_df, current_data=current_df)
        report.save_html(str(html_output_path))
        metrics_dict = report.as_dict()

        with open(json_output_path, "w", encoding="utf-8") as f:
            json.dump(metrics_dict, f, indent=2)

        print(f"Saved Evidently HTML dashboard to: {html_output_path}")
        print(f"Saved metric payload to: {json_output_path}")
        return metrics_dict
    else:
        # Fallback comprehensive reporting engine
        print("Evidently not installed. Using native statistical drift summary engine...")
        summary = {"dataset_drift": False, "drift_by_columns": {}}
        drift_count = 0

        for col in reference_df.select_dtypes(include=[np.number]).columns:
            ref_col = reference_df[col].dropna()
            curr_col = current_df[col].dropna()
            from scipy.stats import ks_2samp
            res = ks_2samp(ref_col, curr_col)
            drifted = bool(res.pvalue < 0.05)
            if drifted:
                drift_count += 1
            summary["drift_by_columns"][col] = {
                "drift_detected": drifted,
                "p_value": float(res.pvalue),
                "statistic": float(res.statistic),
            }

        summary["dataset_drift"] = drift_count > (len(reference_df.columns) / 3)
        summary["drifted_features_count"] = drift_count

        with open(json_output_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)

        # Generate minimal clean HTML dashboard
        html_content = f"""<!DOCTYPE html>
<html>
<head><title>MLOps Data Drift Report</title>
<style>body{{font-family:system-ui;padding:24px;background:#f8fafc;color:#1e293b}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #cbd5e1;padding:8px 12px;text-align:left}}th{{background:#e2e8f0}}.drift{{color:#dc2626;font-weight:bold}}.ok{{color:#16a34a;font-weight:bold}}</style>
</head>
<body>
<h2>Data Drift Monitoring Report</h2>
<p>Dataset Drift Detected: <b>{summary['dataset_drift']}</b> ({drift_count} features drifted)</p>
<table>
<tr><th>Feature</th><th>Drift Detected</th><th>p-value</th><th>KS Statistic</th></tr>
"""
        for feat, info in summary["drift_by_columns"].items():
            status_cls = "drift" if info["drift_detected"] else "ok"
            status_text = "DRIFT DETECTED" if info["drift_detected"] else "STABLE"
            html_content += f"<tr><td>{feat}</td><td class='{status_cls}'>{status_text}</td><td>{info['p_value']:.4e}</td><td>{info['statistic']:.4f}</td></tr>\n"
        html_content += "</table></body></html>"

        with open(html_output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Generated standalone HTML report: {html_output_path}")
        return summary


if __name__ == "__main__":
    np.random.seed(42)
    ref = pd.DataFrame({
        "trip_distance": np.random.exponential(3.0, 1000),
        "passenger_count": np.random.choice([1, 2, 3], 1000),
        "hour_of_day": np.random.randint(0, 24, 1000),
    })
    curr = pd.DataFrame({
        "trip_distance": np.random.exponential(5.5, 1000),  # Drifted!
        "passenger_count": np.random.choice([1, 2, 3], 1000),
        "hour_of_day": np.random.randint(0, 24, 1000),
    })
    generate_drift_report(ref, curr)
