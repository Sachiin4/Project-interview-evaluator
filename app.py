import streamlit as st
import subprocess

st.title("Project Interview Evaluator")
st.write("Demo using prepared input files.")

if st.button("Run Evaluation"):
    subprocess.run(["python", "main.py"])
    st.success("Evaluation completed. Check final_report.txt")