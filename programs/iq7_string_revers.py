str1 = "sravan kumar"

print("using bultin methods")
print("".join(reversed(str1)))


print("using slicing")
print(str1[::-1])


print("used loop")
used_loop = ''
for i in str1:
    used_loop = i+used_loop

print(used_loop)

print(' '.join(str1.split(' ')[::-1]))
