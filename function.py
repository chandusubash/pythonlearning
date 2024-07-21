def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


tom_exp_list = [2100, 3500, 2800]
joe_exp_list = [500, 700, 1200]
toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)
print("Toms total expense : ", toms_total)
print("Joe's total expense : ", joes_total)
