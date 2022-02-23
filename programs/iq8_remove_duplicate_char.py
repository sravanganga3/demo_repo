str = "aabbccddeeff"

used_str = ''
ip = []
for i in str:
    if i not in ip:
        ip.append(i)
    if i not in used_str:
        used_str = used_str+i

print("This is append of list: ", ip)
print("This is append of str: ", used_str)