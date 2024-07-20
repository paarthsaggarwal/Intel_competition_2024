# from openai import AzureOpenAI
# import os
# import requests
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
# import json
# from dotenv import find_dotenv, load_dotenv
# import re
# from text_generation import *
# from moviepy.editor import *

# dotenv_path = find_dotenv()
# load_dotenv(dotenv_path)

# i = 1
# b = i+1
# paragraphs = re.split(r"[.]", generated_story)

# client_1 = AzureOpenAI(
#     api_version=os.environ["AZURE_IMAGE_VERSION"],  
#     api_key=os.environ["AZURE_IMAGE_KEY"],  
#     azure_endpoint=os.environ['AZURE_IMAGE_ENDPOINT']
# )

# # title = "Whale is eating fish"

# result_title_images = client_1.images.generate(
#         model="dalle3", # the name of your DALL-E 3 deployment
#         prompt=f'''Generate a comic book cover with the title "{title_without_quotations}" ''',
#         n=1
#         )
    
# json_response = json.loads(result_title_images.model_dump_json())
# image_dir = os.path.join(os.curdir, 'images')
# image_path = os.path.join(image_dir, f"generated_image_title.png")
# image_url = json_response["data"][0]["url"]  # extract image URL from response
# generated_image_title = requests.get(image_url).content  # download the image

# with open(image_path, "wb") as image_file:
#     image_file.write(generated_image_title)

# image_files_title = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# st.image(image_files_title)

# i=1
# st.subheader("The images for the story is shown below")
# for para in paragraphs[:-1]:
#     # from tts import *
#     result_1 = client_1.images.generate(
#     model="dalle3", # the name of your DALL-E 3 deployment
#     prompt=para.strip(),
#     # seed=1,
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

#     # Loading the audio file using moviepy
#     audio_clip = AudioFileClip(f"audio/output{i}.mp3")
#     audio_duration = audio_clip.duration


#     # Loading the image files using moviepy
#     image_clip = ImageClip(f"images/generated_image{i}.png").set_duration(audio_duration)

#     # Use moviepy to create a text clip from the text
#     text_clip = TextClip(para)
#     text_clip = text_clip.set_pos('center').set_duration(audio_duration)

#     # Use moviepy to create a video for each "paragraph" by concatenating
#     clip = image_clip.set_audio(audio_clip)
#     video = CompositeVideoClip([clip, text_clip])


#     # Save the videos in a directory
#     video = video.write_videofile(f"videos/video{i}.mp4", fps=24)
    
#     # clip = VideoFileClip(f"videos/{file}")

#     # clips.append(clip)

#     i+=1
#     b+=1


# clips = []
# l_files = os.listdir("videos")

# for file in l_files:
#     clip = VideoFileClip(f"videos/{file}")
#     clips.append(clip)

# # Merging the audio and image files to create a final video
# final_video = concatenate_videoclips(clips)
# final_video = final_video.write_videofile("final_video.mp4")

# video_file = open('final_video.mp4', 'rb') 
# video_bytes = video_file.read() 
# st.subheader("The video narrating the story with images is shown below")
# st.video(video_bytes) #displaying the final video using streamlit

##################################################

###############################

# st.image(image_files_title)

# #Using Pillow#################################################################
# img = Image.open(f"images/generated_image_title.png")

# # Call draw Method to add 2D graphics in an image
# I1 = ImageDraw.Draw(img)

# # Custom font style and font size
# myFont = ImageFont.truetype('Arial.ttf', 65)

# # Add Text to an image
# I1.text((10, 10), title_without_quotations, font=myFont, fill =(255, 0, 0), align='center')

# # Display edited image
# img.show()

# # Save the edited image
# final_title_image = img.save(f"images/final_title_image.png")
# st.image(final_title_image)

# ##################################################################

# # json_response = json.loads(result_1.model_dump_json())

# # # Set the directory for the stored image
# # image_dir = os.path.join(os.curdir, 'images')

# # # If the directory doesn't exist, create it
# # if not os.path.isdir(image_dir):
# #     os.mkdir(image_dir)

# # # Initialize the image path (note the filetype should be png)
# # image_path = os.path.join(image_dir, 'generated_image.png')

# # # Retrieve the generated image
# # image_url = json_response["data"][0]["url"]  # extract image URL from response
# # generated_image = requests.get(image_url).content  # download the image

# # with open(image_path, "wb") as image_file:
# #     image_file.write(generated_image)

