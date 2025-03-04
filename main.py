import pyttsx3

if __name__ == '__main__':
    print("Welcome to the Speaker")
    print(" enter 'q' to Quit the Speaker")

while True:
    x = input("What do you want me to say? ")
    if x =='q':
        break
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()


