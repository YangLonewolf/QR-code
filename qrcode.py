import pyqrcode
import png

print("""
QR CODE OLUŞTURUCUYA HOŞGELDİNİZ
""")

giriş = input("Linki Giriniz:")

qr = pyqrcode.create(giriş)
qr.svg("kod.svg",scale=8)
qr.svg("kod.eps",scale=8)
qr.png("kod.png",scale=8,module_color=(209,20,203,255))
print("QR CODE OLUŞTURULDU")
