from give_bmi import give_bmi, apply_limit

height = [165.343, 172.765, 182.1255]
weight = [50.505050, 60.606060, 70.70070]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 20))
