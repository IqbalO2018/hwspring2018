#import csv
#csv.reader
#def csvReader
import CSV
With open(‘roster.csv’, ‘rb’) as f:
reader = csv.reader(f)
for row in reader:
print row
