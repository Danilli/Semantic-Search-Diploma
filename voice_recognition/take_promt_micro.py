import speech_recognition as sr


# Function to handle speech recognition
def recognize_speech(microphone, speech, r):
    with microphone as source:
        r.adjust_for_ambient_noise(source)  # Adapt to ambient noise levels
        audio = r.listen(source)  # Listen for audio input
        try:
            text = r.recognize_google(audio)  # Convert audio to text
            speech.append(text)  # Add recognized speech to list
        except sr.UnknownValueError:
            pass


def voice_rec():
    # Initialize recognizer
    r = sr.Recognizer()

    # Set up microphone as audio source
    microphone = sr.Microphone()

    # Initialize list to store speech
    speech = []
    # Continuously listen to speech and recognize it until the user is silent for 1s
    with microphone as source:
        r.adjust_for_ambient_noise(source)
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                speech.append(text)
            except sr.UnknownValueError:
                pass

            # Check if the user is silent for 1s, then stop listening and return full speech
            if r.energy_threshold > 4000:  # Set your own value for this threshold
                recognize_speech(microphone, speech, r)
            elif len(speech) > 0 and text == "stop":
                break

    full_text = " ".join(speech)  # Join recognized speech list into full text
    return full_text
