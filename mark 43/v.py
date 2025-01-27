import pyttsx3

engine= pyttsx3.init()
voices=engine.getProperty("voices")

while True:
    find=int(input("type no"))
    if find<3:
        print(f"{find}voices name is:",voices[find].name)
    else:
        print("0")