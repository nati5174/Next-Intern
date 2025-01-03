import streamlit as st

st.image('david-libeert-oWhdFlqaNwI-unsplash.jpg', width=400)

st.title("Next-Intern")

role  = st.sidebar.selectbox("Pick Something", ("Home","Find Jobs", "Resume Creatr", "Cover letter creatr"))


if role == "Home":
    st.write("Next Intern is a web-app which helps students in getting their next internship. The app provides, users with a oppurtunity to find internships based on location and desired position, a resume generator based on job your applying to, and a cover letter generator based off of the job your applying to.")
elif role == "Find Jobs":
    st.write("Will provide you with urls to jobs")
elif role == "Resume Creatr":
    st.write("Will build you a resume")

elif role == "Cover letter creatr":
    st.write("Will build you a Cover letter")    

