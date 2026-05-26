import requests
import json

URL_PREDICT= 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'


def sentiment_analyzer(text_to_analyze):
  header= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
  myobj = { "raw_document": { "text": text_to_analyze } } 
  response = requests.post(URL_PREDICT, json = myobj, headers=header)
  formatted_response = json.loads(response.text)
  #print(formatted_response)
  label = formatted_response['documentSentiment']['label']
  score = formatted_response['documentSentiment']['score']

  return {'label': label, 'score': score}