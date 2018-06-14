li = [1, 2, 3, 4, 5]

for i, el in enumerate(li):
    print(f'Index: {i}, Element: {el}')

print("")

# The second argument to enumerate tells it what number to begin counting from
for i, el in enumerate(li, 10):
    print(f'Index: {i}, Element: {el}')
