# Zip - aggregate elements from 2 or more iterables
# Result in tuple

usernames = ['A001', 'A002', 'A003', 'A004']
passwords = ('qwer', 'asfg', 'zxcv', 'yuio')
login_dates = ['01.02.21', '02.03.2022', '04.05.2019', '07.08.2018']

user_zip = zip(usernames, passwords)

for each_val in user_zip:
    print(each_val)

print(type(user_zip))

data_zip = zip(usernames, passwords, login_dates)
for data in data_zip:
    print(data)