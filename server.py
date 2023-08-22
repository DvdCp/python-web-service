from flask import Flask, request, jsonify

app = Flask(__name__)

# POST endpoint
@app.route('/submitString', methods=['POST'])
def submitString():
    try:
        data = request.json  # Access JSON data from the POST request ("data" is the single string)
        asciiValue = 0

        # Calculatinf ASCII value for the received string 
        for char in data:
            asciiValue += ord(char)

        print('Received stiring: ', data)
        print('ASCII decimal value: ', asciiValue, '\n\n')
        
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
    app.run()
