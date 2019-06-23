dosya= open('faizHesaplama.txt','w')
anaPara = float(input("Lutfen Faiz Hesaplamasi Istediginiz Ana Para Miktraini Giriniz"))
yil = int(input("Lutfen Sureyi Yil Cinsinden Giriniz"))
faizOrani = float(input("Lutfen Yillik Faiz Oranini Giriniz"))
toplamFaiz = anaPara*yil*faizOrani/100
aylikFaiz =toplamFaiz/12
gunlukFaiz = toplamFaiz/365
toplamPara = toplamFaiz + anaPara
print("Toplam Faiz Tutari :",toplamFaiz,
	"Aylik Faiz Tutari : ", aylikFaiz,
	"Gunluk Ortalama Faiz Tutari :",gunlukFaiz,
	"Toplam Para Tutari :",toplamPara,sep="\n")
print("Toplam Faiz Tutari :",toplamFaiz,
	"Aylik Faiz Tutari : ", aylikFaiz,
	"Gunluk Ortalama Faiz Tutari :",gunlukFaiz,
	"Toplam Para Tutari :",toplamPara,sep="\n",file=dosya)
dosya.close()
