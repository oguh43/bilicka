import math
import sys
import time

main_value_list = []
first_column_list = []
second_column_list = []
results_list = [""]




while True:
    a = float(input("Hodnoty: "))
    if a != 0:
        main_value_list.append(a)
    else:
        break

print(main_value_list)


number_of_values = len(main_value_list)
for i in range(1,number_of_values+1):
    first_column_list.append(i)

results_list.append(sum(main_value_list)/len(main_value_list))
print(results_list)
print(first_column_list)

for i in range(len(main_value_list)):
    second_column_list.append(main_value_list[i]-results_list[1])
print(second_column_list)

