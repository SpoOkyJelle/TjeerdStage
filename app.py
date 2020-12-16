import requests

from flask import Flask, render_template, request
app = Flask(__name__)

response = requests.get("https://api.hypixel.net/skyblock/bazaar")
if response.status_code != 404:
  er = response.json()['products']['ENCHANTED_REDSTONE']['quick_status']['buyPrice']
  ec = response.json()['products']['ENCHANTED_COBBLESTONE']['quick_status']['buyPrice']
    
else:
  print('Error!')


@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/verwerken", methods=['post'])
def doei():
  value = request.form['naam']


  err = 160 * er
  ecr = 448 * ec

  total = err + ecr
  totalCost =  int(value) / total
  totalCost = round(totalCost)
  winst = int(value) - ( totalCost * total ) 

  totalRedstone = totalCost * 160
  totalCobblestone = totalCost * 448
  
  totalPrice = '{0:,}'.format(round(err + ecr))
  winst = '{0:,}'.format(round(winst))
  totalCost = '{0:,}'.format(totalCost)
  totalRedstone = '{0:,}'.format(round(totalRedstone))
  totalCobblestone = '{0:,}'.format(round(totalCobblestone))
  err = '{0:,}'.format(round(err))
  ecr = '{0:,}'.format(round(ecr))
  

  return render_template(
    "resultaat.html",
    ec=ec, 
    er=er, 
    totalcost=totalCost, 
    winst=winst, 
    err=err, 
    ecr=ecr, 
    totalPrice=totalPrice,
    totalRedstone=totalRedstone,
    totalCobblestone=totalCobblestone,
  )

if __name__ == "__main__":
  app.run(debug=True)