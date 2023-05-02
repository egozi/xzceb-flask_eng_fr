# import json
# from re import U
""" translation script """ 
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2019-04-30',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ translate from english to french"""
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ translate from french to english"""
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text

# if __name__ == '__main__':
#     res = englishToFrench("hello")
#     # res_str = res['translations'][0]['translation']
#     print(res)
#     res = frenchToEnglish(res)
#     print(res)
#     # languages = language_translator.list_languages().get_result()
#     # print(languages)
