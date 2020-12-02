def merge_the_tools(string, k):
    t=list()
    for i in range(0,len(string), k):
        x=string[i:i+k]
        t.append(x)
            
    for i in range(len(t)):
        x=""
        for j in  range(k):
            if t[i][j] in x:
                continue
            else:
                x=x+t[i][j]
        print(x)
       
    
    
    
