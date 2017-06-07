import requests
def lambda_handler(event, context):
    return str(requests.__version__)
