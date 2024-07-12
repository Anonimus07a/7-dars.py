#ism = input("ismingiz nima: ")
#yosh = input('yoshingiz nechchida: ')
#print('ismingiz: ' + ism, '; yoshingiz: ' + '' + yosh)
#print("anvar" =='Anvar')
#print(10**2<2**10)

#son1 = input("son kiriting:")
#son2 = input("son kiriting:")
#qiymat = input("amalni kiriting:")
#
#if qiymat == '+':
#    print(int(son1)+int(son2))
#elif qiymat == '-':
#    print(int(son1)-int(son2))
#elif qiymat == '*':
#    print(int(son1)*int(son2))
#elif qiymat == '/':
#    print(int(son1)/int(son2))
#else:
#    print('bunday qiymat mavjud emas!') 

# Uy ishi 

#Users = {
#    
#}
#
#ism = input("usernameni kiriting:")
#password = input("parolni kiriting:")
#password2 = input("parolni qayta kititing:")
#
#if password == password2:
#    print()
#elif password != password2:
#    input("parol notug'ri qayta kiriting:")
#    
#bush = input("accaunt mavjud emas yangi accaunt qushishni hohlaysizmi?") 
#
#if bush == "ha":
#    Users[ism] = password
#else:
#    print('raxmat') 
#
#print("sizning accauntingiz ochildi:", Users)  

#Users = {
#    "Jhon":{
#        "password":"1234",
#        "email":"Jhon15@gmail.com",
#        "age":21
#    },
#    "Stive":{
#        "password":"123456789",
#        "email":"Stive55@gmail.com",
#        "age":17
#    }
#}  
#
#print(f"parol: {Users['Jhon']['password']}, \n email: {Users['Jhon']['email']}, \n age: {Users['Jhon']['age']}")

#Users = {
#    "Jhon":"Jhon",
#    "12345":"12345"
#}
#
#ism = input("ism kiriting")
#parol = input("parolni kiriting")
#
#if Users["12345"] == 12345 and Users["Jhon"] == "Jhon":
#    print("siz ruyxatdan utingiz!")  
#elif Users["12345"] == 12345 and Users["Jhon"] == "Jhon":
#    print("siz ruyxatdan utingiz!")      
#else:
#    print("parol notug'ri")   
# 

#topshiriq 1
#Users = {
#    "email": "Jhon55@gmail.com",
#    "ism": "Jhon",
#    "password": "12345",
#    "email2": "", 
#    "ism2": "",
#    "password2": ""
#}
#
#email = input("emailni kiriting:")
#ism = input("usernameni kiriting:")
#password = input("parolni kiriting:")
#
#if Users["email"] != email:
#    print("email xato!")
#elif  Users["ism"] != ism:
#    print("parol xato!")
#elif Users[ism] != ism:
#    print("username xato!")  

# topshiriq 2
Users = {
    "joylangan":{
    "email": "Jhon55@gmail.com",
    "ism": "Jhon",
    "Familiya":"Jhozev",
    "password":"12345"
    },
    "Joylanishikerak":{
    "email2": "", 
    "ism2": "",
    "password2": ""
    }
}

email = input("emailni kiriting:")
ism = input("usernameni kiriting:")
Familiya = input("lastnameni kiriting:")
password = input("parolni kiriting:")

if Users["joylangan""email"] != email:
    print("email xato!")
elif  Users["joylangan"["ism"]] != ism:
    print("ism xato!")
elif  Users["joylangan"["Familiya"]] != Familiya:
    print("Familiya xato!")    
elif Users["joylangan"["password"]] != password:
    print("password xato!")  
yes = input("berilgan accaund xato yangi ochishni xoxlaysizmi:")
 
if yes.lower() == "ha" or "xa" or "yes" or "ok" or "albatta":
    email2 = input("yangi emailni kiriting:")
    ism2 = input("yangi usernameni kiriting:")
    Familiya2 = input("yangi lastnameni kiriting:")
    password2 = input("yangi parolni kiriting:")
    
    Users["Joylanishikerak"["email2"]] = email2 
    Users["Joylanishikerak"["ism2"]] = ism2
    Users["Joylanishikerak"["Familiya2"]] = Familiya2
    Users["Joylanishikerak"["password2"]] = password2
    
    print(f"Yangi emailingiz: {Users['email2']}, Username: {Users['ism2']}, lastname: {Users['Familiya2']}, Password: {Users['password2']}")
else:
    print("Raxmat")
    
