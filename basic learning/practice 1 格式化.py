A=input('name:')
B=int(input('how old:'))
print('Hi, I am %s, I am %d years old.'%(A,B))

text = input('Write the sentence here:')
text = text[0].upper()+text[1:]
if text[-1:]!= '.':
    text=text+'.'
    print(text)


print("Hi. My name is {0} and I'm {1} years old.".format(input('name:'),int(input('old:'))))