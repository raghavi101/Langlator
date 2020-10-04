from flask import Flask, render_template, request, redirect, url_for, session,logging, flash
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

@app.route("/")
def home():
     return render_template("home.html")

@app.route("/translatelang", methods=["GET", "POST"])
def translatelang():
     
     if request.method == "POST":
          content = request.form.get("content")
          fromlang = request.form.get("fromlang")
          tolang = request.form.get("tolang")
          trans = Translator()
         
          t = trans.translate(str(content), src=str(fromlang), dest=str(tolang))
          x = f'Source: {t.src}'
          y = f'Destination: {t.dest}'
          finallang = f'{t.origin} -> {t.text}'
          return render_template("/display.html", finallang = finallang, fromlang=fromlang, tolang=tolang)
     else :
          return render_template("/translatelang.html")
          


@app.route("/languages")
def languages():
     return render_template("languages.html")

@app.route("/about")
def about():
     return render_template("about.html")

@app.route("/display")
def display():
     return render_template("display.html")
    



if __name__ == "__main__":
      app.run(debug = True)