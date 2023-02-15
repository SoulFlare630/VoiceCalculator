import speech_recognition as sr 
import wordtodigits as wtd

r = sr.Recognizer()
mic = sr.Microphone()
conv = wtd.convert(text="hello")


def remove(string_input): 
    return string_input.replace(" ", "")

print("This is a voice calculator that supports simple essential calculation functions.")
print("You can say 'Addition', 'Subtraction', 'Multiplication', 'Division'.")
print("Please say large numbers as induvidual digits (for example, instead of 1 million, say 1,0,0,0,0,0,0) as it (Google) finds it hard to process them.")
print("A quiet environment, reduced mic sensitivity along with a seperate microphone (if you have one) can make it easier (for Google) to recognize your voice")
input("Press Enter to continue.")
print("What operation would you like to do?")
print("You may wait one second and then speak.")

with mic as source:       
    r.adjust_for_ambient_noise(source)    
    audio = r.listen(source)    
operation = r.recognize_google(audio)

if operation == "addition":
    print("You have chosen Addition.")
    print("Say you first number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no1 = r.recognize_google(audio)
    conv1 = wtd.convert(text=no1)
    rem1 = remove(conv1)
    print("First number registered as " + str(rem1) + ".")
    print("Say your second number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no2 = r.recognize_google(audio)
    conv2 = wtd.convert(text=no2)
    rem2 = remove(conv2)
    print("Second number registered as " + str(rem2) + ".")
    result = int(rem1) + int(rem2)
    print("The answer is " + str(result) + ".")

elif operation == "subtraction":
    print("You have chosen Subtraction.")
    print("Say you first number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no1 = r.recognize_google(audio)
    conv1 = wtd.convert(text=no1)
    rem1 = remove(conv1)
    print("First number registered as " + str(conv1) + ".")
    print("Say your second number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no2 = r.recognize_google(audio)
    conv2 = wtd.convert(text=no2)
    rem2 = remove(conv2)
    print("Second number registered as " + str(rem2) + ".")
    result = int(rem1) - int(rem2)
    print("The answer is " + str(result) + ".")

elif operation == "multiplication":
    print("You have chosen Multiplication.")
    print("Say you first number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no1 = r.recognize_google(audio)
    conv1 = wtd.convert(text=no1)
    rem1 = remove(conv1)
    print("First number registered as " + str(rem1) + ".")
    print("Say your second number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no2 = r.recognize_google(audio)
    conv2 = wtd.convert(text=no2)
    rem2 = remove(conv2)
    print("Second number registered as " + str(rem2) + ".")
    result = int(rem1) * int(rem2)
    print("The answer is " + str(result) + ".")

elif operation == "division":
    print("You have chosen Division.")
    print("Say you first number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no1 = r.recognize_google(audio)
    conv1 = wtd.convert(text=no1)
    rem1 = remove(conv1)
    print("First number registered as " + str(rem1) + ".")
    print("Say your second number.")
    with mic as source:       
        r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)    
    no2 = r.recognize_google(audio)
    conv2 = wtd.convert(text=no2)
    rem2 = remove(conv2)
    print("Second number registered as " + str(rem2) + ".")
    result = int(rem1) / int(rem2)
    print("The answer is " + str(result) + ".")

else:
    print("Google misheard what you said - please go to a quiter environment and/or reduce you mic sensitivity and try again. If you have a better microphone, use that one.")
