import streamlit as st
from app.auth import require_admin
from app.queries import insert_opportunity
from app import utils

require_admin()
st.title("➕ Add New Opportunity")

with st.form("add_form"):
    col1, col2 = st.columns(2)
    with col1:
        company_name  = st.text_input("Company Name *")
        job_title     = st.text_input("Job Title *")
        category      = st.selectbox("Category *", utils.CATEGORIES)
        city          = st.text_input("City")
        country       = st.text_input("Country", value="Pakistan")
        work_mode     = st.selectbox("Work Mode", utils.WORK_MODES)
    with col2:
        required_skills   = st.text_area("Required Skills *")
        experience_level  = st.selectbox("Experience Level", utils.EXPERIENCE_LEVELS)
        salary_min        = st.number_input("Salary Min", min_value=0, value=0)
        salary_max        = st.number_input("Salary Max", min_value=0, value=0)
        currency          = st.selectbox("Currency", utils.CURRENCIES)
        application_deadline = st.date_input("Application Deadline")
        status            = st.selectbox("Status", utils.STATUSES)
        source_link       = st.text_input("Source Link")
    
    submitted = st.form_submit_button("Add Opportunity")

if submitted:
    if not company_name or not job_title or not required_skills:
        st.error("Company Name, Job Title, and Required Skills are required.")
    else:
        try:
            insert_opportunity({
                "company_name": company_name, "job_title": job_title,
                "category": category, "city": city, "country": country,
                "work_mode": work_mode, "required_skills": required_skills,
                "salary_min": salary_min or None, "salary_max": salary_max or None,
                "currency": currency, "experience_level": experience_level,
                "application_deadline": application_deadline, "status": status,
                "source_link": source_link,
            })
            st.success(f"✅ Added: {job_title} at {company_name}")
            st.cache_data.clear()
        except Exception as e:
            st.error(f"Error: {e}")