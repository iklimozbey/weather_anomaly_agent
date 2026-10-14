import pandas as pd


def build_report(df: pd.DataFrame) -> str:
    anomalies = df[df["anomaly"]]
    lines = [f"{len(anomalies)} anomali / {len(df)} kayıt"]
    if not anomalies.empty:
        lines.append(anomalies.head(10).to_string(index=False))
    return "\n".join(lines)


def llm_summary(report: str) -> str:
    """İsteğe bağlı: raporu bir LLM'e özetlettir. Şimdilik pas geçiyor."""
    return report
