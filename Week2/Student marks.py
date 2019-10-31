__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'


NUMBER_OF_MARKS = int(input('Please insert a number: '))

name = input ("Enter the student's name: ")
total_marks = []
for count in range (NUMBER_OF_MARKS):
    try:
        total_marks.append(int(input('Enter result: ')))

    except ValueError:
        print('Please use integers')


average_mark = sum(total_marks) / NUMBER_OF_MARKS
heighest_score = max(total_marks)
lowest_score = min(total_marks)
print ('The average mark for ' +name+ ' is: ' +str(average_mark))
print('The heightst score is: ' +str(heighest_score))
print('The lowest score is: ' +str(lowest_score))