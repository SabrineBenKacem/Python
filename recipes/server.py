from flask_app import app

# ! CONTROLLERS HERE
from flask_app.controllers import recipes, users


if __name__ == '__main__':
    app.run(debug=True, port=5505)