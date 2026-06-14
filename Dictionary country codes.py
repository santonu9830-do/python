country_code = {
    'India': '0091',
    'USA': '001',
    'UK': '044'
}

print("Country Code for India is:")
print(country_code.get('India', 'Not Found'))

print("Country Code for Japan is:")
print(country_code.get('Japan', 'Not Found'))