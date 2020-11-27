n=int(input())
x=list()
for i in range(n):
    x.append(input())
    
for i in range(n):
    try:
        a, b= x[i].split()
        m=int(a)
        n=int(b)
        f= m//n
        print(f)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
