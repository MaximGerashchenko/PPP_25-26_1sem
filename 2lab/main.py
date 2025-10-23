#ЭТО НОМЕР 6 ВО ВТОРОЙ ЛАБОРАТОРНОЙ 

s = input()
st = []
for i in range(len(s)):
    c = s[i]
    if c in '([{':
        st.append(c)
    elif c == ')':
        if not st or st[-1] != '(':
            print(i + 1)
            exit()
        st.pop()
    elif c == ']':
        if not st or st[-1] != '[':
            print(i + 1)
            exit()
        st.pop()
    elif c == '}':
        if not st or st[-1] != '{':
            print(i + 1)
            exit()
        st.pop()
if st:
    print(len(s) + 1)
else:
    print('ok')
