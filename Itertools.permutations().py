from itertools import permutations

k=input().split(" ")
ls=list(permutations(k[0],int(k[1])))
ls.sort()
for i in range(len(ls)):
    for j in ls[i]:
        print(j, end="")
    print()
