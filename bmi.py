def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))

    return_value = 0
    if bmi <= 18.5:
        print("Underweight")
        return_value = -1
    elif bmi <= 25:
        print("Normal")
        return_value = 0
    elif bmi > 25:
        print("Overweight")
        return_value = 1
    return return_value


calculate_bmi(1.73, 57)