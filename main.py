import speech_recognition as sr
import time, serial, threading

#py -3.8 main.py

ser = serial.Serial("COM3", 9600, timeout=1)

def main():

    r = sr.Recognizer()
    while True:
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Listening")

            audio = r.listen(source)

            try:
                phrase = r.recognize_google(audio).lower()
                print(f'You said {phrase}')
                if "stop" in phrase or "end" in phrase:
                    break
                elif "like" in phrase or "imagine" in phrase:
                    print("Taze")
                    #x = threading.Thread(target=shock, args=(1,))
                    #x.start()
                continue

            except Exception as e:
                print("Error :  " + str(e))

            # # write audio
            # with open("recorded.wav", "wb") as f:
            #     f.write(audio.get_wav_da
            
def shock(duration=1):
    time.sleep(1)
    ser.write(b'H')
    time.sleep(duration)
    ser.write(b'L')

if __name__ == "__main__":
    main()


