x = float(input('x= '))
y = float(input('y= '))
#оскільки нема повних чисел правильним буде викоистання саме float
if abs(x)<y and y<1:
    print('Належить')
else:
    print('не належить')