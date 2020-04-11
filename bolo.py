"""
დაწერეთ ფუნქცია რომელიც დაადგენს მომხმარებლის
მიერ შემოტანილი მნიშვნელობა მათემატიკურია თუ არა.
შემდეგ შემოატანინეთ მომხმარებელს 10 მნიშვნელობა
გამოყოფილი , ებით თითეული შეამოწმეთ არის თუ არა
მათემატიკური მნიშვნელობით თქვენივე ფუნქციის
დახმარებით ამის შემდეგ დაყავით ეს სია 2 ნაწილად და
*გააერთიანეთ Dictionary ში სადაც დაყოფილი სიის
პირველი ნაწილი იქნება key მეორე ნაწილი value.

*გააერთიანეთ - გაერთიანება მოახდინეთ ფუნქციის
საშუალებით რომელსაც დაარქმევთ mergeList( )
"""
rame=input("dawere rame gamoyavi mdzimeebit ','  ").split(",")
while len(rame)!=10:
    a=input("shemoitane rame ")
    rame.append(a)
x=0
dict={}
if rame[x] is int or float :
    half_length=len(rame)//2
    key=rame[0:half_length]
    value=rame[half_length:]
    for k in key:
        dict[key[x]]=value[x]
        x+=1
print(dict)











