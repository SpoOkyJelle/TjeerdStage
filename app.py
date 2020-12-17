import requests

from flask import Flask, render_template, request
app = Flask(__name__)

response = requests.get("https://api.hypixel.net/skyblock/bazaar")
if response.status_code != 404:
  erAPI = response.json()['products']['ENCHANTED_REDSTONE']['sell_summary'][0]['pricePerUnit']
  ecAPI = response.json()['products']['ENCHANTED_COBBLESTONE']['sell_summary'][0]['pricePerUnit']
  ecbAPI = response.json()['products']['ENCHANTED_COAL_BLOCK']['sell_summary'][0]['pricePerUnit']
  eiiAPI = response.json()['products']['ENCHANTED_IRON']['sell_summary'][0]['pricePerUnit']
  egAPI = response.json()['products']['ENCHANTED_GLOWSTONE_DUST']['sell_summary'][0]['pricePerUnit']
  
  lavaBucket = response.json()['products']['ENCHANTED_LAVA_BUCKET']['buy_summary'][0]['pricePerUnit']
  superCompacter = response.json()['products']['SUPER_COMPACTOR_3000']['buy_summary'][0]['pricePerUnit']
  redstoneLamp = response.json()['products']['ENCHANTED_REDSTONE_LAMP']['buy_summary'][0]['pricePerUnit']


    
else:
  print('Error!')

def lavabucketWinst(amount):
  return round(amount * (lavaBucket - ((ecbAPI * 2) + (eiiAPI * 3))) )

def supercompacterWinst(amount):
  return round(amount * (superCompacter - ((erAPI * 160) + (ecAPI * 448))) )

def redstoneLampWinst(amount):
  return round(amount * (redstoneLamp - ((erAPI * 128) + (egAPI * 32))) )
  



@app.route("/")
def hello():
  return render_template("index.html", 
  winstLavaBucket='{0:,}'.format(lavabucketWinst(1)),
  winstSuperCompacter='{0:,}'.format(supercompacterWinst(1)),
  winstRedstoneLamp='{0:,}'.format(redstoneLampWinst(1)),
  )  

@app.route("/verwerken_lava_bucket", methods=['post'])
def lavabucket():
  value = request.form['naam']

  EnchantedCoalBlockPrice = 2 * ecbAPI
  EnchantedIronPrice = 3 * eiiAPI

  ecbeiiTotalPrice = EnchantedCoalBlockPrice + EnchantedIronPrice
  lbA =  int(value) / ecbeiiTotalPrice
  lbA = round(lbA)

  ecbA = lbA * 2
  eiiA = lbA * 3
  
  return render_template(
    "lavabucket.html",
    ecbA='{0:,}'.format(round(ecbA)),
    eiiA=eiiA,
    LavaBucketW='{0:,}'.format(round( lavabucketWinst(int(lbA)) )),
    ecbAPI=ecbAPI,
    eiiAPI='{0:,}'.format(round(eiiA)),
    ecbeiiTotalPrice='{0:,}'.format(round(EnchantedCoalBlockPrice + EnchantedIronPrice)),
    EnchantedCoalBlockPrice='{0:,}'.format(round(EnchantedCoalBlockPrice)),
    EnchantedIronPrice='{0:,}'.format(round(EnchantedIronPrice)),
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
  SupercompacterW = '{0:,}'.format(round( supercompacterWinst(scA) ))
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
  RedstonelampW = '{0:,}'.format(round( redstoneLampWinst(rlA) ))
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


