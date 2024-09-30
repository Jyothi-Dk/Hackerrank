n=int(input())#3
dict1={}
for i in range(n):
    name=input()
    score=input()
    scores=list(map(int,score.split()))
    dict1[name]=scores
list1=[]
search_ele=input()
for name in dict1:
    if name==search_ele:
        for values in dict1[name]:
             list1.append(values)
        
print(list1)


sum1=sum(list1)
len1=len(list1)
print(sum1/len1)
          
    