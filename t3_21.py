m = int(input())
k = 0
while 4**k<m:
    k+=1
print(k-1)


#or

m = int(input())
k = 0
while True:
    if 4**k >= m: break
    k+=1
print(k-1)
