import os
import azure.cognitiveservices.speech as speechsdk
from moviepy.editor import * # importing moviepy (used for combining video audio and images)
from dotenv import find_dotenv, load_dotenv # importing dotenv to acquire the path to the API keys in the .env file
from text_generation import *


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

speech_key = os.getenv("AZURE_SPEECH_KEY")
speech_region = os.getenv("AZURE_SPEECH_REGION")
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)

a = 1
paragraphs = re.split(r"[.]", generated_story)

language_1 = 'en-US-JennyNeural'

if language == 'German':
    language_1 = 'de-DE-ConradNeural'

elif language == 'English':
    language_1 = 'en-US-JennyNeural'

elif language == 'French':
    language_1 = 'fr-FR-HenriNeural'

elif language == 'Spanish':
    language_1 = 'es-ES-ElviraNeural'

elif language == 'Italian':
    language_1 = 'it-IT-IsabellaNeural'
    
else:
    language_1 = 'en-US-JennyNeural'

audio_config_title = speechsdk.audio.AudioOutputConfig(filename=f'''audio/output_title.mp3''')
speech_config.speech_synthesis_voice_name=language_1
speech_synthesizer_title = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config_title)
# text_title = title_without_quotations
# speech_synthesis_result_title = speech_synthesizer_title.speak_text_async(text_title).get()


# german = 'de-DE-ConradNeural'
# english = 'en-US-JennyNeural'
# french = 'fr-FR-HenriNeural'
# spanish = 'es-ES-ElviraNeural'
# italian = 'it-IT-IsabellaNeural'

for para in paragraphs[:-1]:
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    audio_config = speechsdk.audio.AudioOutputConfig(filename=f'''audio/output{a}.mp3''')
    
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name=language_1
    
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    text = para.strip()
    
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    a+=1 
    