import sys

key_word = {'BEGIN': 'Begin',
            'END': 'End',
            'FOR': 'For',
            'IF': 'If',
            'THEN': 'Then',
            'ELSE': 'Else'
            }

delimiter = {':': 'Colon',
             '+': 'Plus',
             '*': 'Star',
             ',': 'Comma',
             '(': 'LParenthesis',
             ')': 'RParenthesis',
             ':=': 'Assign'
             }

file_path = sys.argv[1]

f = open(file_path, 'r')
for line in f.readlines():
    line = line.strip()
    i = 0
    while i < len(line):
        start = i
        if line[i].isalpha():  # 字符开头
            i += 1
            while i < len(line) and line[i].isalnum():
                i += 1
            if line[start:i] in key_word.keys():  # 关键字
                print(key_word[line[start:i]])
            else:  # 标识符
                print('Ident({})'.format(line[start:i]))
        elif line[i].isdigit():  # 数字开头
            i += 1
            while i < len(line) and line[i].isdigit():
                i += 1
            print('Int({})'.format(line[start:i]))
        elif line[i] in delimiter.keys():
            key = line[i]
            if line[i] == ':' and i + 1 < len(line) and line[i + 1] == '=':
                key = ':='
                i += 1
            print(delimiter[key])
            i += 1
        elif line[i] == ' ':
            i += 1
        else:
            exit(0)
exit(0)
