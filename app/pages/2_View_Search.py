import streamlit as st
from app.queries import get_opportunities_filtered
from app.utils import CATEGORIES, WORK_MODES, STATUSES, EXPERIENCE_LEVELS, df_to_csv_bytes, show_no_data

st.title("🔍 View & Search Opportunities")

with st.sidebar:
    st.subheader("Filters")
    search    = st.text_input("Search (company / title / skills)")
    category  = st.selectbox("Category",       ["All"] + CATEGORIES)
    city      = st.text_input("City")
    work_mode = st.selectbox("Work Mode",      ["All"] + WORK_MODES)
    status    = st.selectbox("Status",         ["All"] + STATUSES)
    exp_level = st.selectbox("Experience",     ["All"] + EXPERIENCE_LEVELS)
    sal_min   = st.number_input("Min Salary",  min_value=0, value=0)
    sal_max   = st.number_input("Max Salary",  min_value=0, value=0)

df = get_opportunities_filtered(
    category  = None if category  == "All" else category,
    city      = city or None,
    work_mode = None if work_mode == "All" else work_mode,
    status    = None if status    == "All" else status,
    salary_min = sal_min or None,
    salary_max = sal_max or None,
    experience = None if exp_level == "All" else exp_level,
    search     = search or None,
)

st.metric("Records found", len(df))
if df.empty:
    show_no_data()
else:
    st.dataframe(df, use_container_width=True)
    st.download_button("📥 Export as CSV", df_to_csv_bytes(df), "opportunities.csv", "text/csv")