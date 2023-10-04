import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Web deployment of medical Diagnostic App🏥')
st.subheader('IS the person diabetic')

df = pd.read_csv('diabetes.csv')
if st.sidebar.checkbox('View Data',False):
    st.write(df.head())
if st.sidebar.checkbox('View Distributions',False):
    df.hist()
    plt.tight_layout()
    st.pyplot()
    

    
# step 1  Load the pickle file
model = open('rfc.pickle', 'rb')
clf = pickle.load(model)
model.close()

# step 2 Get the front-end user input 
pregs=st.number_input('Pregnancies',0,17,0),
glucose=st.number_input('Glucose',44,199,44),
BP=st.number_input( 'BloodPressure',24,122,24),
Skin=st.number_input('SkinThickness',7,99,7),
Insulin=st.number_input('Insulin',14,846,14),
BMI=st.number_input('BMI',18,67,18), 
dpf=st.number_input('DiabetesPedigreeFunction',0.05,2.50,0.05), 
Age=st.number_input('Age',21,85,21)
