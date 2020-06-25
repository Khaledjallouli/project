from flask import Flask
from flask_cors import CORS
import controller as c

app = Flask(__name__)
CORS(app)

#####
# START OF ROUTES SECTION
#####

@app.route('/soccerMatchesClassification', methods=['GET'])
def soccerMatchesClassification():
    return app.response_class(
        response=c.getSoccerMatchesClassification(),
        status=200,
        mimetype='application/json'
    )

@app.route('/soccerMatchesRegression', methods=['GET'])
def soccerMatchesRegression():
    return app.response_class(
        response=c.getSoccerMatchesRegression(),
        status=200,
        mimetype='application/json'
    )

@app.route('/fetchNewMatches', methods=['GET'])
def fetchNewMatches():
    return app.response_class(
        response=c.fetchNewMatches(),
        status=200,
        mimetype='application/json'
    )

@app.route('/retrainClassification', methods=['GET'])
def retrainClassification():
    return app.response_class(
        response=c.retrainClassification(),
        status=200,
        mimetype='application/json'
    )

@app.route('/retrainRegression', methods=['GET'])
def retrainRegression():
    return app.response_class(
        response=c.retrainRegression(),
        status=200,
        mimetype='application/json'
    )

#####
# END OF ROUTES SECTION
#####

# should probably stay at the end:
if __name__ == '__main__':
    app.run()
