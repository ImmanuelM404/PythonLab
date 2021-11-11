#data_presenter.py


open_file = open('CupcakeInvoices.csv')

for line in open_file:     #loop through data and print each row 
    print(line)
open_file.close()

open_file = open('CupcakeInvoices.csv')

for line in open_file:
    line = line.split(',')  #.split separates each cloumn into an array based on the comma
    print(line[2])
open_file.close()


open_file = open('CupcakeInvoices.csv')

for line in open_file:
    line = line.split(',')
    total = float(line[3]) * float(line[4])
    print(format(total, '.2F'))

open_file = open('CupcakeInvoices.csv')

sumnedTotals = 0 
for line in open_file:
    line = line.split(',')
    total = float(line[3]) * float(line[4])    
    sumnedTotals = sumnedTotals + total
print(format(sumnedTotals, '.2F'))    #'.2F' format is fromating the org float to only to 2decimals 



