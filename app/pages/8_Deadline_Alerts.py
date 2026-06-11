import streamlit as st
from app.queries import get_deadline_alerts, get_expired_opportunities

st.title("⏰ Deadline Alerts")

tab1, tab2 = st.tabs(["Closing Within 7 Days", "Expired Opportunities"])

with tab1:
    df = get_deadline_alerts()
    if df.empty:
        st.success("✅ No opportunities closing within 7 days.")
    else:
        st.warning(f"⚠️ {len(df)} opportunity/ies closing soon!")
        for _, row in df.iterrows():
            days = int(row["days_left"])
            color = "🔴" if days <= 2 else "🟡"
            st.markdown(f"{color} **{row['job_title']}** at {row['company_name']} — {days} day(s) left (Deadline: {row['application_deadline']})")

with tab2:
    df2 = get_expired_opportunities()
    if df2.empty:
        st.success("✅ No expired opportunities that need updating.")
    else:
        st.warning(f"⚠️ {len(df2)} record(s) may need status updated to 'Expired'.")
        st.dataframe(df2, use_container_width=True)