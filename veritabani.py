import sqlite3 #sqlite3 dahil ettik

con=sqlite3.connect("kütüphane.db") #kütüphane databasemizi kurduk.
cursor = con.cursor()#imleç ekledik

def tablo_olustur():#tablo oluşturmak için gerekli kodları yazacağız.
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (İsim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_sayisi INT)")
    con.commit()#burda bağlantının işlenmesini sağladık.


def veriekle():
   cursor.execute("INSERT INTO kitaplik VALUES('Hayat Hikayem','Omer AKKOYUN','Tornado',323)")
   con.commit()

def veriekle2(isim,yazar,yayınevi,sayfa):
   cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa))
   con.commit()
   
print("Yazar kaydı yapmak için aşağıdaki bilgileri eksiksiz doldurun!")
isim=input("kitap ismi girin:")
yazar=input("yazar ismi girin:")
yayınevi=input("yayınevi ismi girin:")
sayfa=input("sayfa sayısını girin:")

#Buraya kadar olan kısım sadece veritabanı ayarları
    
veriekle2(isim,yazar,yayınevi,sayfa)#Fonksiyonumuzu burda çalıştırdık.
con.close()#bağlantıyı kapattık.
