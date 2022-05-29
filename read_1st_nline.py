file_1=open('demo.txt','r')
n=int(input('enter how many line do you want to read'))
for i in range(n):
    line=file_1.readline()
    print(line)