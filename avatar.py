from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse
from moviepy.editor import *
from pydub.exceptions import CouldntDecodeError
import speech_recognition as sr
import soundfile as sf 
from gtts import gTTS
# from avatarapp.utils import map_phonemes_to_mouth_images
from pydub.silence import split_on_silence
import pydub

import os
from django.shortcuts import render
import cv2



import pyttsx3
import moviepy.editor as mpy
from pydub import AudioSegment
from moviepy.editor import ImageClip, concatenate

#step1
text = "Hello, how are you today?"
engine = pyttsx3.init()
engine.save_to_file(text, 'testavatar.wav')
engine.runAndWait()

#step2
audio_path = "testavatar.wav"
recognizer = sr.Recognizer()
with sr.AudioFile(audio_path) as audio_file:
    audio = recognizer.record(audio_file)
text = recognizer.recognize_google(audio)
print("Recognized Text:", text)

#step3
avatar_image = cv2.imread('images/avatars.png')
cv2.imwrite('modified_avatar_image.jpg', avatar_image)
# cv2.imshow('Modified Avatar Image', avatar_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#step4
image_path = "modified_avatar_image.jpg"
audio_path = "testavatar.wav"
image = ImageClip(image_path)
audio = AudioSegment.from_wav(audio_path)
image = image.set_duration(len(audio) / 1000)  
start_time = 5000  # Set the start time in milliseconds
audios = audio[start_time:]

lip_sync_animation = concatenate([image + audios])
print(lip_sync_animation)
output_path = "lip_sync_animation.mp4"
lip_sync_animation.write_videofile(output_path, codec='libx264')