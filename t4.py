#скалярний добуток

n = int(input())

v1 = []
v2 = []
for i in range(n):
    element_v1 = float(input(f'v1_{i+1}='))
    v1.append(element_v1)
    element_v2 = float(input(f'v2_{i+1}='))
    v2.append(element_v2)
print(v1, '\n', v2)

if len(v1) == len(v2):
    s = 0
    for i in range(n):
        s+=v1[i]*v2[i]

else:
    s = None
    print('wsdiwnwniwnefn')

print(s)