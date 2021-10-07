#  Radio Button

import streamlit as st

#Title and option of radio button
status = st.radio("Select Subject: ", ('English', 'Math'))

#Choice based on condition
if (status == 'Science'):
    st.success("Science")
else:
    st.success("Math")
