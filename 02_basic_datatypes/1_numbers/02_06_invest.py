'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

val_0 = float(input('Initial investment amount: '))
int_rate_perc = float(input('Interest rate in percentage: '))
int_rate = int_rate_perc / 100
years_float = float(input('Number of years to invest: '))

year_int = int(years_float)

print('Assuming interest is paid once per year and at the end of the investment period:')
for i in list(range(1,year_int+1)):
    val_fut = val_0 * (1 + int_rate)**i
    print('Value after ', i, 'years = ', val_fut)

val_end = val_0 * (1 + int_rate)**years_float

print('Value after ', years_float, 'years = ', val_end)
