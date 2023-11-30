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
from pydub import AudioSegment
import os
from django.shortcuts import render
import cv2
# from moviepy.editor import ImageSequenceClip
import moviepy.editor as mp

import pyttsx3

def lip_sync(request):
    if request.method == 'POST':
        text = request.POST['text']
        output_path = 'output.wav'
        text_to_speech(text, output_path)

        # Generate facial animations based on text
        frames = generate_facial_animations(text)

        # Convert frames to video
        video_path = 'output.mp4'
        frames_to_video(frames, video_path)

        return render(request, 'index.html', {'audio_path': output_path, 'video_path': video_path})

    return render(request, 'index.html')

def text_to_speech(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()


def frames_to_video(frames, video_path):
        # Load the audio file
        audio_path = "output.wav"

        # Create a recognizer instance
        recognizer = sr.Recognizer()

        # Read the audio file
        with sr.AudioFile(audio_path) as audio_file:
            audio = recognizer.record(audio_file)
        recognizer = sr.Recognizer()
        # Perform speech recognition on the audio
        text = recognizer.recognize_google(audio)

        # Print the recognized text
        print("Recognized Text:", text)

        # Load the avatar image
        avatar_image = cv2.imread('images/avatar.png')

        # Perform image processing or manipulation
        # Example operations:
        # - Resize the image: avatar_image = cv2.resize(avatar_image, (new_width, new_height))
        # - Crop a region of interest: roi = avatar_image[y:y+h, x:x+w]
        # - Apply filters or effects: avatar_image = cv2.filter2D(avatar_image, -1, kernel)

        # Save or display the modified image
        cv2.imwrite('modified_avatar_image.jpg', avatar_image)
        cv2.imshow('Modified Avatar Image', avatar_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




        # # Load the audio file
        # with sr.AudioFile(audio_path) as audio_file:
        #     # Read the audio data
        #     audio = recognizer.record(audio_file)

        #     # Perform speech recognition
        #     text = recognizer.recognize_google(audio)

        # # Print the recognized text
        # print("Recognized Text:", text)

        # # Extract phonemes using a phoneme extraction library or model
        # phonemes = generate_facial_animations(text)
        # print("Phonemes:", phonemes)
        # for phoneme in phonemes:
        #     # Retrieve the corresponding avatar movement for each phoneme
        #     avatar_movement = mouth_images_mapping.get(phoneme)
        #     if avatar_movement:
        #         # Append the avatar movement to the animation sequence
        #         animation_sequence.append(avatar_movement)
        #     else:
        #         # Handle the case when no avatar movement is found for a phoneme
        #         output_video_path = "output.mp4"
        # # Assuming each avatar movement is represented as an image file
        # frame_sequence = [cv2.imread(movement_image_path) for movement_image_path in animation_sequence]
        # video = mp.ImageSequenceClip(frame_sequence, fps=30)
        # video.write_videofile(output_video_path, codec="libx264")


def generate_facial_animations(text):
    mouth_images = []
    for phoneme in text:
        if phoneme == 'AH':
            mouth_images.append('path_to_mouth_image1.png')
        elif phoneme == 'P':
            mouth_images.append('path_to_mouth_image2.png')
        else:
            mouth_images.append('path_to_default_mouth_image.png')

    return mouth_images







# def generate_video(request):
#     if request.method == 'POST':
#         text = request.POST['text']
#         # Convert text to audio using gTTS library
#         tts = gTTS(text)
#         request.POST['text']
#         file_path='rec1.wav'
#         # file_path=tts.save('rec1.wav')
#         #pydub.AudioSegment.ffmpeg = "E:\avatarlipsync\avatarproject\ffmpeg-6.0-essentials_build\ffmpeg-6.0-essentials_build\bin"
#         if os.path.exists(file_path):
#             sound_file = AudioSegment.from_wav(file_path)
#             print(sound_file)
#         else:
#             print("File not found or inaccessible.")
#         # tts.save('harvard.FLAC')
        
#         # Use speech recognition to get the phonemes or sounds from the audio
#         # audio_file = "harvard.FLAC" 
#         recognizer = sr.Recognizer()
#         print(recognizer)
#         with sr.AudioFile(sound_file) as source:
#             audio = recognizer.record(source)
#         phonemes = recognizer.phonemes(audio, language='en-US', show_all=True)
#         print(phonemes)

#         # Use the phonemes/sounds to determine the corresponding mouth positions/images
#         mouth_images = map_phonemes_to_mouth_images(phonemes)
#         print(mouth_images)

#         # Generate the lip sync video using MoviePy
#         clip = ImageSequenceClip(mouth_images, fps=24)
#         clip.write_videofile('path_to_temp_video.mp4')

#         # Return the video file as a response
#         return FileResponse(open('path_to_temp_video.mp4', 'rb'), content_type='video/mp4')

#     return render(request, 'index.html')
