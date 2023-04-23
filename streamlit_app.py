import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import requests

st.set_page_config(layout="wide", page_title="LiviaZC 30days streamlit", page_icon="💐")

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

# st.subheader('code block is how it is')
#st.code("""
#[theme]
#primaryColor="#F39C12"
#backgroundColor="#2E86C1"
#secondaryBackgroundColor="#AED6F1"
#textColor="#FFFFFF"
#font="monospace"
#""")

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
st.subheader('column combine sidebar objects practice')
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

st.subheader('the way to use API')
st.title('Bored API')
selected_type = st.sidebar.selectbox('Select an activity type for API', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1 :
    with st.expander('about this part') :
        st.write('this part suggest things you can do while you are bored based on the cate. you chose, powered by Bored API')
with c2 :
    st.write(suggested_activity)

st.write('suggested activity')
st.info(suggested_activity['activity'])

c3, c4, c5 = st.columns(3)
with c3 :
    st.metric(label = 'number of people required', value = suggested_activity['participants'])
with c4 :
    st.metric(label = 'what type', value = suggested_activity['type'].capitalize())
with c5 :
    st.metric(label = 'link', value = suggested_activity['link'])

# ---
#from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo
#from pathlib import Path
#import json

#with st.sidebar :
#    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=ujVgw7qpZRQ")
#if "data" not in st.session_state:
#    st.session_state.data = Path("data.json").read_text()

#layout = [
#    dashboard.Item("editor", 0, 0, 6, 3),
#    dashboard.Item("chart", 6, 0, 6, 3),
#    dashboard.Item("media", 0, 2, 12, 4),
#]

#with elements("demo") :
#    with dashboard.Grid(layout, draggableHandle=".draggable"):
#        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
#            mui.CardHeader(title="Editor", className="draggable")
#            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
#               editor.Monaco(
#                    defaultValue=st.session_state.data,
#                    language="json",
#                    onChange=lazy(sync("data"))
#                )
#        with mui.CardActions:
#            mui.Button("Apply changes", onClick=sync())
#        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):
#            mui.CardHeader(title="Chart", className="draggable")
#            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
#                nivo.Bump(
#                    data=json.loads(st.session_state.data),
#                   colors={ "scheme": "spectral" },
#                    lineWidth=3,
#                    activeLineWidth=6,
#                    inactiveLineWidth=3,
#                    inactiveOpacity=0.15,
#                    pointSize=10,
#                    activePointSize=16,
#                    inactivePointSize=0,
#                    pointColor={ "theme": "background" },
#                    pointBorderWidth=3,
#                    activePointBorderWidth=3,
#                    pointBorderColor={ "from": "serie.color" },
#                    axisTop={
#                        "tickSize": 5,
#                        "tickPadding": 5,
#                        "tickRotation": 0,
#                        "legend": "",
#                        "legendPosition": "middle",
#                        "legendOffset": -36
#                    },
#                    axisBottom={
#                        "tickSize": 5,
#                        "tickPadding": 5,
#                        "tickRotation": 0,
#                        "legend": "",
#                        "legendPosition": "middle",
#                        "legendOffset": 32
#                    },
#                    axisLeft={
#                        "tickSize": 5,
#                        "tickPadding": 5,
#                        "tickRotation": 0,
#                        "legend": "ranking",
#                        "legendPosition": "middle",
#                        "legendOffset": -40
#                    },
#                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
#                    axisRight=None,
#                )
#        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
#            mui.CardHeader(title="Media Player", className="draggable")
#            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
#                media.Player(url=media_url, width="100%", height="100%", controls=True)

# ---

# from streamlit_shap import st_shap
# import shap
# from sklearn.model_selection import train_test_split
# import xgboost

# @st.cache_data
# def load_data():
#     return shap.datasets.adult()

# @st.cache_data
# def load_model(X, y):
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
#     d_train = xgboost.DMatrix(X_train, label=y_train)
#     d_test = xgboost.DMatrix(X_test, label=y_test)
#     params = {
#         "eta": 0.01,
#         "objective": "binary:logistic",
#         "subsample": 0.5,
#         "base_score": np.mean(y_train),
#         "eval_metric": "logloss",
#         "n_jobs": -1,
#     }
#     model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
#     return model

# st.title("`streamlit-shap` displaying SHAP plots")

# st.subheader('Input data')
# X,y = load_data()
# X_display,y_display = shap.datasets.adult(display=True)

# with st.expander('About the data'):
#     st.write('Adult census data is used as the example dataset.')
# with st.expander('X'):
#     st.dataframe(X)
# with st.expander('y'):
#     st.dataframe(y)
# # with st.expander('X write'):  # the effect is same as above
# #     st.write(X)
# # with st.expander('y write'):
# #     st.write(y)

# st.subheader('SHAP output')

# # train XGBoost model
# model = load_model(X, y)

# # compute SHAP values
# explainer = shap.Explainer(model, X)
# shap_values = explainer(X)

# with st.expander('Waterfall plot'):
#     st_shap(shap.plots.waterfall(shap_values[0]), height=300)

# # with st.expander('Beeswarm plot'):
# #     st_shap(shap.plots.beeswarm(shap_values), height=300)

# explainer = shap.TreeExplainer(model)
# shap_values = explainer.shap_values(X)

# with st.expander('Force plot'):
#     st.subheader('First 1')
#     st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
#     st.subheader('First 1000')
#     st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)

# ---
# hugging face
# code can refer to https://github.com/charlywargnier/zero-shot-classifier/blob/main/streamlit_app.py

# from streamlit_option_menu import option_menu

# with st.sidebar:
#     selected = option_menu(
#         "",
#         ["Demo", "Unlocked Mode"],
#         icons=["bi-joystick", "bi-key-fill"],
#         menu_icon="",
#         default_index=0,
#     )

# API_KEY = st.secrets["hugface"]
# API_URL = (
#     "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
# )
# headers = {"Authorization": f"Bearer {API_KEY}"}

# from streamlit_tags import st_tags, st_tags_sidebar
# label_widget = st_tags(
#     label="",
#     text="Add labels - 3 max",
#     value=["Transactional", "Informational"],
#     suggestions=[
#         "Navigational",
#         "Transactional",
#         "Informational",
#         "Positive",
#         "Negative",
#         "Neutral",
#     ],
#     maxtags=3,
# )
# MAX_LINES = 5

# sample = """
# I want to buy something in this store
# How to ask a question about a product
# Request a refund through the Google Play store
# I have a broken screen, what should I do?
# Can I have the link to the product?
# """

# text = st.text_area(
#     "Enter keyphrase to classify",
#     sample,
#     height=200,
#     key="2",
#     help="At least two keyphrases for the classifier to work, one per line, "
#     + str(MAX_LINES)
#     + " keyphrases max as part of the demo",
# )
# lines = text.split("\n")  # A list of lines
# lines = list(filter(None, set(lines)))

# if len(lines) > MAX_LINES:
#     st.info(
#         f"🚨 Only the first "
#         + str(MAX_LINES)
#         + " keyprases will be reviewed. Unlock that limit by switching to 'Unlocked Mode'"
#     )

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     # Unhash to check status codes from the API response
#     # st.write(response.status_code)
#     return response.json()    

# listToAppend = []
# for row in lines:
#     output2 = query(
#                 {
#                     "inputs": row,
#                     "parameters": {"candidate_labels": label_widget},
#                     "options": {"wait_for_model": True},
#                 }
#             )
#     listToAppend.append(output2)

# df = pd.DataFrame.from_dict(listToAppend)

# from st_aggrid import AgGrid
# from st_aggrid.grid_options_builder import GridOptionsBuilder
# from st_aggrid.shared import JsCode
# from st_aggrid import GridUpdateMode, DataReturnMode

# gb = GridOptionsBuilder.from_dataframe(df)
# gb.configure_default_column(
#     enablePivot=True, enableValue=True, enableRowGroup=True
# )
# gb.configure_selection(selection_mode="multiple", use_checkbox=True)
# gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
# gridOptions = gb.build()

# response = AgGrid(
#     df,
#     gridOptions=gridOptions,
#     enable_enterprise_modules=True,
#     update_mode=GridUpdateMode.MODEL_CHANGED,
#     data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
#     height=400,
#     fit_columns_on_grid_load=False,
#     configure_side_bar=True,
# )
    

# @st.cache_data
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode("utf-8")

# csv = convert_df(df)

# st.caption("")

# st.download_button(
#     label="Download results as CSV",
#     data=csv,
#     file_name="results.csv",
#     mime="text/csv",
#)

# end of hugging face
# ---

# youtube thumbnail
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://www.youtube.com/watch?v=ujVgw7qpZRQ')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')

# done with 30 days challenge, yeahhhh
