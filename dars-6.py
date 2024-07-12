#def menignFunksiyam(ism):
#    print(f"salom{ism}")
#
#ismlar = input('ismlar kiriting>>>').split()
#
#menignFunksiyam(ismlar)

#ismlar = input("ismlar kiriting>>>").split()
#
#number = 1
#for ism in sorted(ismlar):
#    print(f"{number, menignFunksiyam()}) {ism.title()}") 
#    number += 1

#def calculator(son1, son2, amal):
#    if amal == '+':
#        print(son1+son2)
#    elif amal == '-':
#        print(son1-son2)
#    elif amal == '*':
#        print(son1*son2)
#    elif amal == '/':
#        print(son1/son2)  
#    else:
#        print("amal yoki berilgan son xato!")
#
#son1 = int(input("1-sonni kiriting?>>>"))
#son2 = int(input("2-sonni kiriting?>>>"))
#amal = input("amal kiriting?>>>")
#
#while True:
#    calculator(son1, son2, amal)

sell = input("qanday kitob olasiz?")

kitoblar = {
    "harry poter":{
        "Author":"  J. K. Rowling",
        "Price":"20$",
        "Description":"Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter",
        "Year":"1997"
    },
    "qushilgankitob":{
        "muallifi":"",
        "narxi":"",
        "haqida":"",
        "yili":""
    }
}


if sell == "harry poter":
    print("kitob narxi:20$")
    sel = input("bu kitobni sotib olasizmi>>>")
    if sel == 'ha':
        son = int(input("nechta sotib olasiz?"))
        print(f"siz {sell}dan {son}-ta sotib oldingiz \n sotib olganingiz uchun raxmat!")
    else:
        print("raxmat!")    
elif sell != kitoblar["harry poter"]:
    kitob = input("bu kitob mavjud emas \n shunday kitob sizda bulsa sotasizmi?")
    if kitob == "ha":
        Author = input('kitob muallifi>>>')
        Price = input('kitob narxi>>>')
        Description = input("qisqacha ma'lumot>>>")
        Year = input('nechanchi yili chiqgan>>>')
        kitoblar["qushilgankitob"]["muallifi"] = [Author]
        kitoblar["qushilgankitob"]["narxi"] = [Price]
        kitoblar["qushilgankitob"]["haqida"] = [Description]
        kitoblar["qushilgankitob"]["yili"] = [Year]
        print(kitoblar["qushilgankitob"])  
    else:
        print("raxmat!")    
