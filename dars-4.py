
#parol = input("parolni kiriting? >>>")
#maxfiyparol = ""
#
#for i in parol:
#    i = '*'
#    maxfiyparol += i
#print(maxfiyparol)

#i = 0
#
#while i < 5:
#    print("salom")
#    i += 1 

Users = {
    'Jhon':{
        'email':'Jhon55@gmail.com',
        'password':'123321',
        'age':21
    },
    'Stive':{
        'email':'Stive@gmail.com',
        'password':123456,
        'age':21
    }
}
while True:
    search = input("Usernameni kiriting >>>")
    parol = input("parolni kiriting >>>")
    if search in Users and parol == Users[search]['password']:
        yes = input('parol maxfiy qolsinimi? >>>')
        if yes == 'ha': 
            maxfiy = ''
            for i in parol:
                i = '*'
                maxfiy += i
            print(f"emailingiz: {Users[search]['email']}")   
            print(F"parolingiz: {maxfiy}")
            print(f"Yoshingiz: {Users[search]['age']}")

        else:
            print(f"emailingiz: {Users[search]['email']}")
            print(f"parolingiz: {Users[search]['password']}")
            print(f"Yoshingiz: {Users[search]['age']}")
    else:
        savol = input("Bunday foydalanuvchi mavjud emas yangi accaunt qushasizmi? >>>")
        if savol == 'ha':
            email2 = input('emailni kiriting')
            password2 = input('password kiriting')
            age2 = input('age kiriting')

            Users['Stive']["email"] = [email2]
            Users['Stive']["password"] = [password2]
            Users['Stive']["age"] = [age2]

            print(f"Yangi email:{email2}, \n parol:{password2}, \n yosh:{age2}")
        else:
            print("Foydalanganingiz uchun raxmat!")
            break