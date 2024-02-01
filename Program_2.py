Biological_gender = input("Please enter your biological gender (Male/Female): ")
Hemoglobin_value = float(input("Please enter your hemoglobin value (g/l): "))
hemoglobin_ranges = {
        "Male": {"low": 117, "high": 155},
        "Female": {"low": 134, "high": 167}}
if Biological_gender == 'Male':
    if Hemoglobin_value < hemoglobin_ranges[Biological_gender]['low']:
        print("Your hemoglobin level is low.")
elif Hemoglobin_value <= hemoglobin_ranges[Biological_gender]['high']:
    print("Your hemoglobin level is normal.")
else:
    print("Your hemoglobin level is high.")
if Biological_gender == 'Female':
    if Hemoglobin_value < hemoglobin_ranges[Biological_gender]['low']:
        print("Your hemoglobin level is low.")
        if Hemoglobin_value <= hemoglobin_ranges[Biological_gender]['high']:
            print("Your hemoglobin level is normal.")
else:
    print("Your hemoglobin level is high.")