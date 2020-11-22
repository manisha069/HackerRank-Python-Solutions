if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    a=list(arr)
    a.sort()
    a.reverse()
    
    for i in a:
        if i != a[0]:
            print(i)
            break
        
