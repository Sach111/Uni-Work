__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'
while True:
    try:
        Length_of_rectangle = int(input('Length of rectangle: '))
    except ValueError:
        print('Please enter integers only')
        continue
    if Length_of_rectangle < 1:
        print('Sorry cant do it')
    else:
        break
while True:
    try:
        Height_of_rectangle = int(input('Height of rectangle: '))
    except ValueError:
        print('Please enter integers only')
        continue
    if Height_of_rectangle < 1:
        print('Sorry cant do it')
    else:
        break

area= Length_of_rectangle * Height_of_rectangle
print('Area of rectangle is ' +str(area))
