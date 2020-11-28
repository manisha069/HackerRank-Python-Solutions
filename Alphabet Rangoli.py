def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data=list()
    for i in range(n):
        data.append(alpha[i])
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        row="-".join(row)
        width= n*4-3
        row=row.center(width, "-")
        print(row)


    
    

