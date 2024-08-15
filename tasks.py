import json
import pdb


def get_mock_data():
    """
    A function to fetch all JSON data.
    :return: JSON containing all
    """
    try:
        # pdb.set_trace()
        mock_data = {}
        with open("mock_data.json") as f:
            mock_data = json.loads(f.read())
        return mock_data

    except Exception as ex:
        raise  ex


def transform_data(api_data=None):
    """
    This function does sample transformation of API data of the
    :param api_data: JSON structure containing data obtained from APIs like Shopify
    :return:
        Processed JSON containing filtered quantities required by user.
    """
    try:
        # pdb.set_trace()
        available_titles = []
        if api_data:
            product = api_data.get("products")
            for itm in product:
                available_titles.append(itm.get("title"))
            output = {
                "available_titles": available_titles
            }
            with open("processed_data.json", "w") as f:
                json.dump(output, f, ensure_ascii=False, indent=4)
            return {
                "status": True,
                "message": "Processed data written to output file."
            }
        else:
            return {
                "status": False,
                "message": "Empty API data received."
            }
    except Exception as ex:
        raise ex

def fetch_processed_data():
    """
    A function to fetch all JSON data.
    :return: JSON containing all
    """
    try:
        # pdb.set_trace()
        processed_data = {}
        with open("processed_data.json") as f:
            processed_data = json.loads(f.read())
        return processed_data

    except Exception as ex:
        raise  ex
