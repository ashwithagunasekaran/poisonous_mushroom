import streamlit as st
import pandas as pd
st.title('check if the mushroom is edible or not')
with st.form(key='mushroom_form'):
 cap_diameter = st.number_input("Enter cap-diameter")
 cap_shape = st.number_input("Enter cap-shape")
 gill_attachment = st.number_input("Enter gill-attachment ")
 gill_color = st.number_input("Enter gill-color")
 stem_height = st.number_input("Enter stem-height")
 stem_width= st.number_input("Enter stem-width")
 stem_color= st.number_input("Enter stem-color")
 season = st.number_input("Enter season")

 submit_button = st.form_submit_button(label='Submit')
test = pd.DataFrame({'cap-diameter':cap_diameter,'cap-shape':cap_shape,
                     'gill-attachment':gill_attachment,
                     'gill-color':gill_color ,
                     'stem-height':stem_height,
                     'stem-width':stem_width,
                     'stem-color':stem_color,'season':season},index=[0])

import pickle
model = pickle.load(open("C:\\Users\\Dell\Downloads\\mushroom_cleaned (3).pkl",'rb'))
if submit_button:
     prediction=model.predict(test)
     
     if prediction[0] == 0:
        st.write("This mushroom is edible!")
     else:
        st.write("This mushroom is poisonous!")