# # # Display the image in the default image viewer
# # image = Image.open(image_path)
# # image.show()
############################ChatGPT CODE##############
from openai import AzureOpenAI
import os
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json
from dotenv import find_dotenv, load_dotenv
import re
from text_generation import *
from moviepy.editor import *
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

paragraphs = re.split(r"[.]", generated_story)

i = 1
b = i + 1

# Initialize clips list
clips = []

client_1 = AzureOpenAI(
    api_version=os.environ["AZURE_IMAGE_VERSION"],  
    api_key=os.environ["AZURE_IMAGE_KEY"],  
    azure_endpoint=os.environ['AZURE_IMAGE_ENDPOINT']
)


# result_title_images = client_1.images.generate(
#         model="Dalle-3",  # the name of your DALL-E 3 deployment
#         prompt=f'''Generate a comic book cover with the title "{title_without_quotations}" ''',
#         n=1
#     )

# json_response = json.loads(result_title_images.model_dump_json())
# image_dir = os.path.join(os.curdir, 'images')
# image_path = os.path.join(image_dir, f"generated_image_title.png")
# image_url = json_response["data"][0]["url"]  # extract image URL from response
# generated_image_title = requests.get(image_url).content  # download the image

# with open(image_path, "wb") as image_file:
#     image_file.write(generated_image_title)

# audio_clip_title = AudioFileClip(f"audio/output_title.mp3")
# audio_duration_title = audio_clip_title.duration
# image_clip_title = ImageClip(f"images/generated_image_title.png").set_duration(audio_duration_title)

# clip_title = image_clip_title.set_audio(audio_clip_title)
# # video = CompositeVideoClip([clip, text_clip])
# video_title = CompositeVideoClip([clip_title])


# # Save video
# video_path_title = f"videos/video_title.mp4"
# video_title.write_videofile(video_path_title, fps=24)

# # Append video clip to clips list
# clips.append(VideoFileClip(video_path_title))

# def image_creation(style):
#     result_1 = client_1.images.generate(
#         model="Dalle-3",  # the name of your DALL-E 3 deployment
#         prompt=f'''Generate a image that would be seen in an educational book novel based on {para.strip()} 
#                     which has the words {para.strip()} written on it''',
#         n=1,
#         size="1024x1024"
#     )
        
#     return result_1

# with open('style.txt', 'r') as file:
#     # Read the entire file content
#     content_5 = file.read()

# style = content_5

# Iterate through paragraphs
for para in paragraphs[:-1]:
    # Generate image for the paragraph
    result_1 = client_1.images.generate(
        model="Dalle-3",  # the name of your DALL-E 3 deployment
        prompt=f'''Generate a image that would be seen in an educational book novel based on {para.strip()} 
                    which has the words {para.strip()} written on it''',
        n=1,
        size="1024x1024"
    )
    json_response = json.loads(result_1.model_dump_json())
    image_dir = os.path.join(os.curdir, 'images')
    image_path = os.path.join(image_dir, f"generated_image{i}.png")
    image_url = json_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    # image_files = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Save the generated image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    image_files = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # st.image("The images for the answer are shown below")
    # st.image(image_files)

    # Load audio clip
    audio_clip = AudioFileClip(f"audio/output{i}.mp3")
    audio_duration = audio_clip.duration

    # Load image clip
    image_clip = ImageClip(f"images/generated_image{i}.png").set_duration(audio_duration)
    # image_clip_title = ImageClip(f"images/generated_image_title.png").set_duration(audio_duration)
    # Create text clip
    # text_clip = TextClip(para).set_pos('center').set_duration(audio_duration)

    # Create video clip
    clip = image_clip.set_audio(audio_clip)
    # video = CompositeVideoClip([clip, text_clip])
    video = CompositeVideoClip([clip])


    # Save video
    video_path = f"videos/video{i}.mp4"
    video.write_videofile(video_path, fps=24)

    # Append video clip to clips list
    clips.append(VideoFileClip(video_path))

    # Increment counters
    i += 1
    b += 1

# Concatenate all video clips
final_video = concatenate_videoclips(clips)

# Write final video
final_video_path = "final_video.mp4"
final_video.write_videofile(final_video_path)

# Read final video bytes
with open(final_video_path, 'rb') as video_file:
    video_bytes = video_file.read()

st.subheader("The video for the answer is below")
# Display final video
# st.subheader("The video narrating the story with images is shown below")
st.video(video_bytes)
