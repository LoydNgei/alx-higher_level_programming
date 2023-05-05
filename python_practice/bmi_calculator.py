#!/usr/bin/python3



try:
    name = str(input("What is your name: "))
    weight = int(input("What is your weight in kgs: "))
    height = int(input("What is your height in Metres: "))
    Bmi = (Weight / height ** 2)
    print("Bmi result: {}".format(Bmi))
except (ValueError, NameError):
    print(Bmi)
if Bmi < 25:
    print("Hello {}, you are not overweight".format(name))
else:
    print("Hello {}, you are overweight".format(name))
