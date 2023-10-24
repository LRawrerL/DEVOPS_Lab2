def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))

    if bmi <= 18.5:
        print("Underweight")
    elif bmi <= 25:
        print("Normal")
    elif bmi > 25:
        print("Overweight")


calculate_bmi(1.73, 57)