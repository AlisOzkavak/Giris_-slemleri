print("""
    ******************************

    Kullanıcı Girişi Programı

    ******************************
    """)


sys_kullanici_adi = "admin"
sys_sifre = "admin"

giris_hakki = 3


while True:
    kullanici_adi = input("Kullanici Adi: ")
    sifre = input("Sifre: ")
    
    if (kullanici_adi != sys_kullanici_adi and sifre == sys_sifre):
        print("Kullanici Adi Hatalıdır !!!")
        print("Kalan Giriş Hakkınız:" , giris_hakki)
        giris_hakki -= 1

    elif (kullanici_adi == sys_kullanici_adi and sifre != sys_sifre):
        print("Şifre Hatalıdır !!!")
        print("Kalan Giriş Hakkınız:" , giris_hakki)
        giris_hakki -= 1

    elif (kullanici_adi != sys_kullanici_adi and sifre != sys_sifre):
        print("Kullanici Adi Ve Şifre Hatalıdır !!!")
        print("Kalan Giriş Hakkınız:" , giris_hakki)
        giris_hakki -= 1

    else:
        print("Başarıyla Giriş Yapıldı !!")
        break

    if (giris_hakki == 0 ):
        print("Giriş Hakkınız Bitti")
        break







    
