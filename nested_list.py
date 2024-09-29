n=int(input())
List_names=[]
scores=[]
names=[]
for i in range(n):
    name=input()
    score=int(input())
    new_list=[name,score]
    List_names.extend([new_list])
    for i in List_names:
        names.append(i[0])
        scores.append(i[1])
        
sorted_scores=sorted(scores)
unique_scores=list(set(sorted_scores))
mark_names=[name for name,score in List_names if score==unique_scores[1]]
for i in sorted(mark_names):
    print(i)
    
