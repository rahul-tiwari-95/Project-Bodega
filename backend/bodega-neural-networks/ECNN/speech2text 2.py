import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig

#Class responsible for speech recognition

subscription_key ='89bca3f0d5e54b3eb35e69a9300ba9aa'
region='eastus'


""""
Solomon Speech to Text Recognition CNN Class
Solomon Text to Speech Recognition CNN Class

"""

class solomonSpeech:
    
    def __init__(self):
       
        print('Authentication Success')
        
        
    
    def speech2text(self):
        print("========= Solomon Speech Recognition Neural Network Initiated ============")
        speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        
        print("====== Speak into your microphone =========")
        result = speech_recognizer.recognize_once_async().get() 
        print(result.text)
        
        return result.text
    
    
    def text2speech(self, textscript):
        print("============ Solomon Speech Recognition Neural Network Initiated =================")
        speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
        audio_config = AudioOutputConfig(use_default_speaker=True)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        synthesizer.speak_text_async(textscript)
        
        
        
