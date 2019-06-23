dosya = open('aylikMasraf.txt','w')
aylikGelir = float(input("Lutfen Aylik Gelirinizi Giriniz."))
mutfak = float(input("Lutfen Aylik Mutfak Harcamanizi Giriniz."))
egitim = float(input("Lutfen Aylik Egitim Harcamanizi Giriniz."))
giyim = float(input("Lutfen Aylik Giyim Harcamanizi Giriniz."))
ulasim =float(input("Lutfen Aylik Ulasim Harcamanizi Giriniz."))
toplamMasraf = mutfak + egitim + giyim + ulasim
gelireOran = (toplamMasraf/aylikGelir)*100
print("Aylik Toplam Masrafiniz:",toplamMasraf,"olarak hesaplanmis ve bu masraflarinizin\n"
	"aylik gelirnizie orani: %",gelireOran,"olarak bulunmustur.")
print("Aylik Toplam Masrafiniz:",toplamMasraf,"olarak hesaplanmis ve bu masraflarinizin\n"
	"aylik gelirnizie orani: %",gelireOran,"olarak bulunmustur.",file=dosya)
dosya.close()
