name = input()
age = int(input())
town = input()
salary = float(input())

range_age = None
range_salary = None

if age < 18:
    range_age = 'teen'
elif age < 70:
    range_age = 'adult'
else:
    range_age = 'elder'

if salary < 500:
    range_salary = 'low'
elif salary < 2000:
    range_salary = 'medium'
else:
    range_salary = 'high'

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Town: {town}')
print('Salary: $%.2f' % salary)
print(f'Age range: {range_age}')
print(f'Salary range: {range_salary}')
