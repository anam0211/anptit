s=input()
if s=='z' or s=='Z': print('a')
else:
    if s<'a' or s>'z':
        print(chr(ord(s)+33))
    else:
        print(chr(ord(s)+1))