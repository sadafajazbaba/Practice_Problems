def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    
    print("Your BMI is:", bmi)
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print("You are normal weight.")
    elif bmi >= 25 and bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()