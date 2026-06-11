import streamlit as st
from app.db import test_connection, get_engine
from sqlalchemy import text

st.title("🏥 Database Health Check")

ok, result = test_connection()
if ok:
    st.success("✅ Connected to PostgreSQL")
    st.code(result)
else:
    st.error(f"❌ Connection failed: {result}")
    st.stop()

engine = get_engine()
with engine.connect() as conn:
    count = conn.execute(text("SELECT COUNT(*) FROM opportunities")).fetchone()[0]
    latest = conn.execute(text("SELECT company_name, job_title, created_at FROM opportunities ORDER BY created_at DESC LIMIT 1")).fetchone()
    cols = conn.execute(text("SELECT column_name, data_type FROM information_schema.columns WHERE table_name='opportunities' ORDER BY ordinal_position")).fetchall()

col1, col2 = st.columns(2)
col1.metric("Total Rows in opportunities", count)
if latest:
    col2.info(f"**Latest record:** {latest[0]} — {latest[1]}  \nAdded: {latest[2]}")

st.subheader("Table Columns")
for col in cols:
    st.text(f"  {col[0]:30s}  {col[1]}")