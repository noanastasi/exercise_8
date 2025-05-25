n = int(input('n = '))

mx = int(input('a_{1}:'))
for i in range (1,n):
    a = int(input(f'a_{i+1}:'))
    if a > mx:
        mx = a
print('max=', mx)