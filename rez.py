dic = {}
for i in range(int(input())):   #   1st input = number of matches(n), 2nd input =n Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
    string = input().split(';')
    if string[0] not in dic:
        dic[string[0]] = [1, 0, 0, 0, 0]  # Команда:Всего_игр, Побед, Ничьих, Поражений, Всего_очков
    else:
        dic[string[0]][0] += 1
    if string[2] not in dic:
        dic[string[2]] = [1, 0, 0, 0, 0]
    else:
        dic[string[2]][0] += 1
    if int(string[1]) == int(string[3]):
        dic[string[0]][2] += 1
        dic[string[0]][4] += 1
        dic[string[2]][2] += 1
        dic[string[2]][4] += 1
    else:
        if int(string[1]) < int(string[3]):
            dic[string[0]][3] += 1
            dic[string[2]][1] += 1
            dic[string[2]][4] += 3
        else:
            dic[string[2]][3] += 1
            dic[string[0]][1] += 1
            dic[string[0]][4] += 3
for keys, values in dic.items():
    print(keys + ':',end = '')
    print(*values)