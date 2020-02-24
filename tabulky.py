from datetime import date

main_value_list = []
first_column_list = []
second_column_list = []
third_column_list = []
results_list = [""]
relative = None
interval = []


while True:
    a = float(input("Hodnoty: "))
    if a != 0:
        main_value_list.append(a)
    else:
        break



number_of_values = len(main_value_list)

for i in range(1,number_of_values+1):
    first_column_list.append(i)

results_list.append(sum(main_value_list)/len(main_value_list))

for i in range(len(main_value_list)):
    second_column_list.append(main_value_list[i]-results_list[1])

results_list.append(0)

for i in range(len(second_column_list)):
    third_column_list.append(abs(second_column_list[i]))

results_list.append(sum(third_column_list)/len(second_column_list))
relative = (results_list[3]/results_list[1])*100
interval.append(results_list[1]-relative)
interval.append(results_list[1]+relative)

first_column_list.append(results_list[0])
main_value_list.append(results_list[1])
second_column_list.append(results_list[2])
third_column_list.append(results_list[3])

print("+----+---------+---------+---------+")
for i in range(len(first_column_list)):
    print("|",first_column_list[i]," "*(2-len(str(first_column_list[i])))+"|",round(main_value_list[i],2)," "*(7-len(str(round(main_value_list[i],2))))+"|",round(second_column_list[i],2)," "*(7-len(str(round(second_column_list[i],2))))+"|",round(third_column_list[i],2)," "*(7-len(str(round(third_column_list[i],2))))+"|")
    print("+----+---------+---------+---------+")




print("Relatívna odchýlka: ",relative,"%",sep="")
print("Najpravdepodobnejšia hodnota je: (",interval[0],";",interval[1],")",sep="")
print(date.today())
