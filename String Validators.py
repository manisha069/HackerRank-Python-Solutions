if __name__ == '__main__':
    s = input()
    
    o=0
    for i in s:
        if i.isalpha() == True:
            o=1
            break;
    
        
    t=0
    for i in s:
        if i.isdigit() == True:
            t=1
            break;
    
    
    th=0
    for i in s:
        if i.islower() == True:
            th=1
            break;
    
        
    f=0
    for i in s:
        if i.isupper() == True:
            f=1
            break;
    
        
        
    #is alpha-num
    if o==1 or t==1:
        print("True")
    else:
        print("False")
    
    
    #is alpha
    if o==1:
        print("True")
    else:
        print("False")   
      
    #is digit    
    if t==1:
        print("True")
    else:
        print("False")
        
    #is lower
    if th==1:
        print("True")
    else:
        print("False")
        
    # is upper
    if f==1:
        print("True")
    else:
        print("False")
        
