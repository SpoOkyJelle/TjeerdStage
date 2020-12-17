import random
import requests


# lava bucket berekenen
# nodig:
# 448 eCobble
# 160 eRedstone

response = requests.get("https://api.hypixel.net/skyblock/bazaar")
if response.status_code != 404:
    lavaBucket = response.json()['products']['SUPER_COMPACTOR_3000']['buy_summary'][0]['pricePerUnit']
    
    eCobble = response.json()['products']['ENCHANTED_COBBLESTONE']['sell_summary'][0]['pricePerUnit']
    eRedstone = response.json()['products']['ENCHANTED_REDSTONE']['sell_summary'][0]['pricePerUnit']
    
    totalCobble = eCobble * 448
    totalRedstone = eRedstone * 160
    
    totalCost = totalCobble + totalRedstone
    print(lavaBucket - totalCost)
  
  
  
  

# invoer = input('hoe veel TB??: ')


# def BiteToTB(invoer):
#     kilobite = invoer / 1024 
#     megabite = invoer / (kilobite / 1024) 
#     gigabite = invoer / (1024 / megabite)

#     print(kilobite,"kilobites") 
#     print(megabite,"megabites") 
#     print(gigabite,"gigabites")


# def TBtoBite(invoer):
#     gigabite = invoer * 1024 
#     megabite = invoer * (gigabite * 1000) 
#     bite = invoer * (1000000 * megabite)

#     print(gigabite,"gigabites") 
#     print(megabite,"megabites") 
#     print(bite,"bites")


# TBtoBite(int(invoer))
# BiteToTB(int(invoer))




# number = random.randint(1, 20)


# guessedNumber = input('Guess the number: ')

# if number == int(guessedNumber):
#     print("je hebt gelijk, het nummer was: ", number)
# else:
#     print('fout! Het nummer was: ', number)


# list = [ 'x', 'y' ,'z']

# list[0] = "appel"
# list[1] = "peer"
# list[2] = "aardappel"

# for x in list:
#     print(x)
    

# num1 = random.randint(1, 6)
# print("Random integer: ", num1)

# if num1 == 6:
#     print("goed bezig")    