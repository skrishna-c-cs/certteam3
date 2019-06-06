from cortex_client import InputMessage, OutputMessage

import requests 
import urllib.parse

def main(params):
    msg = InputMessage.from_params(params)
    
    tone = msg.payload.get(‘tone’)
    formatted_tone = urllib.parse.quote_plus(tone)
    
    base_url=”https://gateway.watsonplatform.net/tone-analyzer/api/{tone}”  
    
    validation_response = requests.get(base_url.format(tone=formatted_tone), headers={“X-Mashape- Key”:”OLaf6MvfIWA4l0vv95lq3061GuMaojMFYW1C_E0NmMeS”, “Accept”: “application/json”})
    
    return OutputMessage.create().with_type(‘cortex/Type’).with_payload(validation_response.json()).to_params()