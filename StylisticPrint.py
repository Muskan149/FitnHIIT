def stylisticPrint(text):
    print("----------------------------------")
    print(text)
    print("----------------------------------")

from time import sleep

def loadingEffectPrint(text):
    for x in "...." + text:
        print(x, end = "")
        sleep(0.125)
    print()
