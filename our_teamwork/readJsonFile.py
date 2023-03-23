import codecs
import json
import os.path

json_path = os.path.dirname(os.path.realpath(__file__)) + ""
json_file = 'new.json'

with open(json_file, encoding="utf8") as json_fileopen:
    json_data = json.load(json_fileopen)
    for article in json_data:
        article_text = article['article_title'][0] + "\n" + article['article_data'][0] + "\n\n"
        for i in range(len(article['article_author'])):
            article_text += article['article_author'][i] + "\n"
        article_text += "\n" + article['article_text']
        article_uuid = article['article_uuid']

        with codecs.open(json_path + "/sas_text_new/" + article_uuid + ".txt", "w", "utf-8-sig") as temp:
            temp.write(article_text)
