from flask import Flask, request, jsonify
from model.model import insertStringIntoDb

app = Flask(__name__)

# POST endpoint
@app.route('/submitString', methods=['POST'])
def submitString():
    try:
        data = request.json # Access JSON data from the POST request ("data" is the single string)

        print('Received stiring: ', data, flush=True)

        insertStringIntoDb(data)

        response_data = {"message": "Data received and processed successfully"}
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({"error": str(e)})

# GET endpoint
@app.route('/data', methods=['GET'])
def get_data():
    data = {"key": "value"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
