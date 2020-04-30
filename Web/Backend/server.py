from flask import Flask
from flask_cors import CORS
import controller as c

app = Flask(__name__)
CORS(app)

#####
# START OF ROUTES SECTION
#####

@app.route('/')
def test():
    return "Hello World!"

@app.route('/soccerGames', methods=['GET'])
def soccerGamesOutput():
    return app.response_class(
        response=c.predict_soccerGame(),
        status=200,
        mimetype='application/json'
    )

#####
# END OF ROUTES SECTION
#####

# should probably stay at the end:
if __name__ == '__main__':
    app.run()
