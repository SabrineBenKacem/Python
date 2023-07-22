from flask import Flask, render_template

app = Flask(__name__)                     
    
@app.route('/play')
def play_box():
    return render_template("index.html")

@app.route('/play/<int:number>')
def count_box(number):
    return render_template("index.html", number = number)

@app.route('/play/<int:number>/<url_color>')
def colored_box(number, url_color):
    return render_template("index.html", number = number, color = url_color)

    
if __name__=="__main__":
    app.run(debug=True, port=5500) 