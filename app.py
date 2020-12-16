import requests

from flask import Flask, render_template, request
app = Flask(__name__)

response = requests.get("https://api.hypixel.net/skyblock/bazaar")
if response.status_code != 404:
  erAPI = response.json()['products']['ENCHANTED_REDSTONE']['quick_status']['buyPrice']
  ecAPI = response.json()['products']['ENCHANTED_COBBLESTONE']['quick_status']['buyPrice']
  ecbAPI = response.json()['products']['ENCHANTED_COAL_BLOCK']['quick_status']['buyPrice']
  eiiAPI = response.json()['products']['ENCHANTED_IRON']['quick_status']['buyPrice']
  egAPI = response.json()['products']['ENCHANTED_GLOWSTONE_DUST']['quick_status']['buyPrice']

    
else:
  print('Error!')


@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/verwerken_lava_bucket", methods=['post'])
def lavabucket():
  value = request.form['naam']

  EnchantedCoalBlockPrice = 2 * ecbAPI
  EnchantedIronPrice = 3 * eiiAPI

  ecbeiiTotalPrice = EnchantedCoalBlockPrice + EnchantedIronPrice
  lbA =  int(value) / ecbeiiTotalPrice
  lbA = round(lbA)
  LavaBucketW = int(value) - ( lbA * ecbeiiTotalPrice ) 

  ecbA = lbA * 2
  eiiA = lbA * 3
  
  ecbeiiTotalPrice = '{0:,}'.format(round(EnchantedCoalBlockPrice + EnchantedIronPrice))
  LavaBucketW = '{0:,}'.format(round(LavaBucketW))
  lbA = '{0:,}'.format(lbA)
  ecbA = '{0:,}'.format(round(ecbA))
  eiiA = '{0:,}'.format(round(eiiA))
  EnchantedCoalBlockPrice = '{0:,}'.format(round(EnchantedCoalBlockPrice))
  EnchantedIronPrice = '{0:,}'.format(round(EnchantedIronPrice))

  return render_template(
    "lavabucket.html",
    ecbA=ecbA,
    eiiA=eiiA,
    LavaBucketW=LavaBucketW,
    ecbAPI=ecbAPI,
    eiiAPI=eiiAPI,
    ecbeiiTotalPrice=ecbeiiTotalPrice,
    EnchantedCoalBlockPrice=EnchantedCoalBlockPrice,
    EnchantedIronPrice=EnchantedIronPrice,
    lbA=lbA,

    )



@app.route("/verwerken_super_compacter_3000", methods=['post'])
def compacter3000():
  value = request.form['naam']


  EnchantedRedstonePrice = 160 * erAPI
  EnchantedCobblestonePrice = 448 * ecAPI

  ecerTotal = EnchantedRedstonePrice + EnchantedCobblestonePrice
  scA =  int(value) / ecerTotal
  scA = round(scA)
  SupercompacterW = int(value) - ( scA * ecerTotal ) 

  erA = scA * 160
  ecA = scA * 448
  
  ecerTotalPrice = '{0:,}'.format(round(EnchantedRedstonePrice + EnchantedCobblestonePrice))
  SupercompacterW = '{0:,}'.format(round(SupercompacterW))
  scA = '{0:,}'.format(scA)
  erA = '{0:,}'.format(round(erA))
  ecA = '{0:,}'.format(round(ecA))
  EnchantedRedstonePrice = '{0:,}'.format(round(EnchantedRedstonePrice))
  EnchantedCobblestonePrice = '{0:,}'.format(round(EnchantedCobblestonePrice))
  

  return render_template(
    "supercompacter.html",
    ecAPI=ecAPI, 
    erAPI=erAPI, 
    scA=scA, 
    SupercompacterW=SupercompacterW, 
    EnchantedRedstonePrice=EnchantedRedstonePrice, 
    EnchantedCobblestonePrice=EnchantedCobblestonePrice, 
    ecerTotalPrice=ecerTotalPrice,
    erA=erA,
    ecA=ecA,
  )


@app.route("/verwerken_redstone_lamp", methods=['post'])
def Redstonelamp():

  value = request.form['naam']

  EnchantedRedstone = 128 * erAPI
  EnchantedGlowstone = 32 * egAPI

  eregTotalPrice = EnchantedRedstone + EnchantedGlowstone
  rlA =  int(value) / eregTotalPrice
  rlA = round(rlA)
  RedstonelampW = int(value) - ( rlA * eregTotalPrice ) 

  erA = rlA * 128
  egA = rlA * 32
  
  eregTotalPrice = '{0:,}'.format(round(EnchantedRedstone + EnchantedGlowstone))
  RedstonelampW = '{0:,}'.format(round(RedstonelampW))
  rlA = '{0:,}'.format(rlA)
  erA = '{0:,}'.format(round(erA))
  egA = '{0:,}'.format(round(egA))
  EnchantedRedstone = '{0:,}'.format(round(EnchantedRedstone))
  EnchantedGlowstone = '{0:,}'.format(round(EnchantedGlowstone))

  return render_template(
    "redstonelamp.html",
    eregTotalPrice=eregTotalPrice,
    rlA=rlA,
    erA=erA,
    egA=egA,
    RedstonelampW=RedstonelampW,
    EnchantedRedstone=EnchantedRedstone,
    EnchantedGlowstone=EnchantedGlowstone,
    erAPI=erAPI,
    egAPI=egAPI,
    )

if __name__ == "__main__":
  app.run(debug=True)


