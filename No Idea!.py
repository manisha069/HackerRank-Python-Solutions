
n,m=input().split()

aa=input().split()
A=set(input().split())
B=set(input().split())
score=0
for i in aa:
    if i in A:
        score += 1
    elif i in B:
        score -= 1
print(score)
