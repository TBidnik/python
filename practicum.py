
# Задание №7

import json

with open("lesson_5_hw_77.json", "w") as j_file:
    with open("lesson_5_hw_7.txt", "r") as f_o:
        subjects = {}
        middle = {}
        k, o = 0, 0
        line = f_o.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                k += profit
                o += 1
            middle["avegare"] = k / o
        all_list = [subjects, middle]
    json.dump(all_list, j_file)
    



