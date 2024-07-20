import streamlit as st

st.set_page_config(page_title='GenAI powered educator for all ages', page_icon="🔥",
                   layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title("GenAI powered creative approach to create stories for younger kids")
st.sidebar.title("Fill in the information below")

age = st.sidebar.text_input("Fill in your age", value = "")

topic = st.sidebar.selectbox("Pick your desired topic", ('Biology', 'Physics', 'Biology', "Maths"))  

question = st.sidebar.text_input("Write your question", value = "")

if st.sidebar.button("Generate New Story"):
    from tts import *
    print("Going into image now")
    print(generated_story)
    from image import *

else:
    st.write("Click the button to generate the story.")