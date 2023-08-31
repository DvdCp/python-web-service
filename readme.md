# Flask Web Service for Receiving and Querying Strings

This is a Flask web service written in Python that provides endpoints for receiving and querying strings. It includes a POST endpoint to submit strings, a GET endpoint to retrieve data, and a default route for searching for strings in a database.

## Prerequisites

Before you begin, make sure you have the following dependencies installed:

- Python
- Flask
- Your choice of database library (for the database operations in `model/model.py`)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/DvdCp/python-web-service.git
   ```

## Usage with Docker

1. Navigate to `python-web-service` folder and run:

```bash
docker-compose up --build --remove-orphans --force-recreate
```

This will build the desired image starting from `docker-compose.yml`. Note that this line will also create a custom network that will be used by other services.
This will start the Flask web service on `http://python-web-service:5000/` by default. You can access the endpoints from this URL.

## Endpoints

### Submit String (`POST /submitString`)

This endpoint allows you to submit a string to the web service, which will then insert it into the database. The data should be sent as JSON in the request body.

Example POST request:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"data": "your_string_here"}' http://python-web-service:5000/submitString
```

### Get Data (`GET /data`)

This endpoint returns a sample JSON response. You can customize it to return any data you need.

Example GET request:

```bash
curl http://python-web-service:5000/data
```

### Search for String (`GET /`)

This endpoint allows you to search for a string in the database. You need to provide the `string` parameter in the query string.

Example GET request:

```bash
curl http://python-web-service:5000/?string=your_search_string
```

## Error Handling

The web service includes error handling for HTTP exceptions. If an error occurs, it will return a JSON response with details about the error.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions, enhancements, or bug fixes.

---

**Note:** Make sure to customize the project details as needed and configure your database operations in `model/model.py`.
