import whisper
import speech_recognition

def init():
    global model, recognizer, mic

    print("Loading model...")
    model = whisper.load_model("base.en")
    recognizer = speech_recognition.Recognizer()
    mic = speech_recognition.Microphone()

    print("Adjusting for ambient noise")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
    
    print("Finished")