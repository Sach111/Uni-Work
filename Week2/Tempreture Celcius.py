__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'

while True:
    try:
        temperature_in_celcius = float(input('Please enter the temperature: '))
    except ValueError:
        print('Please enter integers only')
        continue
    else:
        break

temperature_in_farenheit = temperature_in_celcius * 1.8 + 32


print('The temp is ' +str(temperature_in_farenheit) + ' degrees farenheit')