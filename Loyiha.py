# Random sonni chaqirib olamiz
import random

# O'zgaruvchilar !!!
tekshir = 21
urinish = 0
game = 1
son = 0
i = 1

# O'yinga kirish salom berish !!!
print("                                                                  ____________________________________________________")
print("                                                                 |                                                    |")
print("                                                                 | Assalomu alaykum Son topish o'yiniga hush-kelibsiz |")
print("                                                                 |____________________________________________________|")

# Qayta o'ynash uchun sikl !!!
while tekshir==21:

    # Yangi o'yin boshlanganini bildirish va dizayn uchun !!!
    if game==0:
        print("                                                                         ______________________________________")
        print("                                                                        |                                      |")
        print("                                                                        |           NEW GAME PLAY !!!          |")
        print("                                                                        |______________________________________|")
        
    # O'zgaruvchilarni qayta 1 dan sanash uchun !!! 
    i = 1
    
    # Random son uchun chegara berish !!!
    chegara = int(input("\nMen o'ylaydigan sonlar chegarasini kiriting... "))
    
    # Random son olish !!!
    rson = random.randrange(chegara)
    
    # Urunishlar qabul qilish !!!
    urinish = int(input("Siz men o'ylagan sonni qancha urunishda topmoqchisiz... "))
    
    # Urunishlar soni tugaguncha yoki Random sonni topguncha sikl aylantirish !!!
    while urinish!=0:
        
        # Son qabul qilish va urunishlarni sanash !!!
        son = int(input(f"Urinishlar soni = {urinish+i-1}/{i}\nSon kiritishingiz mumkun... "))
        i+=1
        
        # Urunishlarni kamaytirish !!!
        urinish-=1
        
        # Random son bilan kiritilgan sonni tekshirish !!!
        if son==rson:
            
            # To'g'ri bo'sa o'yinni yakunlash !!!
            print(f"\nQoyil siz {i-1}-ta urunishda to'g'ri topdingiz !!!👏")
            break
        
        # Foydalanuvchiga yordam berish !!!
        if urinish!=0:
            if son < rson:
                print("Men o'ylagan son kattaroq !!!")
            else:
                print("Men o'ylagan son kichikroq !!!")
        else:
            print(f"Siz {i-1}-ta urunish bilan topa olmadingiz !!!")
    
    # Qayta o'ynashni tekshirish va new game play (ni) ishga tushurish !!!  
    tekshir = int(input("\nQayta o'ynashni hohlasangiz (21) kiriting agar to'xtatishni xoxlasangiz istalgan sonni kiriting !!!\n... "))
    game = 0     

# O'yinni To'xtaganligi haqida xabar berish !!!
print("                                                                          ____________________________________")
print("                                                                         |                                    |")
print("                                                                         |           GAME STOPED !!!          |")
print("                                                                         |____________________________________|")