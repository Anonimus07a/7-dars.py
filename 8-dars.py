from Function import Addbook, SellBooks  

num = 7

Books = {
    'HrriyPhoter': {
        "Quantiti": num,
        "Author": "J. K. Rowling",
        "Price": "20$",
    },
}

while True:
    search = input("Kitob nomini kiriting >>> ")
    if search in Books:
        book = Books[search]
        print(f"Nom: {search}\nMuallifi: {book['Author']}\nNarxi: {book['Price']}\nSoni: {book['Quantiti']}")
        quantity_to_sell = int(input(f"Qancha sotmoqchisiz '{search}' kitobidan? (1-{book['Quantiti']}) "))
        SellBooks(search, Books, quantity_to_sell)
    else:
        savol = input(f"{search} topilmadi. Bu kitobni qo'shasizmi? (ha/yo'q) ")
        if savol.lower() == 'ha':
            Author = input("Muallifini kiriting >>> ")
            Price = input("Narxini kiriting >>> ")
            Quantiti = int(input("Soni kiriting >>> "))
            Addbook(search, Books, Author=Author, Price=Price, Quantiti=Quantiti)  
