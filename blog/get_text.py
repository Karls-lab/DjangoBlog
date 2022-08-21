# Testing python script
print("hello")
data = ""

f = open("text.txt", mode='r', encoding='utf-8')
for line in f:
	data += line
f.close()

print(data)
