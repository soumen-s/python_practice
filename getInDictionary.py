# Program to handling missing keys in dictionaries using get() function

country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# searching using get() function, if not find then the next string will print
print(country_code.get('India', 'Not Found'))

print(country_code.get('Japan', 'Not Found'))
