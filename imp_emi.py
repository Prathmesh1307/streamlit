import streamlit as st
def calculate_emi(p,n,r):
  emi=p*(r/100)*(((1+(r/100))**n)/(((1+(r/100))**n)-1))
  st.write(f"Emi : {emi:.3f}")
def calculate_outstanding_balance(p,n,r,m):
  balance=(p*((1+(r/100))**n)-((1+(r/100))**m))/(((1+(r/100))**n)-1)
  st.write(f"Outstanding Loan Balance : {balance:.3f}")
st.title("Improvised EMI Calculator App")  
principal = st.slider("Principal Loan Amount", 1000,1000000)
tenure= st.slider("Loan period (in years)",1.0,30.0)
roi= st.slider("Rate of Interest (in % per annum)", 1.0, 15.0)
m= st.slider("Period after which the Outstanding Loan Balance is calculated (in months)", 1.0, tenure*12.0 )
n=tenure*12.0
r=roi/12.0
if st.button("Calculate Emi"):
	calculate_emi(principal,n,r)
if st.button("Calculate Outstanding Loan Balance"):
	calculate_outstanding_balance(principal,n,r,m)