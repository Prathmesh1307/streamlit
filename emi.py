import streamlit as st
def calculate_emi(p,n,r):
  emi=p*(r/100)*(((1+(r/100))**n)/(((1+(r/100))**n)-1))
  st.write(f"Emi : {emi:.3f}")
st.title("EMI Calculator App")  
principal = st.slider("Principal Loan Amount", 1000.0,1000000.0)
tenure= st.slider("Loan period (in years)",1.0,30.0)
roi= st.slider("Rate of Interest (in % per annum)", 1.0, 15.0)
n=tenure*12.0
r=roi/12.0
if st.button("Calculate"):
	calculate_emi(principal,n,r)
