#  Radio Button

import streamlit as st

#Title and option of radio button
status = st.radio("Select Subject: ", ('English', 'Math'))

#Choice based on condition
if (status == 'English'):
    st.success("English")
else:
    st.success("Math")
