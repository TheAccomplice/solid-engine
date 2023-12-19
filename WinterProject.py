# 16 is shuffle (10, reset), 17 is show 2 (3) , 0 is double, 1 is 14 star, 2 is calander (10), 4 is prize
import random
error=0
list = []
for a in range(10000):
    foundno = 0
    for i in range(100):
        gotoprize = 4
        num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        random.shuffle(num_list)
        if num_list[4] == 16:
            num_list = [100] * len(num_list)
        elif num_list[4] == gotoprize:
            num_list[4] = 100
            gotoprize = 16
            foundno += 1
        elif num_list[4] != gotoprize:
            gotoprize = num_list[4]
            num_list[4] = 100
        while num_list[16] != 100:
            temp = 0
            if num_list[gotoprize] == 16:
                num_list = [100] * len(num_list)
            elif num_list[gotoprize] == 4:
                num_list[gotoprize] = 100
                gotoprize = 16
                foundno += 1
            elif num_list[gotoprize] == gotoprize:
                error += 1
            elif num_list[gotoprize] == 100:
                error += 1
            elif num_list[gotoprize] != gotoprize:
                temp = gotoprize
                gotoprize = num_list[gotoprize]
                num_list[temp] = 100
            else:
                print('d')
    list.append(foundno)
print(sum(list) / len(list))
print(list)


