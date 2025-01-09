msg = "Roll a dice!"
print(msg)


import numpy as np

msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,9))

# —————— Test
variable = 'a'
variable_2 = '5'

print(type(variable), type(variable_2))

#print(variable, int(variable), int('5'), '5')  # int(variable) when it is 'a' does not work and result in complete crash

if 5==5 and variable in 'abcdefghi':
    print('Hello')

variable = variable + '-'*5
print(variable)