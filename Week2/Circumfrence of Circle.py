__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'
from math import pi

while True:
    try:
        radius = int(input('Enter radius of circle: '))
    except ValueError:
        print('Please enter integers only')
        continue
    if radius < 0:
        print('Sorry cant do it')
    else:
        break


area= radius * pi
print('Area of circle is ' +str(area))
