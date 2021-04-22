A = [1,2,3]
B = [1,2,3]

i = 0
new = []
for element in A:
    x = element * B[i]
    i = i +1 
    new.append(x)

print(new)

new2 = []
for y in enumerate(A):
    x = A[y]*B[y]
    new2.append(x)

print(new2)