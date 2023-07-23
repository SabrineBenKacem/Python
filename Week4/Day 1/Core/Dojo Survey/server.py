from flask import Flask , render_template, request, redirect, session

app  = Flask(__name__)
app.secret_key = "aknftehdl"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
     session['username'] = request.form['username']
     session['location'] = request.form['location']
     session['fav_lang'] = request.form['fav_lang']
     session['comment'] = request.form['comment']
     return redirect('/result')



@app.route('/result')
def result():
    
    return render_template("result.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/result')










if __name__ =='__main__':
    app.run(debug = True, port=5003)