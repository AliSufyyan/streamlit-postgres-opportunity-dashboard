import streamlit as st
from app.auth import require_admin
from app.queries import get_all_opportunities, get_opportunity_by_id, update_opportunity
from app import utils
import pandas as pd

require_admin()
st.title("✏️ Update Opportunity")

df = get_all_opportunities()
if df.empty:
    st.info("No records to update.")
    st.stop()

options = {f"{r['opportunity_id']} — {r['company_name']} | {r['job_title']}": r['opportunity_id']
           for _, r in df.iterrows()}
selected_label = st.selectbox("Select record to update", list(options.keys()))
opp_id = options[selected_label]
record = get_opportunity_by_id(opp_id)

if record is not None:
    with st.form("update_form"):
        col1, col2 = st.columns(2)
        with col1:
            status   = st.selectbox("Status", utils.STATUSES,
                                    index=utils.STATUSES.index(record["status"]) if record["status"] in utils.STATUSES else 0)
            work_mode = st.selectbox("Work Mode", utils.WORK_MODES,
                                     index=utils.WORK_MODES.index(record["work_mode"]) if record["work_mode"] in utils.WORK_MODES else 0)
            salary_min = st.number_input("Salary Min", value=float(record["salary_min"] or 0))
            salary_max = st.number_input("Salary Max", value=float(record["salary_max"] or 0))
        with col2:
            skills   = st.text_area("Required Skills", value=record["required_skills"])
            deadline = st.date_input("Application Deadline",
                                     value=record["application_deadline"] if pd.notna(record["application_deadline"]) else None)
        submitted = st.form_submit_button("Update")
    if submitted:
        try:
            update_opportunity(opp_id, {
                "status": status, "work_mode": work_mode,
                "salary_min": salary_min or None, "salary_max": salary_max or None,
                "required_skills": skills, "application_deadline": deadline,
            })
            st.success("✅ Record updated successfully.")
            st.cache_data.clear()
        except Exception as e:
            st.error(f"Error: {e}")