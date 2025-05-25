import instagram
import time

while True:
    #Seçim Listesi
    choosing    =   []

    #Arayüz Başlığı
    print("\n"*30)
    title       =   " (@d.yener.16) Yönetimi ".center(70,"=")
    for char in title:
        print(char, end="")
        time.sleep(0.01)
    print("\n")

    #Arayüz Seçenekleri
    options     =   "Takipçi Listesi Çıkart -1".rjust(70) + "\n" + "Takip Edilen Listesi Çıkart -2".rjust(70) + "\n" + "Liste Üzerinden Takip İsteği At -3".rjust(70) + "\n" + "Yalnızca Giriş Yap -4".rjust(70) + "\n" + "SayHi -5".rjust(70) + "\n" + "Programı Kapat -6".rjust(70)
    print(options)

    #Arayüz Alt Boşluğu
    print("\n"*15)

    #Arayüz Girdisi
    choosing.append(input("Yukarıdaki Seçeneklerden Birini Giriniz: "))

    #Seçenek Alt Sınırı
    print("="*70)
    
    #Arayüz Girdi Kontrol...
    if choosing[0] == "6":
        print("\n- Programdan Çıkılıyor...")
        quit()

    else:

        if choosing[0] == "1":
            choosing.append(input("Kullanıcı Adı Giriniz: "))
            print("\n- İşlem Başlatılıyor...")
            memati  =   instagram.InstagramBot()
            memati.SignIn()
            memati.SaveFollower(choosing[1])
            """try:
                memati.SaveFollower(choosing[1])
            except Exception as hata:
                print("\n- Geçersiz Kullanıcı.", hata)
                memati.driver.quit()
                
            else:
                print("\n- İşlem Sona Erdi.")"""
                
            continue

        elif choosing[0] == "2":
            choosing.append(input("Kullanıcı Adı Giriniz: "))
            print("\n- İşlem Başlatılıyor...")
            memati  =   instagram.InstagramBot()
            memati.SignIn()
            try:
                memati.SaveFollowing(choosing[1])

            except Exception as a:
                print("\n- Geçersiz Kullanıcı.", a)
                memati.driver.quit()
                
            else:
                print("\n- İşlem Sona Erdi.")
                
            continue

        elif choosing[0] == "3":
            choosing.append(input("Kullanıcı Adı Giriniz: "))
            choosing.append(input("Takip Edilen veya Takipçi Listesi? (following/follower) "))
            print("\n- İşlem Başlatılıyor...")
            
            
            if choosing[2].lower() == "follower":
                try:
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\memobas505 (Takip Ettikleri).txt", "r", encoding="UTF-8") as f:
                        list1   =   f.readlines()
                    
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{choosing[1]} (Takipçileri).txt", "r", encoding="UTF-8") as f:
                        list2   =   f.readlines()

                    for already in list1:
                        try:
                            list2.remove(already)
                        except ValueError:
                            continue
                    memati  =   instagram.InstagramBot()
                    memati.SignIn()
                    firstTime   =   time.time()
                    print("Yükleniyor...")
                    for user in list2:
                        memati.SendFollow(user.strip("\n- "))
                        loading =   ((list2.index(user) + 1) / len(list2)) * 100
                        print("% {:.2f} ({}/{})".format(loading, (list2.index(user) + 1), len(list2)))
                    lastTime    =   time.time()
                    print(f"\n- İşlem Süresi: {lastTime - firstTime}")
                    
                except FileNotFoundError:
                    print("Kayıtlı Olmayan Kullanıcı!")
                

            elif choosing[2].lower() == "following":
                try:
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\memobas505 (Takip Ettikleri).txt", "r", encoding="UTF-8") as f:
                        list1   =   f.readlines()
                    
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{choosing[1]} (Takip Ettikleri).txt", "r", encoding="UTF-8") as f:
                        list2   =   f.readlines()

                    for already in list1:
                        try:
                            list2.remove(already)
                        except ValueError:
                            continue
                    memati  =   instagram.InstagramBot()
                    memati.SignIn()
                    firstTime   =   time.time()
                    for user in list2:
                        memati.SendFollow(user.strip("\n- "))
                        loading =   ((list2.index(user) + 1) / len(list2)) * 100
                        print("% {:.2f} ({}/{})".format(loading, (list2.index(user) + 1), len(list2)))
                    lastTime    =   time.time()
                    print(f"\n- İşlem Süresi: {lastTime - firstTime}")
                except FileNotFoundError:
                    print("Kayıtlı Olmayan Kullanıcı!")

            else:
                print("\n- Yanlış Seçenek")

            print("\n- İşlem Sona Erdi.")
            continue

        elif choosing[0] == "4":
            print("\n- İşlem Başlatılıyor...")
            memati  =   instagram.InstagramBot()
            memati.SignIn()
            time.sleep(10)
            print("\n- İşlem Sona Erdi.")
            continue

        elif choosing[0] == "5":
            choosing.append(input("Selam Göndermek İstediğiniz Hedef: "))
            print("\n- İşlem Başlatılıyor...")
            memati  =   instagram.InstagramBot()
            memati.SignIn()
            try:
                memati.SayHi(choosing[1].strip())

            except Exception:
                print("\n- Geçersiz Kullanıcı Adı.")
                memati.driver.quit()

            else:
                print("\n- İşlem Sona Erdi.")
                
            continue

        else:
            print("\n- Yanlış Seçenek")
            continue
