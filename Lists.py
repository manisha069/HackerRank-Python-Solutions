if __name__ == '__main__':
    N = int(input())
    li=list()
    for i in range(N):
        cm=input()
        cmd=cm.split()
        
        if cmd[0]=="insert":
            pos= int(cmd[1])
            val=int(cmd[2])
            li.insert(pos,val)
        
        elif cmd[0]=="print":
            print(li)
            
        elif cmd[0]=="remove":
            li.remove(int(cmd[1]))
            
        elif cmd[0]=="append":
            li.append(int(cmd[1]))
            
        elif cmd[0]=="sort":
            li.sort()
            
        elif cmd[0]=="pop":
            li.pop()
            
        elif cmd[0]=="reverse":
            li.reverse()

            
