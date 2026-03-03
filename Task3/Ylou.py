# Masses solar system objects
masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]


# Creating the new list
n_list = []


# looping through to get the right value's
for i in masses:
    if i > 7.349e+22:
        n_list.append(i)
        

print(n_list)


# new list
nn_list = n_list

print()
print(nn_list[5:])


print('the sum: ')
print(sum(nn_list[5:]))

print()
print('the len: ')
print(len(nn_list[5:]))

