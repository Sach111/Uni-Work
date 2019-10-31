__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'

name=input(str('Hello , who are you?: '))

if name ==str(''):
    print('Hello World!')

elif name.lower() == ('arthur'):
    print('My Leige! It is good to meet you.')

else:
    name = name.capitalize()
    print('Hello Sir, ' +name+ '. Its good to meet you')
