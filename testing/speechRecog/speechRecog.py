import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

try:
    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Adjusting for background noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Say something!")
        audio = recognizer.listen(source, phrase_time_limit=100)

    # Recognize speech using Google Web Speech API
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")

except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
