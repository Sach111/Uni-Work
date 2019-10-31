__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'

number_of_pupils = int(input('Number of pupils: '))
number_of_sweets = int(input('Number of sweets: '))
try:
    if number_of_sweets < 1 and number_of_pupils < 1:
        print('Sorry cant do it')
    else:
        sweets_per_pupil = number_of_sweets // number_of_pupils
        left_over_sweets = number_of_sweets % number_of_pupils

        print('Each pupil will get ' +str(sweets_per_pupil) + ' and there will be ' + str(left_over_sweets) + ' sweets left over')
except ValueError:
    print('Please use integers only')
