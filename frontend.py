import streamlit as st 
import requests 
st.title("Placement Prediction") 
cgpa=st.slider("CGPA",0.0,10.0,7.0) 
aptitude=st.slider("Aptitude",0,100,70) 
communication=st.slider("Communication",1,10,5) 
projects=st.slider("Projects",0,5,2)
if st.button("Predict"):
    url = "https://placement-prediction-zrjj.onrender.com/predict"
    data = {
        "cgpa": cgpa,
        "aptitude": aptitude,
        "communication": communication,
        "projects": projects
    }

    try:
        response = requests.post(url, json=data)

        st.write("Status Code:", response.status_code)
        st.write("Response Text:", response.text)

        result = response.json()

        if result['prediction'] == 1:
            st.success("You will be Placed!!")
        else:
            st.error("Not likely to be Placed")

    except Exception as e:
        st.error(f"Error: {e}")
