# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set()
for i in range(n):
    x=input()
    a.add(x)
    
print(len(a))
