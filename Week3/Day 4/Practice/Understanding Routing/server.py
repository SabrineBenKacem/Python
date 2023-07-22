from flask import Flask  
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')          
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')          
def say_name(name):
    return "Hi, " + name
@app.route('/repeat/<int:num>/<string>')
def repeat_string(num, string):
    

    return num * string 

if __name__=="__main__":       
    app.run(debug=True)    

