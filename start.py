from selenium import webdriver
import requests,os,time,re
try:
    os.mkdir("accounts")
except OSError:
    print("")
welcome = """
|||||        Account-Scraper                 |||||

 ||||        Coded By : @Galerici             ||||

  
"""
print(welcome)
queryparameter = input("KeyWord(Steam,Spotify....) : ")
print("Scanning Process Starting")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://www.google.com/search?q=" + queryparameter +"+site:throwbin.io&num=100")
links = []
for asd in chrome.find_elements_by_class_name("r"):
    links.append(asd.find_elements_by_css_selector("*")[0].get_attribute("href"))
    print(asd.find_elements_by_css_selector("*")[0].get_attribute("href"))
chrome.quit()
print(links)
kaçıncıindirkayder = 0
savedtimestamp = time.time()
print("Accounts Saving")
os.mkdir("accounts/" + str(savedtimestamp))
for link in links:
    reallink = ""
    if str(link).startswith("https://throwbin.io"):
        reallink = str(link)[20:]
        asd = requests.get("https://api.throwbin.io/v1/paste/"+ reallink + "/download/").text
        open("accounts/"+str(savedtimestamp) + "/z" + str(kaçıncıindirkayder) + ".txt", 'a' , errors="ignore" , encoding="utf-8").write(str(asd))
        open("accounts/"+str(savedtimestamp) + "/ALL.txt", 'a', errors="ignore" , encoding="utf-8").write(asd + "\n")
    else:
        dsa = requests.get(link).text
        open("accounts/"+ str(savedtimestamp) + "/z" + str(kaçıncıindirkayder) + ".txt", 'a' , errors="ignore" , encoding="utf-8").write(str(dsa))
        open("accounts/"+str(savedtimestamp) + "/ALL.txt", 'a', errors="ignore" , encoding="utf-8").write(dsa + "\n")
    print(str(kaçıncıindirkayder + 1) + "/" + str(len(links)))
    kaçıncıindirkayder += 1
print("Accounts Saved")
print("Extracting Accounts")
croppeds = re.findall("\w{5,30}[@]?\w{1,10}[.]?\w{1,30}[:]\S+",open("accounts/"+str(savedtimestamp) + "/ALL.txt", 'r', errors="ignore" , encoding="utf-8").read())
kaçıncıkırpıldı = 0
croppeds = list(dict.fromkeys(croppeds))
for cropped in croppeds:
    open("accounts/" + str(savedtimestamp) + "/ALL(LikeCombo).txt", 'a', errors="ignore", encoding="utf-8").write(cropped + "\n")
    print(str(kaçıncıkırpıldı) + "/" + str(len(croppeds)))
    kaçıncıkırpıldı += 1
print("Process Done")
os.startfile(os.getcwd() + "\\accounts\\" + str(savedtimestamp) + "\\ALL(LikeCombo)")



