#მომხმარებელს შემოატანინე 50 რიცხვი და შეინახე სიაში ლუწი რიცხვი თუ ინდექსით კენტ ადგილზეა დათვალე თითოეული
#ასეთი შემთხვევა ამოიწერე ინდექსი ელემენტი და დაბეჭდე
sia=[]
dict={}
while len(sia)!=10:
    number=input("enter number ")
    sia.append(number)

x=1
for i in sia:
    if int(i) % 2 ==0 and sia.index(i) % 2 != 0:
        dict[i]=x
        print("index is {} and element is {}".format(sia.index(i),i))

count=sum(dict.values())
print("amount of numbers which are even but have odd index is list {}".format(count))