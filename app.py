from flask import Flask, render_template

from controllers.league_controller import league_blueprint
from controllers.match_controller import match_blueprint
from controllers.wrestler_controller import wrestler_blueprint



app = Flask(__name__)


app.register_blueprint(wrestler_blueprint)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()