import streamlit as st
import pandas as pd
from app.auth import require_admin
from app.queries import bulk_insert, get_opportunities_filtered
from app.utils import df_to_csv_bytes

st.title("📁 CSV Upload & Export")
tab1, tab2 = st.tabs(["Upload CSV", "Export CSV"])

with tab1:
    require_admin()
    st.markdown("Upload a CSV with columns matching the opportunities table.")
    st.download_button("📥 Download CSV Template",
        "company_name,job_title,category,city,country,work_mode,required_skills,salary_min,salary_max,currency,experience_level,application_deadline,status,source_link\n",
        "template.csv", "text/csv")
    
    uploaded = st.file_uploader("Choose CSV file", type=["csv"])
    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            st.subheader("Preview (first 10 rows)")
            st.dataframe(df.head(10))
            st.info(f"Total rows: {len(df)}")
            if st.button("Insert valid rows into database"):
                count, errors = bulk_insert(df)
                st.success(f"✅ Inserted {count} rows.")
                if errors:
                    st.warning("Some rows had errors:")
                    for e in errors:
                        st.text(e)
                st.cache_data.clear()
        except Exception as e:
            st.error(f"Could not read CSV: {e}")

with tab2:
    st.subheader("Export filtered data")
    df = get_opportunities_filtered()
    st.dataframe(df, use_container_width=True)
    st.download_button("📥 Export All as CSV", df_to_csv_bytes(df), "export.csv", "text/csv")