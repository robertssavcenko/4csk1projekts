from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["🍑 🍑 🍑 ", " 🍆💦", "👅", "im a freakkkkkkk lmaooo"]
    bildes = ["https://i.imgflip.com/83ag8h.jpg", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/89f56f15-6080-4550-995b-c78878611786/dgvms7a-53e31f7c-10fe-4f8b-b4b3-e524375a616d.jpg/v1/fill/w_865,h_924,q_70,strp/freak_meter_by_somerandomidklol_dgvms7a-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE1MyIsInBhdGgiOiJcL2ZcLzg5ZjU2ZjE1LTYwODAtNDU1MC05OTViLWM3ODg3ODYxMTc4NlwvZGd2bXM3YS01M2UzMWY3Yy0xMGZlLTRmOGItYjRiMy1lNTI0Mzc1YTYxNmQuanBnIiwid2lkdGgiOiI8PTEwODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.8WTol54YnFLdQ-EmxGStxaLeerPxcmtnCnydooTyKJQ", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyWcFNDirwEzXJSFmptl0j_Kl7IEREZBPy8nVr3ti4tA&s", "https://i.ytimg.com/vi/CWNYZlt4t_Y/maxresdefault.jpg"]
    kopejais_saraksts = [["🍑 🍑 🍑 ","https://i.imgflip.com/83ag8h.jpg"], [" 🍆💦", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/89f56f15-6080-4550-995b-c78878611786/dgvms7a-53e31f7c-10fe-4f8b-b4b3-e524375a616d.jpg/v1/fill/w_865,h_924,q_70,strp/freak_meter_by_somerandomidklol_dgvms7a-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTE1MyIsInBhdGgiOiJcL2ZcLzg5ZjU2ZjE1LTYwODAtNDU1MC05OTViLWM3ODg3ODYxMTc4NlwvZGd2bXM3YS01M2UzMWY3Yy0xMGZlLTRmOGItYjRiMy1lNTI0Mzc1YTYxNmQuanBnIiwid2lkdGgiOiI8PTEwODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.8WTol54YnFLdQ-EmxGStxaLeerPxcmtnCnydooTyKJQ", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyWcFNDirwEzXJSFmptl0j_Kl7IEREZBPy8nVr3ti4tA&s"]]
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts))

if __name__ == '__main__':
    app.run(port = 5000)

    print("Sveiki!")