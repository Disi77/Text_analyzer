# Sample text for analysis in file task_template.py
from task_template import TEXTS


login = {'bob': '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123'}

print(50 * '-')
print('Welcome to the app. Please log in:')
for i in range(3):
    username = input('USERNAME: ')
    password = input('PASSWORD: ')
    if login.get(username) == password:
        break
    else:
        print('Wrong username or password.')
print(50 * '-')


print('We have 3 texts to be analyzed.')
while True:
    try:
        choice = int(input('Enter a number btw. 1 and 3 to select: '))
        if choice in range(1, 4):
            break
    except ValueError:
        print('Enter a number !!!')
print(50 * '-')


text = TEXTS[choice - 1]
words = text.split()
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
numbers = []
word_lens = {}

for word in words:
    word = word.strip(' .,')
    if word.istitle():
        titlecase += 1
    if word.isupper():
        uppercase += 1
    if word.islower():
        lowercase += 1
    if word.isnumeric():
        numeric += 1
        numbers.append(int(word))
    word_len = len(word)
    word_lens[word_len] = word_lens.get(word_len, 0) + 1

print('There are {} words in the selected text.'.format(len(words)))
print('There are {} titlecase words.'.format(titlecase))
print('There are {} uppercase words.'.format(uppercase))
print('There are {} lowercase words.'.format(lowercase))
print('There are {} numeric strings.'.format(numeric))
print(50 * '-')


lens = list(word_lens)
lens.sort()

for item in lens:
    print('{:>2}  {}  {}'.format(item,
                                 word_lens[item] * '▬',
                                 word_lens[item]))
print(50 * '-')


print('If we summed all the numbers in this text we would get: {}'.format(sum(numbers)))
print(50 * '-')
