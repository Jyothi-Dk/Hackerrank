num=int(input())
power=input()
p_list=map(int,power.split())
power_list=list(p_list)#[9 3 1 2 4 2]
temp=power_list #[9 3 1 2 4 2]

sum1=sum(power_list)
main_sum=0
other_sum=0
ans=0
for i in power_list:
    main_sum+=i#9
    other_sum=sum1-main_sum#21-9
    ans+=1
    if other_sum<main_sum:
        break
print(ans)
    
    
    
    
    
    
    



# for i in power_list:
#     if i==max_no:
#         break
#     else:
#         sum+=i#12

# if sum>max_no:#12>9
#      sum=0
# max_sum=0
# sum_amt=[]
# for i in range(len(power_list)):# 9 3 1 2 4 2
#     if power_list[i]!=max(power_list):
#         sum+=power_list[i]
#     else:
#         max_sum+=max(power_list)
#         print(max_sum)
        
#         sum_amt.append(max_sum)
        
        
#         if sum>max_sum:
            
#             power_list=temp#3 1 2 4 2 
            
# print(sum_amt)
        
    
    