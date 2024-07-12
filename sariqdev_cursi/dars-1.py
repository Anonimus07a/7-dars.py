#print("duslaringiz ruyhatini tuzamiz")
#
#ismlar = []
#n=1
#while True:
#    savol = f"{n}-dustigizni ismini kiriting: "
#    ism = input(savol)
#    ismlar.append(ism)
#    takrorlash = input("yana dust qushasizmi? (ha / yo'q)")
#    n+=1
#    if takrorlash != 'ha':
#       break
#
#print("Duslaringiz ruyhti!")
#for ism in ismlar:
#    print(ism.title())

print("duslaringiz ruyhatini tuzamiz")

dostlar = {}
ishora = True
while ishora:
    ism = input("dustingizni ismini kiriting?")  
    yosh = input(f"{ism.title()}ning yoshini kiriting:")

    dostlar[ism] = int(yosh)

    qushish = input("yana malumot qushasizmi? (ha / yo'q)")
    if qushish != 'ha':
        ishora = False

for ism,yosh in dostlar.items():
    print(f"{ism.title()} {yosh}-yoshda")     