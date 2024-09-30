N = int(input())
list1=[]
for i in range(N):
    choice=input()
    if choice[0]=='a':
        split=choice.split()
        list2=list(map(int,split[1]))
        list1.extend(list2)
    list1=list1       
    if choice[0]=='i':
        split=choice.split()
        list2=list(map(int,(split[1],split[2])))
        list1.insert(list2[0],list2[1])
    list1=list1 
    if choice[2]=='m':
        split=choice.split()
        list2=list(map(int,split[1]))
        for i in list2:
            list1.remove(int(i))
    list1=list1
    
   
    if choice[2]=='v':
       list1.reverse()
    list1=list1  
       
    if choice[0]=='s':
       list1.sort()
    list1=list1
     
    if choice=='print':
      print(list1)
    list1=list1

    if choice=='pop':
        list1.pop()
    list1=list1