f = open("file.txt",'a+')
f.write("tekst takoi vot")
f.seek(0)
s = f.readlines()
print(s)
f.close