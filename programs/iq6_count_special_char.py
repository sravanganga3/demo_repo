import re

data = "this is dsd @#%gdkSSDLS:Ffg Ssdfs^&%$$"

re_data = re.findall('[^a-zA-Z\s]', data)

append_data = []
for i in re_data:
    append_data.append(i)

print(append_data)
print(len(append_data))