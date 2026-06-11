# app/utils.py
# WHY: Reusable helper functions used across multiple pages.

import pandas as pd
import streamlit as st

CATEGORIES       = ["Data Science", "AI", "Web Development", "Cyber Security", "Software Engineering"]
WORK_MODES       = ["Remote", "Onsite", "Hybrid"]
STATUSES         = ["Open", "Closed", "Expired", "Shortlisted"]
EXPERIENCE_LEVELS = ["Entry", "Mid", "Senior"]
CURRENCIES       = ["PKR", "USD", "EUR", "GBP"]

def df_to_csv_bytes(df: pd.DataFrame) -> bytes:
    """Convert DataFrame to CSV bytes for st.download_button."""
    return df.to_csv(index=False).encode("utf-8")

def show_no_data():
    st.info("No records found matching your criteria.")

def format_salary(row):
    if pd.isna(row["salary_min"]) and pd.isna(row["salary_max"]):
        return "Not specified"
    return f"{row['currency']} {int(row['salary_min'] or 0):,} – {int(row['salary_max'] or 0):,}"