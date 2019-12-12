print("How many kilometers did you cycle today?")
kms = float(input())
try: 
    print(f"Okay, you said {kms} kilometers, which is {round(kms/100*62,2)} miles")
except TypeError:
    print("Error: did not enter a valid number for kilometers.")