import random


with open('./japanese_learning/ichidanverbs.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split(',')
    if lines[i][1][-1] == '\n':
        lines[i][1] = lines[i][1][:len(lines[i][1])-1]

order = [(x,y) for y in range(2) for x in range(len(lines))]

random.shuffle(order)

todo = order.copy()
while len(todo) > 0:
    i = 0
    while i < len(todo):
        inp = input("Traduci '"+lines[todo[i][0]][todo[i][1]]+"': ")
        if inp == lines[todo[i][0]][todo[i][1]-1]:
            print("Corretto!\n")
            todo.pop(i)
        else:
            print("Sbagliato! la risposta corretta era: '"+lines[todo[i][0]][todo[i][1]-1]+"'\n")
            i+=1

    random.shuffle(todo)



