__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'

while True:
    try:
        temperature_in_farenheit = float(input('Please enter the temperature: '))
    except ValueError:
        print('Please enter integers only')
        continue
    else:
        break

temperature_in_celcius = temperature_in_farenheit / 1.8 - 32
temperature_in_celcius =str(round(temperature_in_celcius, 2))

print('The temp is ' +str(temperature_in_celcius) + ' degrees farenheit')