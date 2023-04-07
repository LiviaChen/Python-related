import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# ---

st.header('streamlit 30 days practice')
with st.expander('reference') :
    st.write('https://30days.streamlit.app/')

# ---

my_bar = st.progress(0)

# ---

st.subheader('conditional statement and also, button control')
st.write('Hello world!')
if st.button('Say hello') :
    st.write('Why hello there')
else :
    st.write('Goodbye')

# ---

st.subheader('this is how simple a pandas dataframe can be write')
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# ---

st.subheader('this is a altair plot object being st.write')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# ----

st.subheader('how to plot a chart speedly with line_chart')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# ---

my_bar.progress(20)

# ---

st.subheader('selectbox and multiselect box')
option = st.selectbox('text here', ('option1', 'option2'))

options = st.multiselect('text here', ['option1', 'option2'], ['option1'])
st.write('you select', options)

# ---

st.subheader('checkbox is here')
icecream = st.checkbox('ice cream')
coffee = st.checkbox('coffee')
if icecream :
    st.write('icecream, are you sure?')
if coffee :
    st.write('coffee? yeah!')

# from streamlit_pandas_profiling import st_profile_report
# import pandas_profiling
# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# pr = df.profile_report()
# st_profile_report(pr)

# ----

st.subheader('this is how math formula is done')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1}
     ''')

# ---

my_bar.progress(60)

# ----

st.subheader('code block is how it is')
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

# st.write(st.secrets['message'])

# ---

st.subheader('file_uploader practice')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')

# st.set_page_config(layout="wide")
# ---

my_bar.progress(100)

# ----
st.subheader('column combine sidebar objecrs practice')
name = st.sidebar.text_input("what's your good name?")
age = st.sidebar.slider('your good age?', 18, 60, 18)
hobbie = st.sidebar.selectbox('your good hobbies', ('eat', 'cool', 'netflix'))
col1, col2, col3 = st.columns(3)

with col1 :
    if name != '' :
        st.write(f'{name}, what a good name!')
    else :
        st.write('please let me know your good name')

with col2 :
    if age != '' :
        st.write(age, 'good age!')  # only number will have special back group while not using format
    else :
        st.write('please let me know your good age')

with col3 :
    if hobbie != '' :
        st.write(f'{hobbie}, good good good!')
    else :
        st.write('please let me know your good hobbie')

# ----
st.balloons()

# ---
st.subheader('form practice')
with st.form('my_form') :
    coffee = st.selectbox('coffee type', ['cold brew', 'home brew'])  
    owncup = st.checkbox('have the own cup?')
    submitted = st.form_submit_button('Submit')  
    if submitted :
        st.markdown(f'''
        You have ordered: 
        - coffee type {coffee} 
        - bring own cup: {owncup}''')
    else :  
        st.write('place your good order')

# ---

st.subheader('retrieve query param')
st.write(st.experimental_get_query_params())
try : 
    if st.experimental_get_query_params()['good'][0] :
        st.write('good, good')  # only works while the url with good=good
except :
    st.write('good?')

# ---

st.subheader('session_state')
st.write(st.session_state)

def f_to_c() :
    st.session_state.c = (st.session_state.f - 32) * 5 / 9
def c_to_f() :
    st.session_state.f = st.session_state.c * 9 / 5 + 32

col1, spacer, col2 = st.columns([2, 1, 2])

with col1 :
    f = st.number_input("F degree", key = 'f', on_change = f_to_c)

with col2 :
    c = st.number_input("C degree", key = 'c', on_change = c_to_f)

st.write(st.session_state)

# ---