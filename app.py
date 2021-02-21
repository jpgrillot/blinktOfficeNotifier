from flask import *
from blinkt import set_all, set_brightness, show, clear
import time

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/off')
def off():
    clear()
    show()
    return render_template('index.html')
@app.route('/video')
def video():
    set_all(255,0,0,brightness=0.1)
    show()
    return render_template('index.html')
@app.route('/meeting')
def meeting():
    set_all(255,255,0,brightness=0.1)
    show()
    return render_template('index.html')
@app.route('/working')
def working():
    set_all(0,255,0,brightness=0.1)
    show()
    return render_template('index.html')
@app.route('/done')
def done():
    set_all(0,0,255,brightness=0.1)
    show()
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)