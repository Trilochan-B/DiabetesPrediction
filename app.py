import streamlit as st
import pandas as pd
import pickle
# from tensorflow.keras.models import load_model

# model = load_model('diabetes_model.h5')
# with open('model.pkl','rb') as f:
#     model = pickle.load(f)
with open('gender_encoder.pkl','rb') as f:
    gender_encoder = pickle.load(f)
with open('smoking_encoder.pkl','rb') as f:
    smoke_encoder = pickle.load(f)
with open('scaler.pkl','rb') as f:
    scaler=pickle.load(f)

st.title('Diabetes Prediction')
gender = st.selectbox(label='Gender',options=gender_encoder.classes_)
age = st.slider('Age',18,99)

hypertension = st.selectbox(label='Hypertension', options=['Yes','No'])
if hypertension == 'Yes':
    hypertension = 1
else:
    hypertension = 0

heart = st.selectbox(label='Heart Disease', options=['Yes','No'])
if heart == 'Yes':
    heart = 1
else:
    heart = 0

smoking = st.selectbox(label='Smoking History',options=['No Info','never','former','current','not current','ever'])

bmi = st.number_input('BMI level',10,100)

h1 = st.number_input('HbA1c level',3,10)


glucose = int(st.number_input('Blood Glucose level',70,320))

but = st.button('Submit')
if but == True:
    input_data = {
    'gender' : gender,
    'age': age,
    'hypertension' : hypertension,
    'heart_disease' : heart,
    'smoking_history' : smoking,
    'bmi' : bmi,
    'HbA1c_level' : h1,
    'blood_glucose_level' : glucose
    }
    input_df = pd.DataFrame([input_data])
    input_df['gender'] = gender_encoder.transform(input_df['gender'])
    smoke_data = smoke_encoder.transform([input_df['smoking_history']])
    smoking_df = pd.DataFrame(smoke_data.toarray(), columns=smoke_encoder.get_feature_names_out(['smoking_history']))
    data = pd.concat([input_df.drop('smoking_history', axis=1), smoking_df], axis=1)
    input_scaled = scaler.transform(data)
    # score = model.predict(input_scaled)[0][0]
    # if score > 0.5:
    #     st.write('There is diabetes in your body.')
    # else:
    #     st.write('There is no diabetes in your body.')





