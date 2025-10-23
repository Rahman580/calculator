sayi = int(input("sayi giriniz:\n"))

sayi2 = int(input("bir sayi daha giriniz:\n"))

op = input("operatör seçiniz:\n")
if op == '+':
    sonuc = sayi + sayi2
elif op == '-':
    sonuc = sayi - sayi2
elif op == '*':
    sonuc = sayi * sayi2
elif op == '/':
    sonuc = sayi / sayi2
print("sonuç:",sonuc )

