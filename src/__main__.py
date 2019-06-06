from cortex_client import InputMessage, OutputMessage
import requests
import urllib.parse
import json
from cortex import Message
from ibm_watson import ToneAnalyzerV3

def main(params):
    msg = Message(params)
    
    tone = msg.payload.get("tone")
    apikey = "OLaf6MvfIWA4l0vv95lq3061GuMaojMFYW1C_E0NmMeS"

    base_url = "https://gateway.watsonplatform.net/tone-analyzer/api"


    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey=apikey,
        url=base_url
    )


    tone_analysis = tone_analyzer.tone({'text': tone}, content_type='application/json').get_result()

    return Message.with_payload({'result':tone_analysis}).to_params()