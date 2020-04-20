import os
import sys
import csv
import operator

stati = ['DONE','TODO']
types = ['HW','PERSONAL','']
class todo_organizer:


    def __init__(self, filename):
       f = open(filename, 'r')
       self.reader = csv.reader(f,delimiter=',')
       
    def sort_stati(self):
        ''' I will sort the stati in this order TODO, DONE '''
        self.sort = sorted(self.reader, key=operator.itemgetter(1), reverse=True)
        

if __name__ == '__main__':
   og = todo_organizer('TO-DO.csv')
   for row in og.reader:
       print(row)

#   og.sort_stati()
#   print(og.sort)
#   for row in og.sort:
#       print(row)

