chat = []
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        if 'Allen' in line:
            name = 'Allen'
            continue
        elif 'Tom' in line:
            name = 'Tom'
            continue
        else:
            chat.append([name, line])

with open('output.txt', 'w', encoding = 'utf-8') as f:
    for name, line in chat:
        f.write(f'{name}: {line}')