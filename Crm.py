

def rehber():
    rehber_kisi_sayısı=0

    guide=[]
    degisken=0
    s=0

    while s==0 :

        import sqlite3
        con=sqlite3.connect("REHBERİM.db")
        cursor=con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS kişi_listesi(İSİM TEXT, TELEFON_NUMARASI INT)")
        
        con.commit()
        
        print("""
        Ajanda ve randevu işlemleri için :1
        Teklif ve Yönetim Sistemi için   :2
        Müşteri ve Yönetimi için         :3
        Aktivite Yönetimi için           :4
        Stok Yönetimi için               :5
        Satimi içi                       :6
        Ürün Yönetimi iış Yönetçin       :7
        Hatırlatıcı Mesajlar için        :8
        Raporlar için                    :9
            
            """)

        islem=int(input("Yapmak istediğiniz işlemin değerini giriniz:"))

        if islem==1:
            ad=input("Eklemek istediğiniz kişinin adı ve soyadını giriniz:")
            no=int(input("Eklemek istediğiniz kişinin numarasını giriniz:"))   
            cursor.execute("insert into kişi_listesi Values(?,?)",(ad,no))
            con.commit()
         
            # if len(guide)!=0 :
            #     sayac=0
            #     for i in guide:
            #         sayac+=1
            #         sayac2=0
            #         if(no==i[1]):
            #             print("Girdiğiniz numara daha önce rehbere eklenmiştir.")
            #             sayac2=58
            #             continue
            #         elif sayac==len(guide) and sayac2==0:
            #             guide=guide+[[ad,no]]
            #             degisken+=1
            #             print("Ekleme işlemi başarılı bir şekilde gerçekleştiriliyor...")
            # else:
            #     guide=guide+[[ad,no]]
            #     degisken+=1
            #     print("Ekleme işlemi başarılı bir şekilde gerçekleştiriliyor...")
            #     print("Rehbere {}:{} eklenmiştir.".format(ad,no))



        if islem==2:
        
            sil_no=int(input("Silmek istediğiniz kişinin numarasını giriniz:"))
            cursor.execute("Delete From kişi_listesi where TELEFON_NUMARASI=?",(sil_no,))
            con.commit() 

            # sayac3=0
            # if len(guide)!=0 :
            #     for x in guide:
            #         sayac3+=1
            #         if sil_no==x[1]:
            #             guide.remove(x)
            #             degisken-=1
            #             sayac3=58
            #             print("Silme işlemi başarılı bir şekilde gerçekleştiriliyor...")
            #             print("Rehberden {} numaralı kişi silinmiştir.".format(sil_no))
            #         else:
            #             print("Rehberde girilen numara bulunamadı.")



        if islem==3:

            cursor.execute("select * From kişi_listesi")
            liste=cursor.fetchall()
            for  i in liste:
                print(i) 

            deger=int(input("Numara ile arama yapmak için '1'e ; Ad ve soyad ile arama yapmak için '2'ye basınız..."))
            if(deger==1):
                deger2=int(input("Aramak istediğiniz kişinin numarasını giriniz:"))
                if len(guide)!=0:
                    sayac4=0
                    for q in guide:
                        sayac4+=1
                        if(deger2==q[1]):    
                            print("Aradığınız kişi= {}:{}".format(q[0],q[1]))
                            sayac4=58
                        elif(sayac4==len(guide)):
                            print("Numara bulunamadı...")
                else:
                    print("Rehberde kayıtlı kişi bulunmamaktadır.")    
            elif(deger==2):
                deger2=input("Aramak istediğiniz kişinin ad ve soyadını giriniz:")
                if len(guide)!=0:
                    sayac4=0
                    for q in guide:
                        sayac4+=1
                        if(deger2==q[0]):    
                            print("Aradığınız kişi= {}:{}".format(q[0],q[1]))
                            sayac4=58
                        elif(sayac4==len(guide)):
                            print("Numara bulunamadı...")
                else:
                    print("Rehberde kayıtlı kişi bulunmamaktadır.")   
            else :
                print("Yanlış numara girdiniz.") 



        if islem==4:  
            deger2=input("Girilmiş olan Ad ve soyadı giriniz: ")
            yeni_isim=input("Yeni isim ve soyisim giriniz:")
            cursor.execute(" Update  kişi_listesi set İSİM=? where İSİM=?",(yeni_isim,deger2))
            con.commit()

            
            # if(deger==1):
            #     deger2=int(input("Aramak istediğiniz kişinin numarasını giriniz:"))
            #     if len(guide)!=0:
            #         sayac4=0
            #         sayac5=0
            #         for q in guide:
            #             sayac4+=1
            #             if(deger2==q[1]):    
            #                 print("Düzenleme yapılacak kişi= {}:{}".format(q[0],q[1]))
            #                 deger2=input("isim ve soyisim giriniz: ")
            #                 yeni_no=int(input("Numara giriniz: "))
            #                 guide[sayac5]=[deger2,yeni_no]
            #                 sayac4=58
            #             elif(sayac4==len(guide)):
            #                 print("Numara bulunamadı...")
            #             sayac5+=1
            #     else:
            #         print("Rehberde kayıtlı kişi bulunmamaktadır.")       
            # if(deger==2):
            #     deger2=input("Ad ve soyad giriniz: ")
            #     if len(guide)!=0:
            #         sayac4=0
            #         sayac5=0
            #         for q in guide:
            #             sayac4+=1
            #             if(deger2==q[0]):    
            #                 print("Düzenleme yapılacak kişi= {}:{}".format(q[0],q[1]))
            #                 deger2=input("isim ve soyisim giriniz: ")
            #                 yeni_no=int(input("Numara giriniz: "))
            #                 guide[sayac5]=[deger2,yeni_no]
            #                 sayac4=58
            #             elif(sayac4==len(guide)):
            #                 print("Numara bulunamadı...")
            #             sayac5+=1
            #     else:
            #         print("Rehberde kayıtlı kişi bulunmamaktadır.") 


        if islem==5:
            rowsQuery = "SELECT COUNT(*) FROM kişi_listesi"
            cursor.execute(rowsQuery)
            numberOfRows = cursor.fetchone()[0]
            print(numberOfRows)

        if islem==6:
            print("Programdan çıkarsanız tüm veriler silinecektir.Programdan çıkmak istediğinizden emin misiniz?")
            sor=input("Çıkmak istiyorsanız 'E'ye devam etmek istiyorsanız 'H'ye basınız:")
            if sor=="E" :
                break
            else:
                continue

rehber()