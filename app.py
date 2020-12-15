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
  totalCost = total * int(value)
  totalCost = '{0:,}'.format(round(totalCost))

  return render_template("resultaat.html", value=value, totalcost=totalCost)

if __name__ == "__main__":
  app.run(debug=True)