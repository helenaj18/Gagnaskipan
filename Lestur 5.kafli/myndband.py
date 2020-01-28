# aðgerðir sem "má" ekki gera
list1 = [4,2,6,4,8]
print(list1)
list1.insert(3,11)
print(list1)
list1.append(22)
print(list1)

list2 = [10,20,30]

list3 = list1 + list2print(list3)


for i in range(len(list3)):
    list3[i] += 1


print(list3)
print(list2)
print(list1)


# aðgerðir sem má gera

list1 = [0] * 5 # til að initializa lista
list1[0] = 4
list1[1] = 2
list1[2] = 6
list1[3] = 4
list1[4] = 8


# má setja stak og prenta en ekki heilan lista
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

list1[1] = list1[4]


