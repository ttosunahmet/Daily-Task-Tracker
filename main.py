import datetime

def dosyaya_yaz(tarih, hedef, takip):
    with open("daily_task.txt", "a") as f:
        f.write(tarih + " - " + hedef + " = " + takip + "\n")

x = datetime.datetime.now()
tarih = (x.strftime("%d.%m.%Y"))

cikis = True

while cikis:

    hedef = input("Merhaba Ahmet Hosgeldin. Bugunki Hedefin Nedir ? \n 1-Kitap Okumak \n 2-Spor Yapmak \n 3-İngilizce Çalışmak \n 4-Çıkış Yapmak\n Lütfen Menüden Secimini Yap.\n Seciminiz : ").lower()
    
    if hedef == "kitap" or hedef == "1":
        hedef = "Kitap Okumak"
        iscorrect = str(input(tarih + " - " + "Tarihli Kitap Okuma Görevinizi Tamamladınız Mı?\n e = evet | h = hayır \n Seçiminiz: ")).lower()
        if iscorrect == "e":
            takip = "tamamlandi"
        elif iscorrect == "h":
            takip = "tamamlanmadi"
        else:
            print("\nHatali Tuslama!\n e = evet | h = hayır\n")
            continue
        dosyaya_yaz(tarih, hedef, takip)

    elif hedef == "spor" or hedef == "2":
        hedef = "Spor Yapmak"
        iscorrect = str(input(tarih + " - " + "Tarihli Spor Yapma Görevinizi Tamamladınız Mı?\n e = evet | h = hayır \n Seçiminiz : ")).lower()
        if iscorrect == "e":
            takip = "tamamlandi"
        elif iscorrect == "h":
            takip = "tamamlanmadi"
        else:
            print("\nHatali Tuslama!\n e = evet | h = hayır\n")
            continue
        dosyaya_yaz(tarih, hedef, takip)
        
    elif hedef == "ingilizce" or hedef == "3":
        hedef = "İngilizce Çalışmak"
        iscorrect = str(input(tarih + " - " + "Tarihli İngilizce Çalışma Görevinizi Tamamladınız Mı?\n e = evet | h = hayır \n Seçiminiz : ")).lower()
        if iscorrect == "e":
            takip = "tamamlandi"
        elif iscorrect == "h":
            takip = "tamamlanmadi"
        else:
            print("\nHatali Tuslama!\n e = evet | h = hayır\n")
            continue
        dosyaya_yaz(tarih, hedef, takip)

    elif hedef == "q" or hedef == "4":
        cikis = False