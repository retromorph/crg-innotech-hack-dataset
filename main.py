import os

f = open('count.txt', 'r')
for category in f.readlines():
    os.system(f"idt run --i {category} --size 100 --engine duckgo --image-size 224 --api-key AIzaSyCJCs7A4UrfS5Bc7NwvI91JYT71-JxZKPc")
f.close()