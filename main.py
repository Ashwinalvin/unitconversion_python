def printing():
    import pyttsx3

    speaker = pyttsx3.init()
    speaker.say("press 1 for km to miles    press 2 for km to meters   press 3 for metres to cm   press 4 for kg to grams  press 5 for deg to far")
    speaker.runAndWait()


printing()
entry = input("Hi I am arrow please enter u r choice of conversion")
entry=int(entry)

def kilotomiles():
    km=input("  enter km value to convert")
    km=float(km)
    miles=float(km/1.689)
    print(km,"km in kilometers is equal to",miles,"miles")


def kmtometer():
    km=input("  enter km value to convert")
    km=float(km)
    meter=float(km*1000)
    print(km,"km in metres is equal to",meter,"meters")
def mtocm():
    m=input("  enter m value to convert")
    m=float(m)
    cm=float(m*100)
    print(m,"m in cm is equal to",cm,"cm")
def kgtogr():
    kg=input("  enter kg value to convert")
    kg=float(kg)
    g=float(kg*1000)
    print(kg,"kg in grams is equal to ",g)
def degtofar():
    d=input("  enter degree value to convert")
    d=float(d)
    far=float(((9/5)*d)+32)
    print(d,"d in farnheit is equal to",far,"F")


if (entry==1):
    kilotomiles()
if (entry==2):
    kmtometer()
if (entry==3):
    mtocm()
if (entry==4):
    kgtogr()
if (entry==5):
    degtofar()



