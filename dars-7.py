
#def function(*args):
#    return args
#
#print(function("Jhon","stive")) 

#def function(*args):
#    ismlar = list(args)
#    ismlar.append("abdullox")
#    return ismlar
#
#n=0
#for ism in function("Jhon","bob","Stive"):
#    n+=1
#    print (n,ism)

#print(function('jhon'))
def function(**kwargs):
    number = input("sonini kiriting>>>")
    mualif = input("muallifini kiriting>>>")
    narxi = input("narxini kiriting>>>")
    haqida = input("kitob nima haqida>>>")
    yili = input("yilini kiriting>>>")
    books["nomi"]['number'] = number
    books["nomi"]['Author'] = mualif
    books["nomi"]['Price'] = narxi
    books["nomi"]['Description'] = haqida
    books["nomi"]['Year'] = yili
    print(books["nomi"])
    return kwargs 


num = 5
books={
    'HrriyPhoter':{
        "number":num,
        "Author":"  J. K. Rowling",
        "Price":"20$",
        "Description":"Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter",
        "Year":"1997"
    },
    "nomi":{
        "number":"",
        "Author":"",
        "Price":"",
        "Description":"",
        "Year":""
    }
}
natija = True

while natija: 
    Sell = input("qanday kitob kerak>>>")
    if Sell == 'HrriyPhoter':
        if Sell == 'HrriyPhoter':
            siz = input("siz bu kitobni sotib olasizmi>>>")
        if siz == 'ha':
            soni = int(input(f"bizda {num}ta kitob bor \n qancha sotib olasiz>>>"))
            num -= soni
            if num == 0:
                 print("bizda bu kitobdan qolmadi!")
                 break
            else:     
                print(f"kitob {num}ta qoldi sotib olganingiz uchun raxmat!")
        else:
            print("raxmat")   
    else:
        add = input("bizda bu kitob mavjud emas \n sizda bulsa sotasizmi?>>>")
        if add == 'ha':
            function()
        else:
            print("raxmat!")
