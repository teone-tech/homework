dictionarylanguage = {'university': {'ka':'უნივერსიტეტი', 'de': 'Universität'}}
english=input("enter word in english ")
if english in dictionarylanguage.keys():
    print(english)
else:
    b=input("enter this word in georgian ")
    c=input("enter this word in german ")

    dicta={}

    dictionarylanguage[english]=dicta
    dicta["ka"]=b
    dicta["de"]=c

print(dictionarylanguage)