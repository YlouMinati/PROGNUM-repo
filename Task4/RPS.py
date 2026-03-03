import numpy as np


# Input player
y= input('rock, paper, sciccor? --> write as R, P or S:  ')

# Assigning radnom cpu genaretad numbers to letters
c= np.array(['R', 'P', 'S'])
c_g= np.random.randint(0,2)
cpu=c[c_g] 


print(f'the computer played: {cpu}')

# Printing the outcome
if y == 'R' and cpu == 'R' :
    print('draw, play again!')
elif y ==' R' and cpu == 'S':
        print('YOU WON!!!!!!!')
elif y == 'R 'and cpu == 'P':
        print('you lose.... try again?')
elif y == 'P' and cpu == 'S':
        print('you lose.... try again?')
elif y == 'P' and cpu == 'R':
        print('YOU WON!!!!!!!')
elif y == 'P' and cpu == 'P':
        print('draw, play again!')
elif y == 'S' and cpu == 'R':
        print('you lose.... try again?')
elif y == 'S' and cpu == 'P':
        print('YOU WON!!!!!!!')
elif y == 'S' and cpu == 'S':
        print('draw, play again!')
        

