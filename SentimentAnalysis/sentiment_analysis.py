'''
Functions intended for sentiment analysis
'''

import json
import requests

URL_PREDICT= (
    "https://sn-watson-sentiment-bert.labs.skills.network/v1"
    "/watson.runtime.nlp.v1/NlpService/SentimentPredict" )

def sentiment_analyzer(text_to_analyze):
    '''
    Obtains the label and the respective score of the prominent sentiment
    retrieving them in the output dictionary.
    '''
    header= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL_PREDICT, json = myobj, headers=header, timeout=5)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = None
        score = None

    return {'label': label, 'score': score}
    