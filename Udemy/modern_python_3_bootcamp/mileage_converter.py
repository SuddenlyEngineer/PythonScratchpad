print("How many kilometers did you cycle today?")
kms = input()
try: 
    print(f"Okay, you said {kms} kilometers, which is {kms/100*62} miles")
except TypeError:
    print("Error: did not enter a valid number for kilometers.")