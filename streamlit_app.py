import streamlit as st
import datetime

# Access the secrets using st.secrets
cvs_generated = st.secrets["cvs_generated"]
cheatsheets_generated = st.secrets["cheatsheets_generated"]
interviews_conducted = st.secrets["interviews_conducted"]

# Streamlit App
st.title("Dashboard")

# Display Metrics
st.markdown(f"### Number of CVs Generated\n# {cvs_generated}")
st.markdown(f"### Number of Cheatsheets Generated\n# {cheatsheets_generated}")
st.markdown(f"### Number of Interviews Conducted\n# {interviews_conducted}")

# Display Last Updated Date
st.markdown(f"Last updated: {datetime.datetime.now().strftime('%d-%m-%Y')}")

