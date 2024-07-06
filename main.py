import speech_recognition as sr
import pyttsx3

# Initialize pyttsx3
engine = pyttsx3.init()

# Customizing the output voice
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

def get_response(user_input):
    if "how are you" in user_input.lower():
        return "I'm doing well, thank you!"
    elif "what's your name" in user_input.lower():
        return "I'm your assistant."
    elif "tell me a joke" in user_input.lower():
        return "Why don't skeletons fight each other? They don't have the guts!"
    else:
        return "Sorry, I didn't understand that."

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`."""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5.0)
   
    try:
        response = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        response = None
   
    return response

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    listening = True

    while listening:
        print("Listening...")
        speech_text = recognize_speech_from_mic(recognizer, microphone)
       
        if speech_text is None:
            print("Didn't recognize anything.")
            continue
       
        print(f"Recognized: {speech_text}")
       
        if "jarvis" in speech_text.lower():
            response_from_openai = get_response(speech_text)
            engine.setProperty('rate', 120)
            engine.setProperty('volume', volume)
            # Set a voice - example uses the first voice available
            engine.setProperty('voice', voices[0].id)
            engine.say(response_from_openai)
            engine.runAndWait()
        else:
            print("Didn't recognize 'jarvis'.")

if __name__ == "__main__":
    main()
