# animals = ['brey', 'jorge', 'matt', 'santy']
import time
# print(animals[3])

# for i in animals:
#     print(i)

# b = [5,5,10,30]

# total = 0
# for i in b:
#     total = total + i
# # print (total)
# total = 0
# for i in range (1,100):
#     total = total + i
    
# # print (total)
# total = 0
# for i in range (1,6):
#     if i % 2 == 0:
#         total = total +1
# print(total)

# print(list(range(1,7)))

count = 0 #total number of multiple of3,5

for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        print('+1')
        count = count + i
  
print(count)
