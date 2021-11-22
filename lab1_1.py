def get_abc(bias, key):
    a = ord('а')
    abc = ''.join([chr(i) for i in range(a,a+32)])
    for sym in key:
        abc = abc.replace(sym, '')
    abc = key + abc
    for i in range(bias):
        abc = abc[-1] + abc[:-1]
    return abc

def encrypt_line(line, alphabet):
  message = ''
  for sym in line:
    if ord(sym) in range(1072,1104):
        message += alphabet[(ord(sym) - 1072)%33]
    elif ord(sym) in range(1040,1072):
        message += alphabet[(ord(sym) - 1040)%33]
    else:
        message += sym
  return message

bias = 2
key = 'кот'
message = ''

abc = get_abc(bias, key)

inp = input()
for sym in inp:
    if sym.isalpha():
        message += abc[(ord(sym) - 224)%33]
    else:
         message += sym
print(message)
print(abc)