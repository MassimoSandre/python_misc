def fact(num):
    if ris[num] != -1:
        return ris[num]
    if num == 1 or num == 0:
        return 1
    
    ris[num] = fact(num-2)+fact(num-1)
    return ris[num]

ris = [-1]*10000

x = int(input("i: "))

print(fact(x))