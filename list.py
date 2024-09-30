N=int(input())
list1=[]
for i in range(N):
    choice=input().split()
    if choice[0]=='append':
        list1.append(int(choice[1]))
    elif choice[0]=='insert':
        list1.insert(int(choice[1]),int(choice[2]))
    elif choice[0]=='remove':
        list1.remove(int(choice[1]))
    elif choice[0]=='print':
       print(list1)
    elif choice[0]=='sort':
        list1.sort()
    elif choice[0]=='reverse':
        list1.reverse()
    elif choice[0]=='pop':
        list1.pop()
        
    