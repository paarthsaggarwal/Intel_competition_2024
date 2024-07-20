import re, os
from dotenv import find_dotenv, load_dotenv # importing dotenv to acquire the path to the API keys in the .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
from openai import AzureOpenAI 
import streamlit as st
from pathlib import Path
from random import randint
import streamlit as st
# from main import question
# from main import age_topic_question
# from main import line

# print(question)

base_folder = Path(__file__).parent.resolve()

max_tokens = 100
max_tokens_title = 20
temperature = 0.8


client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    
deployment_name='intelopenai' #This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment. 
api_key_1 = os.getenv("AZURE_OPENAI_KEY")

# name = "Tom" 
# character = "king"
# genre = "mystery"
# setting = "forest"
# plot = "Bob and Jenny become friends"

seed_text = randint(1, 10000000000000000000)

# st.set_page_config(page_title='GenAI powered educator for all ages', page_icon="🔥",
#                    layout="wide", initial_sidebar_state="auto", menu_items=None)
# st.title("GenAI powered creative approach to create stories for younger kids")
# st.sidebar.title("Fill in the information below")

# age = 10
# topic = "biology"
# question = "What is a cell"

# age = st.sidebar.text_input("Fill in your age", value = "")

# topic = st.sidebar.selectbox("Pick your desired topic", ('Biology', 'Physics', 'Biology', "Maths"))  

# question = st.sidebar.text_input("Write your question", value = "")

# def story(fact):
#     message = f'''Embrace your inner educator and craft 3 sentences worth of information about {fact}.  
#                 Your educational canvas is strictly limited to the {fact}.                
#                 Develop a well-structured narrative, clear beginning, an informative middle, 
#                 and a firm conclusion which makes sense. The conclusion has to be the highest priority 
#                 and it MUST END so that it makes sense to the average Instagram viewers. 
#                The content would be used to create a reel for Instagram and make 
#                sure there is no abusive and harmful language.  '''
    
#     return message

def story(question, topic, age, language):
    message = f'''You are an experienced {topic} tutor who teaches in {language} has tutored thousands of teens all over the country 
                    and therefore you have a lot of experience. You are asked a question by one of your students.
                    Answer the question asked by the student in a sensible, informative way as if they had a skill level of {age}.
                    Make sure the answer is clear. The question is {question}. Write the answer in {language}. 
                    '''
    
    return message

def title_generation(generated_story):
    title_with_quotations = f'''Read the {generated_story} and generate a concise title. '''
    return title_with_quotations

# age_topic_question()

# question = 0

with open('question.txt', 'r') as file:
    # Read the entire file content
    content_1 = file.read()

with open('topic.txt', 'r') as file:
    # Read the entire file content
    content_2 = file.read()

with open('age.txt', 'r') as file:
    # Read the entire file content
    content_3 = file.read()

with open('language.txt', 'r') as file:
    # Read the entire file content
    content_4 = file.read()

# Print the content
print(content_1)

question = content_1
topic = content_2
age = content_3
language = content_4

# language = 'German'

raw_story = story(question, topic, age, language)
        
response = client.chat.completions.create(
model=deployment_name, # model = "deployment_name".
messages=[
    {"role": "system", "content": "You are a prominent educator and tutor."},
    {"role": "user", "content": raw_story},
],
# seed=seed_text,
temperature=temperature,
max_tokens=max_tokens
)
# raw_html = generate_story(name, character, genre, setting, plot)
generated_story = response.choices[0].message.content

# #Generating title for story
# raw_title = title_generation(generated_story)
# response_title = client.chat.completions.create(
# model=deployment_name, # model = "deployment_name".
# messages=[
#     {"role": "system", "content": "You are someone who is good at generating titles"},
#     {"role": "user", "content": raw_title},
# ],
# temperature=temperature,
# max_tokens=max_tokens_title
# )
# # raw_html = generate_story(name, character, genre, setting, plot)
# title_with_quotations = response_title.choices[0].message.content
# title_without_quotations = re.sub(r'"', '', title_with_quotations)


# with open("generated_text.txt", "w") as file:
#     file.write(generated_text.strip())

# st.subheader("The text for the answer is given below")
st.write(generated_story)

with open("generated_text.txt", "w") as file:
    file.write(generated_story.strip())

# with open("generated_title.txt", "w") as file:
#     file.write(title_without_quotations.strip())

# st.subheader(title_without_quotations)
# st.write(generated_story)