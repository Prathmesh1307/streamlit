# Importing the necessary Python modules.
import numpy as np
import pandas as pd
import streamlit as st 
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_log_error,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Define the 'prediction()' function.
@st.cache()
def prediction(car_df,carwidth,enginesize,horsepower,drivewheel_fwd,car_company_buick):
  X=car_df.iloc[:,:-1]
  y=car_df["price"]
  X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
  lr_clf=LinearRegression()
  lr_clf.fit(X_train,y_train)
  accuracy=lr_clf.score(X_train,y_train)
  price=lr_clf.predict([[carwidth,enginesize,horsepower,drivewheel_fwd,car_company_buick]])
  price=price[0]
  y_test_pred=lr_clf.predict(X_test)
  test_r2_score=r2_score(y_test,y_test_pred)
  mae=mean_absolute_error(y_test,y_test_pred)
  msle=mean_squared_log_error(y_test,y_test_pred)
  mse=mean_squared_error(y_test,y_test_pred)
  rmse=np.sqrt(mse)
  return price ,accuracy,test_r2_score,mae,msle,mse,rmse
def app(car_df):
  st.markdown("<p style='color:blue;font-size:25px'> This app uses <b>Linear regression</b> to predict the price of a car based on your inputs. </p>",unsafe_allow_html = True)
  st.subheader("Select values ")
  cw=st.slider("Carwidth",float(car_df["carwidth"].min()),float(car_df["carwidth"].max()))
  es=cw=st.slider("Enginesize",int(car_df["enginesize"].min()),int(car_df["enginesize"].max()))
  hp=cw=st.slider("Horsepower",int(car_df["horsepower"].min()),int(car_df["horsepower"].max()))
  dw=st.radio("Is a forward drivewheel car ?",("Yes","No"))
  if dw=="No":
    dw=0
  else:
    dw=1
  cb=st.radio("Is the car manufactured by buick ?",("Yes","No"))
  if cb=="No":
    cb=0
  else:
    cb=1
  if st.button("Predict"):
    st.subheader("Prediction Results")
    price,accuracy,test_r2_score,mae,msle,mse,rmse=prediction(car_df,cw,es,hp,dw,cb)
    st.success(f"The predicted price of the car : {price}")
    st.info(f"Accuracy of the model : {accuracy:.3f}")
    st.info(f"R2 score of the model : {test_r2_score:.3f}")
    st.info(f"Mean absolute error of the model : {mae:.3f}")
    st.info(f"Mean squared log error of the model : {msle:.3f}")
    st.info(f"Mean squared error of the model : {mse:.3f}")
    st.info(f"Root mean squared error of the model : {rmse:.3f}")