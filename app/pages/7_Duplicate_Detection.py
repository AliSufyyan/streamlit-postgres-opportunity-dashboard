import streamlit as st
from app.queries import get_duplicates
from app.auth import require_admin

require_admin()
st.title("🔎 Duplicate Detection")
st.markdown("Detects opportunities with the same company, job title, and city.")

df = get_duplicates()
if df.empty:
    st.success("✅ No duplicates found.")
else:
    st.warning(f"⚠️ Found {len(df)} potential duplicate record(s).")
    st.dataframe(df, use_container_width=True)
    st.info("Go to the Delete page to remove unwanted duplicates.")