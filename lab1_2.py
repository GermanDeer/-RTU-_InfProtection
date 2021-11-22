#from os import path


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

def decryption_by_mono(line):
    message = ''
    for sym in line:
        if sym.isalpha():
            message += common_letters[enc_letters.index(sym)]
        else:
            message += sym
    return message


def percentage(x, count):
    return round(x*100/count,3)


bias = 6                    #Смещение
key = 'метал'               #Ключ
abc = get_abc(bias, key)    #Генерация алфавита
print(abc)

path = 'H:/Projects/protection_inf/'

book = open(path + 'book.txt','r',encoding='utf-8')
enc_book = open(path + 'enc_book.txt','w',encoding='utf-8')
print(ord('я'))

mono_gramms = {}
bi_gramms = {}
num_of_monogramms = 0
num_of_bigramms = 0

for line in book:
    new_line = encrypt_line(line,abc)
    tmp = ''
    for sym in new_line:
        if sym.isalpha():

            if sym in mono_gramms.keys():
                mono_gramms[sym] += 1
            else:
                mono_gramms[sym] = 1
            num_of_monogramms += 1


            if tmp.isalpha():
                bi = tmp+sym
                if bi in bi_gramms.keys():
                    bi_gramms[bi] += 1
                else:
                    bi_gramms[bi] = 1
                num_of_bigramms += 1
        tmp = sym
    enc_book.write(new_line)

mono_gramms = {k: percentage(v, num_of_monogramms) for k, v in sorted(mono_gramms.items(), key=lambda item: item[1], reverse = True)}
bi_gramms = {k: percentage(v, num_of_bigramms) for k, v in sorted(bi_gramms.items(), key=lambda item: item[1], reverse = True)}

common_letters = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъ'
enc_letters = list(mono_gramms)


print(mono_gramms)
print(bi_gramms)

enc_book.close()
enc_book = open(path + 'enc_book.txt','r', encoding='utf-8')
dec_book = open(path + 'dec_book.txt','w', encoding='utf-8')

for line in enc_book:
    dec_book.write(decryption_by_mono(line))







