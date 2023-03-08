from flask import Flask, render_template
from threading import Thread

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
  return "bot is up"

def run():
  app.run(
        host='0.0.0.0',
        port=6969
    )

def keep_alive():
    t = Thread(target=run)
    t.start()