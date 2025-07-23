# 🧠 Python Built-in String Method

# Case Conversion
print('hello'.capitalize())       # Hello
print('HELLO'.lower())            # hello
print('hello'.upper())            # HELLO
print('my name'.title())          # My Name
print('Hello'.swapcase())         # hELLO
print('GROSS'.casefold())          # gross (more aggressive lowercase)

# Searching and Checking
print('apple'.find('p'))          # 1
print('apple'.rfind('p'))         # 2
print('apple'.index('p'))         # 1
print('apple'.rindex('p'))        # 2
print('apple'.startswith('a'))    # True
print('apple'.endswith('e'))      # True

# Modification 
print('apple'.replace('p', '*'))  # a**le
print(' hello '.strip())          # 'hello'
print(' hello'.lstrip())          # 'hello'
print('hello '.rstrip())          # 'hello'
print('python'.center(10, '*'))   # **python**
print('a\tb\tc'.expandtabs(4))    # a   b   c
print('42'.rjust(5, '0'))         # 00042
print('42'.zfill(5))              # 00042
print('unhappy'.removeprefix('un'))   # happy
print('filename.txt'.removesuffix('.txt'))  # filename

# Info & Boolean Checks
print(len('hello'))              # 5
print('banana'.count('a'))       # 3
print('abc'.isalpha())           # True
print('123'.isdigit())           # True
print('abc123'.isalnum())        # True
print('123'.isdecimal())         # True
print('12345'.isnumeric())       # True
print('var1'.isidentifier())     # True
print('hello'.islower())         # True
print('HELLO'.isupper())         # True
print('   '.isspace())           # True
print('hello\n'.isprintable())   # False
print('Hello World'.istitle())   # True

# Join and Split
print('a,b,c'.split(','))        # ['a', 'b', 'c']
print('a,b,c'.rsplit(',', 1))    # ['a,b', 'c']
print('a b c'.split())           # ['a', 'b', 'c']
print('line1\nline2'.splitlines())  # ['line1', 'line2']
print('-'.join(['a', 'b']))      # a-b

# Other Useful Methods
print('hello'.encode())          # b'hello'
print('hello world'.partition(' '))  # ('hello', ' ', 'world')
print('Hello {}, your score is {}'.format('Alice', 95))  # Hello Alice, your score is 95
