# from completion import *
import streamlit as st
# from image_title import *
import urllib.request
from pathlib import Path
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# import moviepy
import re
import os
# from instapy_clis import client

base_folder = Path(__file__).parent.resolve()

with open('question.txt', 'w') as clear_file:
    clear_file.truncate(0)

with open('topic.txt', 'w') as clear_file:
    clear_file.truncate(0)

with open('age.txt', 'w') as clear_file:
    clear_file.truncate(0)

with open('language.txt', 'w') as clear_file:
    clear_file.truncate(0)

# with open('style.txt', 'w') as clear_file:
#     clear_file.truncate(0)

for filename in os.listdir('images'):
    if os.path.isfile(os.path.join('images', filename)):
        os.remove(os.path.join('images', filename))

for filename in os.listdir('audio'):
    if os.path.isfile(os.path.join('audio', filename)):
        os.remove(os.path.join('audio', filename))

for filename in os.listdir('videos'):
    if os.path.isfile(os.path.join('videos', filename)):
        os.remove(os.path.join('videos', filename))


st.set_page_config(page_title='GenAI powered educator for kids', page_icon="🔥",
                layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title("NavigateNinja - personalized learning and accessible education")

st.sidebar.title("Fill in the information below")

age = st.sidebar.selectbox("Enter your expertise on the subject", ('Novice', 'Intermediate', 'Advanced'))

topic = st.sidebar.selectbox("Pick your desired topic", ('Biology', 'Physics', 'Chemistry', "Maths", "Economics", "Geography", "History"))  

language = st.sidebar.selectbox("Choose your language", ("English", "German", "French", "Spanish", "Italian"))  

# style = st.sidebar.selectbox("Choose your style", ("animated", "fantasy", "abstract"))

question = st.sidebar.text_input("Ask your question", value = "") 


with open("question.txt", "w") as file:
    file.write(question)

with open("topic.txt", "w") as file:
    file.write(topic)

with open("age.txt", "w") as file:
    file.write(age)

with open("language.txt", "w") as file:
    file.write(language)

# with open("style.txt", "w") as file:
#     file.write(style)

# age = 0
# topic = 0
# question = 0

if st.sidebar.button("Ask NavigateNinja"):
    from tts import *
    print("Going into image now")
    print(generated_story)
    from image import *






# username = 'USERNAME'
# password = 'PASSWORD'
# video = 'docs/video-sample-upload.mp4'
# text = 'This will be the caption of your video.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

# with client(username, password) as cli:
#     cli.upload(video, text)

# Open the file in read mode

        # Increment the line count for each line encountered
        

# Setting te layout of the page using streamlit



# from completion import *

# options = ["Bella", "Arnold", "Elli", "Josh"]
# voice = st.sidebar.selectbox("Select a voice to narrate the story:", options)


# Using an if statement to detect whether user presses the "Generate Mew Story" button
# if st.sidebar.button("Generate New Story"):
    # from text_generation import *
    # raw_story = story(name, character, genre, setting, plot)
    
    # response = client.chat.completions.create(
    # model=deployment_name, # model = "deployment_name".
    # messages=[
    #     {"role": "system", "content": "You are a seasoned storyteller"},
    #     {"role": "user", "content": raw_story},
    # ],
    # seed=1,
    # temperature=temperature,
    # max_tokens=max_tokens
    # )
    # # raw_html = generate_story(name, character, genre, setting, plot)
    # generated_story = response.choices[0].message.content

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


    # # with open("generated_text.txt", "w") as file:
    # #     file.write(generated_text.strip())

    # with open("generated_text.txt", "w") as file:
    #     file.write(generated_story.strip())

    # with open("generated_title.txt", "w") as file:
    #     file.write(title_without_quotations.strip())

    # st.subheader(title_without_quotations)
    # st.write(generated_story)
    # print(generated_title)

#     audio = generate_audio(generated_text, voice) # generating audio
    
#     st.subheader("The audio which narrates the story is shown below")
#     st.audio(audio, format='audio/mp3')
    
    # client = AzureOpenAI(
    #     api_version=os.getenv("AZURE_IMAGE_VERSION"),  
    #     api_key=os.environ["AZURE_IMAGE_KEY"],  
    #     azure_endpoint=os.environ['AZURE_IMAGE_ENDPOINT']
    # )
    # i = 1
    # a = i+1
    # paragraphs = re.split(r"[.]", generated_story)
    # print("=================")
    # print(paragraphs)

# st.image(image_files)

    # st.subheader("The audio which narrates the story is shown below")
    # st.audio(speech_synthesis_result)
    
    # result_title_images = client_1.images.generate(
    #     model="dalle3", # the name of your DALL-E 3 deployment
    #     prompt=title_without_quotations,
    #     n=1
    #     )
    
    # json_response = json.loads(result_title_images.model_dump_json())
    # image_dir = os.path.join(os.curdir, 'images')
    # image_path = os.path.join(image_dir, f"generated_image_title.png")
    # image_url = json_response["data"][0]["url"]  # extract image URL from response
    # generated_image_title = requests.get(image_url).content  # download the image

#     with open(image_path, "wb") as image_file:
#         image_file.write(generated_image_title)

#     image_files_title = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
#     # st.image(image_files_title)

# #Using Pillow#################################################################
#     img = Image.open(f"images/generated_image_title.png")

#     # Call draw Method to add 2D graphics in an image
#     I1 = ImageDraw.Draw(img)

#     # Custom font style and font size
#     myFont = ImageFont.truetype('Arial.ttf', 65)

#     # Add Text to an image
#     I1.text((10, 10), title_without_quotations, font=myFont, fill =(255, 0, 0), align='center')

#     # Display edited image
#     img.show()

#     # Save the edited image
#     final_title_image = img.save(f"images/final_title_image.png")
#     st.image(final_title_image)

    #################End of using Pillow - might have to delete ###############################################################

    
    # st.subheader("The images for the story is shown below")
    # for para in paragraphs[:-1]:
    #     result_1 = client_1.images.generate(
    #     model="dalle3", # the name of your DALL-E 3 deployment
    #     prompt=para.strip(),
    #     n=1
    #     )
    #     json_response = json.loads(result_1.model_dump_json())
    #     image_dir = os.path.join(os.curdir, 'images')
    #     image_path = os.path.join(image_dir, f"generated_image{i}.png")
    #     image_url = json_response["data"][0]["url"]  # extract image URL from response
    #     generated_image = requests.get(image_url).content  # download the image

    #     with open(image_path, "wb") as image_file:
    #         image_file.write(generated_image)

    #     image_files = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]



    #     i+=1
    #     a+=1

    # st.image(image_files) 


        


        # image_url = result_1['data'][0]['url']
        # urllib.request.urlretrieve(image_url, f"images/image{i}.jpg")


        # json_response = json.loads(result_1.model_dump_json())
        # # image_path = os.path.join(image_dir, 'generated_image.png')
        # image_path = os.path.join(image_dir, f"generated_image{a}.png")
        
        # json_response = json.loads(result_1.model_dump_json())
        # image_url = json_response["data"][0]["url"]  # extract image URL from response
        # image_path = urllib.request.urlretrieve(image_url, f"images/image{i}.jpg")
        # generated_image = requests.get(image_url).content  # download the image
        #Retrieve the generated image

        



    
        # result = client.images.generate(
        # model="dall-image-gen", # the name of your DALL-E 3 deployment
        # prompt=para.strip(),
        # n=1
        # )
    # downloads_dir = os.path.expanduser("~/Images")
    # i=1
    # a = i-1
    # for para in paragraphs[:-1]:
    #     # response = openai.Image.create(
    #     # prompt=para.strip(),
    #     # n=1,
    #     # # size="512x512"
    #     print(paragraphs[i-1])
    #     result = client.images.generate(
    #     model="dall-image-gen", # the name of your DALL-E 3 deployment
    #     prompt=paragraphs[i-1],
    #     n=1
    #     )

    #     #image_path = os.path.join(downloads_dir, f"generated_image{a}.png")
        
    #     json_response = json.loads(result.model_dump_json())
    #     image_url = json_response["data"][0]["url"]  # extract image URL from response
    #     image_path = urllib.request.urlretrieve(image_url, f"images/image{a}.jpg")
    #     generated_image = requests.get(image_url).content  # download the image
    #     #Retrieve the generated image
    #     with open(image_path, "wb") as image_file:
    #         image_file.write(generated_image)
        
    #     i+=1
    #     a+=1


    # # Display the image in the default image viewer
    # image_folder = "images"
    # image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    # st.subheader("The images for the story is shown below")
    # st.image(image_files) 

    # displaying images on website using streamlit  

        # image_url = response['data'][0]['url']
        # urllib.request.urlretrieve(image_url, f"images/image{i}.jpg")
#         tts = gTTS(text=para, lang='en', slow=False)
#         tts.save(f"audio/voiceover{i}.mp3") # saving audio in a directory called audio
#         # Loading the audio file using moviepy
#         audio_clip = AudioFileClip(f"audio/voiceover{i}.mp3")
#         audio_duration = audio_clip.duration

#         # Loading the image files using moviepy
#         image_clip = ImageClip(f"images/image{i}.jpg").set_duration(audio_duration)

#         # Use moviepy to create a text clip from the text
#         text_clip = TextClip(para, font="Lane", size=(400, 0), color="black", bg_color="aqua")
#         text_clip = text_clip.set_pos('center').set_duration(audio_duration)

#         # Use moviepy to create a video for each "paragraph" by concatenating
#         clip = image_clip.set_audio(audio_clip)
#         video = CompositeVideoClip([clip, text_clip])

#         # Save the videos in a directory
#         video = video.write_videofile(f"videos/video{i}.mp4", fps=24)

# i+=1

    # image_folder = "images"
    # # Get a list of image files in the folder
    # image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    # st.subheader("The images for the story is shown below")
    # st.image(image_files) # displaying images on website using streamlit 

#     clips = []
#     l_files = os.listdir("videos")
#     for file in l_files:
#         clip = VideoFileClip(f"videos/{file}")
#         clips.append(clip)

#     # Merging the audio and image files to create a final video
#     final_video = concatenate_videoclips(clips, method="compose")
#     final_video = final_video.write_videofile("final_video.mp4")

#     video_file = open('final_video.mp4', 'rb') 
#     video_bytes = video_file.read() 
#     st.subheader("The video narrating the story with images is shown below")
#     st.video(video_bytes) #displaying the final video using streamlit

# else:
#     st.write("Click the button to generate the story.")