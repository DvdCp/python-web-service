import json
from flask import Flask, request, jsonify, abort
from werkzeug.exceptions import HTTPException
from model.model import insertStringIntoDb, selectStringFromDb

app = Flask(__name__)

# POST endpoint
@app.route('/submitString', methods=['POST'])
def submitString():
    
    data = request.json 

    print('INFO: Received stiring: ', data, flush=True)

    insertStringIntoDb(data)

    return 'OK', 201       
    
# GET endpoint
@app.route('/data', methods=['GET'])
def get_data():
    data = {"key": "value"}
    return jsonify(data)

@app.route('/', methods=['GET'])
def getString():

    stringToSearch = request.args.get('string')
    print('INFO: Searching {} from DB'.format(stringToSearch), flush=True)
    res = selectStringFromDb(stringToSearch)

    if (len(res) == 0):
        abort(404, 'Not Found')

    return jsonify(json.dumps(res));
        
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
