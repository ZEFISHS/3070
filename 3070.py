import time
from selenium import webdriver

browser = webdriver.Chrome('/Users/cheh3/HACK/Raid Protect/.env/chromedriver')

#rtx 3070
browser.get("https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-gaming-oc-8gb-gddr6-pci-express-4-0-graphics-card/6437909.p?skuId=6437909")

#pc achetable (cela sert de test quand vous voulez voir si le bot marche il suffit de enlevez le # et si il marche il l'ajoutera) 
#browser.get("https://www.bestbuy.com/site/cyberpowerpc-gamer-xtreme-gaming-desktop-intel-core-i5-10600kf-8gb-memory-nvidia-geforce-gtx-1660-super-1tb-hdd-240gb-ssd-black/6430869.p?skuId=6430869")


buyButton = False

while not buyButton:

    try:
        test = input("Blocage Tapez oui pour continuer : ") #cette ligne ne sert que a bloquer le systeme car quand le bot va ouvrir la page chrome ou de votre navigateur vous devrai avoir choisi votre pays et quand vous avez fini tapez oui ou aytre chose ca marchera comme meme
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")


        print("Bouton n'est pas prêt")


        time.sleep(1)
        browser.refresh()

    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
        print("Bouton a été cliqué")
        addToCartBtn.click()
        buyButton = True
