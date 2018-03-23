import os
from dotenv import load_dotenv
import requests

""" API Constants """
GLOBAL_ID = "EBAY-DE"   # set for Ebay Marketplace in Germany
OPERATION_NAME = "findItemsAdvanced"
SERVICE_VERSION = "1.0.0"
RESPONSE_DATA_FORMAT = "XML"
BASEURL = "http://svcs.ebay.com/services/search/FindingService/v1"

""" load environment """
load_dotenv('.env')

def call(cfg):
    """ returns (if successful) api response as string """
    call_url = BASEURL+"?"+"OPERATION-NAME="+OPERATION_NAME+"&"+"SERVICE-VERSION="+SERVICE_VERSION+"&"+"SECURITY-APPNAME="+str(os.getenv("EBAY_APIKEY"))+"&"+"RESPONSE-DATA-FORMAT="+RESPONSE_DATA_FORMAT+"&"+"GLOBAL-ID="+GLOBAL_ID
    r = requests.post(call_url, data=cfg)
    if r.status_code != 200:
        print(r.text)
        raise Exception("API returned status code "+str(r.status_code))
    else:
        return r.text
