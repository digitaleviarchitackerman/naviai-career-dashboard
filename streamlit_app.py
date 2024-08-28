import streamlit as st
import datetime
import random

# Initialize session state if not present
if 'cvs_generated' not in st.session_state:
    st.session_state.cvs_generated = 3448
if 'cheatsheets_generated' not in st.session_state:
    st.session_state.cheatsheets_generated = 221
if 'interviews_conducted' not in st.session_state:
    st.session_state.interviews_conducted = 512
if 'last_update_date' not in st.session_state:
    st.session_state.last_update_date = datetime.date.today()

# Define the update values for today
today_date = datetime.date.today()

# Function to simulate daily increase
def update_metrics():
    st.session_state.cvs_generated += random.randint(5, 40)  # Random CVs generated today
    st.session_state.cheatsheets_generated += random.randint(0, 10)  # Random Cheatsheets generated today
    st.session_state.interviews_conducted += random.randint(0, 15)  # Random Interviews conducted today
    st.session_state.last_update_date = today_date  # Update the last update date

# Update metrics if the date has changed
if today_date > st.session_state.last_update_date:
    update_metrics()

# Calculate the delta values for display
delta_cvs = random.randint(5, 40)
delta_cheatsheets = random.randint(0, 10)
delta_interviews = random.randint(0, 15)

# Metrics display
st.metric(label="Number of CVs Generated", value=st.session_state.cvs_generated, delta=f"+{delta_cvs} today")
st.metric(label="Number of Cheatsheets Generated", value=st.session_state.cheatsheets_generated, delta=f"+{delta_cheatsheets} today")
st.metric(label="Number of Interviews Conducted", value=st.session_state.interviews_conducted, delta=f"+{delta_interviews} today")

# Additional info
st.text(f"Last updated: {st.session_state.last_update_date}")
