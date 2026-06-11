import streamlit as st
from app.auth import require_admin
from app.queries import get_all_opportunities, get_opportunity_by_id, delete_opportunity

require_admin()
st.title("🗑️ Delete Opportunity")

df = get_all_opportunities()
if df.empty:
    st.info("No records to delete.")
    st.stop()

options = {f"{r['opportunity_id']} — {r['company_name']} | {r['job_title']}": r['opportunity_id']
           for _, r in df.iterrows()}
selected_label = st.selectbox("Select record to delete", list(options.keys()))
opp_id = options[selected_label]
record = get_opportunity_by_id(opp_id)

if record is not None:
    st.warning("⚠️ You are about to delete the following record:")
    st.json({k: str(v) for k, v in record.items()})
    confirm = st.checkbox("I confirm I want to permanently delete this record.")
    if st.button("🗑️ Delete", disabled=not confirm):
        try:
            delete_opportunity(opp_id)
            st.success("✅ Record deleted.")
            st.cache_data.clear()
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")