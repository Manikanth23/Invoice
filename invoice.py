product1_name, product1_price = 'Books', 50.00
product2_name, product2_price = 'Computer', 10000.00
product3_name, product3_price = 'Monitor', 5000.00

company_name = 'Sravanthi Super Market'
company_address = 'Alwal'
company_city = 'Hyderabad'

message = 'Thanks for shopping with us today!'
# create a top border
print('*' * 50)

print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))
# print a line between sections
print('=' * 50)

print('\tProduct Name\tProduct Price')
# create a print statement for each item
print('\t{}\t\tRs.{}'.format(product1_name.title(), product1_price))
print('\t{}\tRs.{}'.format(product2_name.title(), product2_price))
print('\t{}\t\tRs.{}'.format(product3_name.title(), product3_price))

print('=' * 50)
# print out header for section of total
print('\t\t\tTotal')
# calculate total price and print out
total = product1_price + product2_price + product3_price
print('\t\t\tRs.{}'.format(total))
# print a line between sections
print('=' * 50)
print('\n\t{}\n'.format(message))