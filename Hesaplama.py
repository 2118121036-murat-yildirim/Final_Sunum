def Toplama(a, b):
    return a + b

def Çıkarma(a, b):
    return a - b

def Çarpma(a, b):
    return a * b

def Bölme(a, b):
    if b == 0:
        return "Bölme işlemi için ikinci sayı sıfır olamaz!"
    return a / b

def display_menu():
    print("\nHesap Makinesi...")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Seçiminizi yapın: ")
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Birinci sayıyı giriniz: "))
            num2 = float(input("İkinci sayıyı girin: "))
            
            if choice == "1":
                print(f"Sonuç: {Toplama(num1, num2)}")
            elif choice == "2":
                print(f"Sonuç: {Çıkarma(num1, num2)}")
            elif choice == "3":
                print(f"Sonuç: {Çarpma(num1, num2)}")
            elif choice == "4":
                print(f"Sonuç: {Bölme(num1, num2)}")
        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")
