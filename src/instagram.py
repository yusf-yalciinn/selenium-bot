from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import json
import time
import os
import datetime
import os
#-------------------------------------------
class InstagramBot:
    def __init__(self):
        self.driver     =   webdriver.Chrome()

        with open("account.json", "r", encoding="UTF-8") as f:
            self.crude   =   json.load(f)

        self.action          =   webdriver.ActionChains(self.driver)

    def SignIn(self):
        self.driver.get("https://www.instagram.com/")
        
        time.sleep(2) #Wait...
        
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.crude["nickname"])
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.crude["password"])
        
        self.driver.maximize_window() #Full Screen
        
        time.sleep(2) #Wait...
        
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click() 
        
        time.sleep(3) #Wait...

    def SendFollow(self, user):
        time.sleep(3) #Wait...
        
        self.driver.get(f"https://www.instagram.com/{user}/")

        time.sleep(4) #Wait...
        
        butons   =   self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header').find_elements(By.TAG_NAME, "button")
        for buton in butons:
            if buton.text == "Takip Et":
                buton.click()

        time.sleep(8) #Wait...

    def SayHi(self, name):
        self.driver.get("https://www.instagram.com/direct/inbox/")
        
        time.sleep(5) #Wait...
        
        butons  =   self.driver.find_elements(By.TAG_NAME, "button")
        for buton in  butons:
            if buton.text == "Şimdi Değil":
                buton.click()
                
        time.sleep(2) #Wait...

        for div in self.driver.find_element(By.CSS_SELECTOR, "div.N9abW").find_elements(By.TAG_NAME, "div"):
            
            if div.text == name or div.text == (name + " (düzenlendi)"):
                div.click()
                            
                if 6 < datetime.datetime.now().time().hour <= 12:
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(f"Günaydın")

                    time.sleep(2) #Wait...
                    
                    self.action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                    
                    time.sleep(2) #Wait...
                    

                elif 12 < datetime.datetime.now().time().hour <=16:
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(f"İyi öğlenler")

                    time.sleep(2) #Wait...
                    
                    self.action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

                    time.sleep(2) #Wait...
                    

                elif datetime.datetime.now().time().hour > 16 or 0 <= datetime.datetime.now().time().hour <= 6:
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(f"İyi akşamlar")

                    time.sleep(2) #Wait...
                    
                    self.action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                    
                    time.sleep(2) #Wait...
             
                break

        else:
            try:
                self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
                self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(name)
                
                time.sleep(2) #Wait...
                
                self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button').click()
                
                time.sleep(2) #Wait...

                self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()

                time.sleep(2) #Wait...

                try:
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/button/div').click()

                except Exception:
                    pass
                
                time.sleep(2)
                
                if 6 < datetime.datetime.now().time().hour <= 12:
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(f"Günaydın")

                    time.sleep(2) #Wait...
                        
                    self.action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        
                    time.sleep(2) #Wait...
                        

                elif 12 < datetime.datetime.now().time().hour <=16:
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(f"İyi öğlenler")

                    time.sleep(2) #Wait...
                        
                    self.action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

                    time.sleep(2) #Wait...
                        

                elif datetime.datetime.now().time().hour > 16 or 0 <= datetime.datetime.now().time().hour <= 6:
                    self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(f"İyi akşamlar")

                    time.sleep(2) #Wait...
                        
                    self.action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        
                    time.sleep(2) #Wait...
                 

            except Exception:
                raise Exception("Undefined message box")

        
        self.driver.quit()

    def SaveFollowing(self, nickname):
        self.driver.get(f"https://www.instagram.com/{nickname}/")
        
        time.sleep(5) #Wait...
        
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        
        time.sleep(2) #Wait...
        
        dialog  =   self.driver.find_element(By.CSS_SELECTOR, 'div[role=dialog] ul')
        followerCount   =   dialog.find_elements(by=By.TAG_NAME, value="li")
        i   =   0
        while True:
            if i == 0:
                dialog.click()
            self.action.key_down(Keys.END).key_up(Keys.END).perform()
            
            time.sleep(2) #Wait...
            
            
            if i == 0:
                dialog.click()
            i+=1
            self.action.key_down(Keys.END).key_up(Keys.END).perform()
            
            time.sleep(4) #Wait...
            

            if len(followerCount) != len(dialog.find_elements(by=By.TAG_NAME, value="li")):
                followerCount = dialog.find_elements(by=By.TAG_NAME, value="li")
                continue
            
            else:
                if os.path.exists(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takip Ettikleri)"):
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takip Ettikleri).txt", "a", encoding="UTF-8") as f:
                        updateList  =   f.readlines()
                        updateSet   =   set(f.readlines().extend(followerCount))
                        if updateList == list(updateSet):
                            break
                        else:
                            pass
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takip Ettikleri).txt", "w", encoding="UTF-8") as f:
                        for user in updateSet:
                            f.write("- " + user.find_element(by=By.TAG_NAME, value="a").get_attribute("href")[26:-1] + "\n")
                            
                    time.sleep(2) #Wait...
                    
                    break
                
                else:
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takip Ettikleri).txt", "w", encoding="UTF-8") as f:
                        for user in followerCount:
                            f.write("- " + user.find_element(by=By.TAG_NAME, value="a").get_attribute("href")[26:-1] + "\n")
                            
                    time.sleep(2) #Wait...
                    
                    break
                
        self.driver.quit()

    def SaveFollower(self, nickname):
        self.driver.get(f"https://www.instagram.com/{nickname}/")
            
        time.sleep(5) #Wait...
            
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div').click()
            
        time.sleep(2) #Wait...
            
        dialog  =   self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]')
        followerCount   =   dialog.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span/span")
        print(followerCount)
        i   =   0
        while True:
            if i == 0:
                dialog.click()
            self.action.key_down(Keys.END).key_up(Keys.END).perform()
                
            time.sleep(2) #Wait...
                
                
            if i == 0:
                dialog.click()
            i+=1
            self.action.key_down(Keys.END).key_up(Keys.END).perform()
                
            time.sleep(4) #Wait...
                

            if len(followerCount) != len(dialog.find_elements(By.TAG_NAME, "li")):
                followerCount = dialog.find_elements(By.TAG_NAME, "li")
                continue
                
            else:
                if os.path.exists(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takipçileri)"):
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takipçileri).txt", "a", encoding="UTF-8") as f:
                        updateList  =   f.readlines()
                        updateSet   =   set(f.readlines().extend(followerCount))
                        if updateList == list(updateSet):
                            break
                        else:
                            pass
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takipçileri).txt", "w", encoding="UTF-8") as f:
                        for user in updateSet:
                            f.write("- " + user.find_element(By.TAG_NAME, "a").get_attribute("href")[26:-1] + "\n")
                                
                    time.sleep(2) #Wait...
                        
                    break
                    
                else:
                    with open(f"D:\\Applications with Python\\Konsol Uygulamaları\\Memati Yönetim\\Kayıtlar\\{nickname} (Takipçileri).txt", "w", encoding="UTF-8") as f:
                        for user in followerCount:
                            f.write("- " + user.find_element(By.TAG_NAME, "a").get_attribute("href")[26:-1] + "\n")
                                
                    time.sleep(2) #Wait...
                        
                    break
                    
        self.driver.quit()
