import math

n=13
students='Kkunjkhahorin'
prime=[]
composite=[]
for i in students:
    ascii=ord(i)
    # print(ascii)
    for i in range(2,(ascii//2)+1):
        if ascii%i==0:
            is_prime=False
            break
        else:
            is_prime=True
    if is_prime:
        
        prime.append(ascii)
    else:
        composite.append(ascii)
        

for i in prime:
    prime.sort()

for i in composite:
    composite.sort(reverse=True)
    
prime_str=''
for i in prime:
    prime_str+=chr(i)
comp_str=''
for i in composite:
    comp_str+=chr(i)
     

new_str=prime_str+comp_str
print(new_str)
