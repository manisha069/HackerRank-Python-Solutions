# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
M=set(map(int,input().split()))
n=int(input())
N=set(map(int,input().split()))

ls=list(M.symmetric_difference(N))
ls.sort()
for i in ls:
    print(i)
