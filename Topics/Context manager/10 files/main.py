# write your code here
for i in range(1, 11):
    name = f'file{i}.txt'
    with open(name, 'w') as file:
        file.write(f'{i}')
