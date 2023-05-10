import streamlit as st
import time
import os
import csv
import pandas as pd
from Inferencing import inferencing
from test_url import format_url

st.set_page_config(page_title="Detect DGA", page_icon="🐞", layout="centered")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title(":cop: Detect and Evaluate Domain Generation Algorithms (DGA) ")

header = ['URL','Data','Comment','STATUS', 'DGA_Class']
save_file = r'data2.csv'
if not os.path.exists(save_file):
    with open(save_file, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

# sidebar
st.sidebar.markdown("# Detect and Evaluate Domain Generation Algorithms")
st.sidebar.markdown("## Deep Learning Approach")
st.sidebar.write("MSc Cybersecurity - Master Project")
st.sidebar.write("University of the West of England")
st.sidebar.write("## [WIYASINGHE UDESH](https://github.com/ukmihiran)")
form = st.form(key="annotation")

with form:
    url = st.text_input("Enter URL :")
    comment = st.text_area("Comment :")
    date = st.date_input("Date :")
    submitted = st.form_submit_button(label="Submit")

st.markdown("""---""")
b1, b2 = st.columns(2)
with b1:
    b1 = st.metric("Binary Prediction", "No Prediction Yet")
with b2:
    b2 = st.metric("Class Prediction", "No Prediction Yet")
st.markdown("""---""")

sh = st.subheader('Previous Records :page_facing_up:')

data_file = pd.read_csv(save_file)
data_file = data_file.tail(11)
dataframe = st.dataframe(data_file, use_container_width=True)
expander = st.expander("See all records")

if submitted:
    # st.snow()
    # st.balloons()

    sh.empty()
    dataframe.empty()
    b1.empty()
    b2.empty()

    if len(url) == 0:
        status = st.warning('Fill the URL and continue :heavy_exclamation_mark:')
        sh = st.subheader('Previous Records :page_facing_up:')

    else:
        # # st.snow()
        # with st.spinner('Wait for it...'):
        url = format_url(url)
        print(url)
        predictions = inferencing(url)
            # time.sleep(0.5)

        binary_pred_arr = predictions[0]
        class_pred_arr = predictions[1]
        binary_pred = binary_pred_arr[0]
        if binary_pred== "Benign":
            b1.metric("Binary Prediction", binary_pred)
            b2.metric("", "")
        else:
            b1.metric("Binary Prediction", binary_pred)
            b2.metric("Class Prediction", class_pred_arr[0])


        status = st.success("Thanks! Your URL was recorded.")
        sh = st.subheader('Previous Records :page_facing_up:')


        data_entered = [url, date, comment, binary_pred, class_pred_arr[0]]
        with open(save_file, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data_entered)

    data_file = pd.read_csv(save_file)
    data_file = data_file.tail(11)
    dataframe = st.dataframe(data_file, use_container_width = True)







