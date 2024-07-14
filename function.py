def Addbook(nomi, Books, **kwargs):
    Books[nomi] = kwargs
    return "kitob qushildi"

def SellBooks(book_title, books_dict, quantity_to_sell):
    if book_title in books_dict:
        if books_dict[book_title]["Quantiti"] >= quantity_to_sell:
            books_dict[book_title]["Quantiti"] -= quantity_to_sell
            print(f"{quantity_to_sell} ta '{book_title}' kitob sotildi.")
        else:
            print(f"bizda '{book_title}' kitobi qolmadi!")
    else:
        print(f"'{book_title}' nomli kitob topilmadi.")
