import streamlit as st
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder
import tensorflow as tf
import pickle
import pandas as pd

model = tf.keras.models.load_model('model.h5')

with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)

with open('onehot_encoder_geo.pkl', 'rb') as file:
    OneHot_Encoder = pickle.load(file)
with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)

##streamlit app
st.title('Customer Churn prediction')


# User input
geography= st.selectbox ('Geography', OneHot_Encoder.categories_[0])
gender = st.selectbox ('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance =st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider ('Tenure', 0, 10)
num_of_products = st.slider ('Number of Products', 1, 4)
has_cr_card= st.selectbox ('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])


input_data = pd.DataFrame({
'CreditScore': [credit_score],
'Gender': [label_encoder_gender.transform([gender])[0]],
'Age': [age],
'Tenure': [tenure],
'Balance': [balance],
'NumOfProducts': [num_of_products],
'HasCrCard': [has_cr_card],
'IsActiveMember': [is_active_member],
'EstimatedSalary': [estimated_salary]
})

geo_encoded = OneHot_Encoder.transform([[geography]]).toarray()
geo_df = pd.DataFrame(geo_encoded,columns=OneHot_Encoder.get_feature_names_out(['Geography']))

input_Data = pd.concat([input_data.reset_index(drop=True),geo_df],axis=1)
imput_Data_scaled = scaler.transform(input_Data)
prediction = model.predict(imput_Data_scaled)
prob = prediction[0][0]
st.write(f'Churn prediction : {prob:.2f}')
if(prob>0.5):
    st.write('the Customer is likey to churn')
else:
    st.write('the customer is not likely to churn')