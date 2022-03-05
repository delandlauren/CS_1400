'''
Lauren DeLand
CS 1400-005
Rabbits, Rabbits, Rabbits
03/04/2022

'''
# imports csv reader
import csv

#defines function and parameters
def do_research(cages, adults, babies):
    month = 1
    total = adults + babies
    
    #open file to write in
    with open('C:/Users/default.DESKTOP-DVRK650/OneDrive/Documents/rabbits.csv', 'w') as output_file:
        print('# Table of rabbit pairs\nMonth, Adults, Babies, Total',file = output_file)
        
        print(f'{month}, {adults}, {babies}, {total}', file = output_file)

        # loops the equation until proven False
        while total < cages:
            babies = adults
            adults = total
            month += 1
            total = babies + adults
            print(f'{month}, {adults}, {babies}, {total}', file = output_file)

        
        print(f'# Cages will run out in month {month}', file = output_file)

# User input for parameters

cages = int(input(""))
adults = int(input(""))
babies = int(input(""))

# calls the function
def main():
    do_research(cages, adults, babies)
if __name__ == '__main__':
    main()

