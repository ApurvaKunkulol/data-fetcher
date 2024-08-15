import tasks

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Your Flask app is live!</p>"


@app.route("/fetch-data")
def fetch_data():
    """
    A function to fetch data from any external service like Shopify as mentioned in the test exercise.
    :return:
    A JSON containing all required values.
    """
    try:
        mock_data = tasks.get_mock_data()
        status = tasks.transform_data(mock_data)
        return status
    except Exception as ex:
        raise ex


@app.route("/fetch-processed-data")
def fetch_processed_data():
    """
    A function to fetch data from any external service like Shopify as mentioned in the test exercise.
    :return:
    A JSON containing all required values.
    """
    try:
        mock_data = tasks.fetch_processed_data()
        return mock_data
    except Exception as ex:
        raise ex

