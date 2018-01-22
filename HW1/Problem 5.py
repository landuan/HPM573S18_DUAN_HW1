# Problem 5
months = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
          '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
print(months.keys())
print(months.values())
for (key, value) in months.items():
    if key == '1':
        print('the', key, 'st month is', value)
    elif key == '2':
        print('the', key, 'nd month is', value)
    elif key == '3':
        print('the', key, 'rd month is', value)
    else:
        print('the', key, 'th month is', value)
for (key, value) in months.items():
    print(value, 'is month', key)
