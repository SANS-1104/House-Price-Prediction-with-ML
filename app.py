import streamlit as st
import numpy as np
import pickle
model = pickle.load(open('Model.pkl', 'rb'))


st.title("HOUSE PRICE PREDICTION APP")
st.subheader('Select your Requirements and get an Estimate of House Prices according to California...!!')
st.write('-'*25)

salary_in_rs = st.number_input('Enter Your Salary (in Rs)')
salary_in_dollar = salary_in_rs*0.012

house_age = st.slider('Select Age of House', 1,52)

no_of_rooms = st.selectbox('Select Expected No of Rooms in House',[i for i in range(0,11)])

no_of_bedrooms = st.selectbox('Select Expected No of BedRooms in House',[i for i in range(0,5)])

members = st.number_input('How many members in your House?', format='%i',step=1, min_value=1, max_value=6)

ave_occup = members / no_of_rooms if no_of_rooms > 0 else 0

latitude = 36.778259
longitude = -119.417931
population = 1372.7453488372093


input_data = np.array([[salary_in_dollar, house_age, no_of_rooms, no_of_bedrooms, population, ave_occup, latitude, longitude]])


if st.button('Predict House Price'):
    predicted_price = model.predict(input_data)
    price_in_usd = predicted_price[0]
    price_in_inr = price_in_usd * 83.99

    st.success(f"The estimated house price is: $ {price_in_usd:,.2f}     or      ₹ {price_in_inr:,.2f}")
    st.balloons()
