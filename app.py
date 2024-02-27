import streamlit as st
import pandas as pd
import pickle



def user_input():
    # Divider
    st.markdown('<div style="text-align: laeft;"><h2>Dataframe</h2></div>', unsafe_allow_html=True)

    df = pd.read_csv('P1G5_Set_1_Muhammad_Irsyad.csv')

    st.dataframe(df)

    # Divider
    st.markdown('<div style="text-align: left;"><h2>Input Data</h2></div>', unsafe_allow_html=True)


    limit_balance = st.number_input("Enter Limit Balance", value=200000.0)
    sex = st.number_input("Enter Sex (1.0 for male, 2.0 for female)", value=1.0)
    education_level = st.number_input("Enter Education Level", value=4.0)
    marital_status = st.number_input("Enter Marital Status", value=1.0)
    age = st.number_input("Enter Age", value=49.0)
    pay_0 = st.number_input("Enter Pay_0", value=0.0)
    pay_2 = st.number_input("Enter Pay_2", value=0.0)
    pay_3 = st.number_input("Enter Pay_3", value=0.0)
    pay_4 = st.number_input("Enter Pay_4", value=0.0)
    pay_5 = st.number_input("Enter Pay_5", value=0.0)
    pay_6 = st.number_input("Enter Pay_6", value=0.0)
    bill_amt_1 = st.number_input("Enter Bill_amt_1", value=49221.0)
    bill_amt_2 = st.number_input("Enter Bill_amt_2", value=49599.0)
    bill_amt_3 = st.number_input("Enter Bill_amt_3", value=50942.0)
    bill_amt_4 = st.number_input("Enter Bill_amt_4", value=50146.0)
    bill_amt_5 = st.number_input("Enter Bill_amt_5", value=50235.0)
    bill_amt_6 = st.number_input("Enter Bill_amt_6", value=48984.0)
    pay_amt_1 = st.number_input("Enter Pay_amt_1", value=1689.0)
    pay_amt_2 = st.number_input("Enter Pay_amt_2", value=2164.0)
    pay_amt_3 = st.number_input("Enter Pay_amt_3", value=2500.0)
    pay_amt_4 = st.number_input("Enter Pay_amt_4", value=3480.0)
    pay_amt_5 = st.number_input("Enter Pay_amt_5", value=2500.0)
    pay_amt_6 = st.number_input("Enter Pay_amt_6", value=3000.0)

    data = {
        'limit_balance': limit_balance,
        'sex': sex,
        'education_level': education_level,
        'marital_status': marital_status,
        'age': age,
        'pay_0': pay_0,
        'pay_2': pay_2,
        'pay_3': pay_3,
        'pay_4': pay_4,
        'pay_5': pay_5,
        'pay_6': pay_6,
        'bill_amt_1': bill_amt_1,
        'bill_amt_2': bill_amt_2,
        'bill_amt_3': bill_amt_3,
        'bill_amt_4': bill_amt_4,
        'bill_amt_5': bill_amt_5,
        'bill_amt_6': bill_amt_6,
        'pay_amt_1': pay_amt_1,
        'pay_amt_2': pay_amt_2,
        'pay_amt_3': pay_amt_3,
        'pay_amt_4': pay_amt_4,
        'pay_amt_5': pay_amt_5,
        'pay_amt_6': pay_amt_6
    }

    features = pd.DataFrame(data, index=[0])
    return features

input = user_input()

st.subheader('User Input')
st.write(input)

with open("model.pkl", 'rb') as model:
  model = pickle.load(model)

prediction = model.predict(input)

if prediction == 1:
    prediction_text = 'will pay next month'
else:
    prediction_text = 'will not pay next month'

st.subheader('Input Results')

st.write(f'Based on user input, the customer {prediction_text}')

  



