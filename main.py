<<<<<<< HEAD
pyhton -m pip install Flask

from flask import Flask
=======

from flask import Flask, render_template
>>>>>>> 2f7458e63bfeacd00c16db35107c41979c8bac2f

app = Flask(__name__)

@app.route("/")
def index():
<<<<<<< HEAD
    return "sveiki"

if __name__ == '__main__':
app.run(port = 5000)

print("sveiki")
=======
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("teksts.html")

if __name__ == '__main__':
    app.run(port=5000)

    print ("sveiki")
>>>>>>> 2f7458e63bfeacd00c16db35107c41979c8bac2f
