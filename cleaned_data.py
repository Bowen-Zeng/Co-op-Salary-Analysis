import pandas as pd
from pathlib import Path 
import re
import numpy as np
from typing import Optional, Tuple

USD_TO_CAD = 1.35
HOURS_PER_WEEK = 40
WEEKS_PER_MONTH = 4
WEEKS_PER_TERM = 16

RAW_DATA_PATH = Path("data/raw/Waterloo_Co-op_Salaries_List_for_Analysis.csv")
CLEAN_DATA_PATH = Path("Processed/cleaned_salaries.csv")

def load_raw_data():
    # Skip the introductory note row and align columns with parser expectations
    df = pd.read_csv(RAW_DATA_PATH, skiprows=1, header=0)
    df.columns = ["company_role", "salary_raw"]
    return df

def normalize_text(s: str) -> str:
    if pd.isna(s):
        return ""
    return (
        s.lower()
        .replace(",", "")
        .strip()
    )

def detect_currency(s: str) -> str:
    if "usd" in s or "us $" in s:
        return "USD"
    return "CAD"

def detect_pay_period(s: str) -> Optional[str]:
    if any(k in s for k in ["hr", "hour"]):
        return "hourly"
    if "week" in s:
        return "weekly"
    if "month" in s:
        return "monthly"
    if "term" in s or "4 month" in s or "4-month" in s:
        return "term"
    if "stipend" in s:
        return "stipend"
    return None

def extract_numeric_values(s: str) -> Optional[float]:
    numbers = [float(n) for n in re.findall(r"\d+\.?\d*", s)]
    if not numbers:
        return None

    # Handle ranges or seniority increases by midpoint
    return sum(numbers) / len(numbers)
    
def normalize_to_hourly(value: float, period: str) -> Optional[float]:
    if value is None or period is None:
        return None

    if period == "hourly":
        return value
    if period == "weekly":
        return value / HOURS_PER_WEEK
    if period == "monthly":
        return value / (WEEKS_PER_MONTH * HOURS_PER_WEEK)
    if period in ["term", "stipend"]:
        return value / (WEEKS_PER_TERM * HOURS_PER_WEEK)

    return None

def convert_to_cad(value: float, currency: str) -> Optional[float]:
    if value is None:
        return None
    if currency == "USD":
        return value * USD_TO_CAD
    return value

def parse_salary(salary_raw: str) -> Tuple[Optional[float], str, Optional[str]]:
    s = normalize_text(salary_raw)

    currency = detect_currency(s)
    period = detect_pay_period(s)
    numeric_value = extract_numeric_values(s)

    hourly = normalize_to_hourly(numeric_value, period)
    hourly_cad = convert_to_cad(hourly, currency)

    return hourly_cad, currency, period

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower().str.strip()

    parsed = df["salary_raw"].apply(parse_salary)

    df["salary_cad_hourly"] = parsed.apply(lambda x: x[0])
    df["currency_original"] = parsed.apply(lambda x: x[1])
    df["pay_period"] = parsed.apply(lambda x: x[2])

    # Drop rows we couldn't parse
    df = df.dropna(subset=["salary_cad_hourly"])

    # Sanity filter
    df = df[(df["salary_cad_hourly"] > 5) & (df["salary_cad_hourly"] < 200)]

    # Split company_role into company and role
    df["company"] = df["company_role"]
    df["role"] = ""  # Role is not separated in the original data

    # Calculate annual salary in USD
    # Annual = hourly * 40 hrs/week * 52 weeks/year
    # Convert CAD to USD by dividing by USD_TO_CAD
    df["salary_annual_usd"] = (df["salary_cad_hourly"] * 40 * 52) / USD_TO_CAD

    return df


def main():
    df_raw = load_raw_data()
    df_clean = clean_data(df_raw)

    CLEAN_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)

    print(f"Cleaned {len(df_clean)} rows saved to {CLEAN_DATA_PATH}")

if __name__ == "__main__":
    main() 