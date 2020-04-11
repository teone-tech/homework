listOfNumbers = [3,2,1,4,5,6,7,8,9,22,25,16,17,28]
a=0
sorted_list=[]
while True:
    if a in listOfNumbers:
        sorted_list.append(a)
    a += 1
    if a>max(listOfNumbers):
        break
new_list = []
for i in sorted_list:
    if i%2 != 0:
        new_list.append(i)
new_list.append('startOF->evens')
for i in sorted_list:
    if i%2 == 0:
        new_list.append(i)
print(new_list)