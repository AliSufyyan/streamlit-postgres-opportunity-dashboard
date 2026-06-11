import streamlit as st
import plotly.express as px
from app.queries import get_all_opportunities

st.title("📊 Analytics Dashboard")
df = get_all_opportunities()

if df.empty:
    st.info("No data available.")
    st.stop()

# ── KPIs ─────────────────────────────────────────────────────────────────────
k1,k2,k3,k4,k5,k6 = st.columns(6)
k1.metric("Total Opportunities",  len(df))
k2.metric("Open",                 len(df[df["status"] == "Open"]))
k3.metric("Companies",            df["company_name"].nunique())
k4.metric("Cities",               df["city"].nunique())
k5.metric("Remote Roles",         len(df[df["work_mode"] == "Remote"]))
k6.metric("Avg Min Salary (PKR)", f"{df['salary_min'].mean():,.0f}" if df["salary_min"].notna().any() else "N/A")

st.divider()

tab1, tab2, tab3 = st.tabs(["By Category", "By Work Mode & Status", "Salary Analysis"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df["category"].value_counts().reset_index(),
                     x="category", y="count", title="Opportunities by Category",
                     color="category")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.pie(df, names="category", title="Category Share")
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig3 = px.bar(df["work_mode"].value_counts().reset_index(),
                      x="work_mode", y="count", title="By Work Mode", color="work_mode")
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        fig4 = px.bar(df["status"].value_counts().reset_index(),
                      x="status", y="count", title="By Status", color="status")
        st.plotly_chart(fig4, use_container_width=True)

with tab3:
    salary_df = df.dropna(subset=["salary_min", "salary_max"])
    if not salary_df.empty:
        fig5 = px.box(salary_df, x="category", y="salary_min",
                      title="Salary Min Distribution by Category", color="category")
        st.plotly_chart(fig5, use_container_width=True)
        
        fig6 = px.scatter(salary_df, x="salary_min", y="salary_max",
                          color="category", size="salary_max",
                          hover_data=["company_name","job_title"],
                          title="Salary Range by Opportunity")
        st.plotly_chart(fig6, use_container_width=True)
    else:
        st.info("No salary data available for analysis.")