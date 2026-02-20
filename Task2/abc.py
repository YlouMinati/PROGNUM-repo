a =float(input('value a = '))

b =float(input('value b = '))

c =float(input('value c = '))

D= (b**2-4*a*c)



if D > 0:
    x_1= (-b+((b**2)-4*a*c)**0.5)/(2*a)
    x_2= (-b-((b**2)-4*a*c)**0.5)/(2*a)
    print(f'x+ = {x_1} ', f'x- = {x_2}')
    
elif D == 0:
    x_1= (-b+((b**2)-4*a*c)**0.5)/(2*a)
    print(f'x = {x_1}')
    
else:
    print('not obtainable')