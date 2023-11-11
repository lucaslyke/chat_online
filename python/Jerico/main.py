import speech_recognition as sr
import pyttsx3
import openai

#setando a api da openai
openai.api_key = "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"

#inicializando o reconhecimento de fala
engine = pyttsx3.init()

#configurando a voz em português brasil
voices = engine.getProperty('voices')  #retorna uma lista com todas as vozes instaladas no sistema operacional
portuguese_voice = None
for voice in voices:
    if 'portuguese' in voice.languages:
        portuguese_voice = voice
        break
if not portuguese_voice is None: 
    engine.setProperty('voz', portuguese_voice.id)
else:
    print("não foi encontrada nenhuma voz em português")

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping unknown error")

def generate_response(prompt):
    #fazendo a solicitação da api
    response = openai.Completion.creat(
        engine="text-davinvi-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response['choices'][0]['text']

#Imprima as respostas geradas pelo modelo de audio
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Digite 'pandora' para começão a gravar sua pergunta: ")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio, language="pt-BR")
                if transcription.lower() == 'pandora':
                    filename = "input.wav"
                    print("Faça a sua pergunta: ")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename,'wb') as f:
                            f.write(audio.get_wav_data())
                    #transformando audio em texto
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"Você disse: {text}")
                        #Gerando resposta via CHATGPT
                        response = generate_response(text)
                        print(f"Jerico: {response}")
                        #Fala o resultado do chatbot
                        speak_text(response)

            except Exception as e:
                print('Ocorreu um erro', str(e))

if __name__ == "__main__":
    main()
