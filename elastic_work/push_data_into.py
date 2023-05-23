from elasticsearch import Elasticsearch
import doc_parsers
import requests
import os


def init_es(host="localhost", port=9200, index="company_documents"):
    es = Elasticsearch([{'host': host, 'port': port, 'scheme': "http"}])
    mapping = {
        "mappings": {
            "title": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "text": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "key_words": {
                "type": "keyword"
            },
        }
    }
    es.indices.create(index=index, body=mapping, ignore=400)
    return es


def post_elastic(data, doc_name="default_name", url="http://localhost:9200", index_name="company_documents"):
    if type(data) is not dict:
        return "BAD WAY"
    response = requests.put(f"{url}/{index_name}/_doc/{doc_name}?pretty", json=data)
    return response.json()


def push_data(file_absolute_path: str, **kwargs):
    """func take an absolute_path, parse file and push to elastic. Or return a message. Not threw an exception"""
    doc_name = file_absolute_path.split("\\")[-1].split(".")[0]
    if file_absolute_path[-5:] == ".json":
        data = doc_parsers.parse_json(file_absolute_path)
    elif file_absolute_path[-4:] == ".txt":
        data = doc_parsers.parse_txt(file_absolute_path)
    elif file_absolute_path[-4:] == ".pdf":
        data = doc_parsers.parse_pdf(file_absolute_path)
    else:
        return f"UNACCEPTABLE!!! for {file_absolute_path}"
    data.update(kwargs)
    return post_elastic(data, doc_name=doc_name)


def push_data_from_folder(folder_path: str) -> list:
    """for each document in folder"""
    docs_list = os.listdir(folder_path)
    res = []
    try:
        for file_name in docs_list:
            res.append(push_data(os.path.join(folder_path, file_name)))
    except EOFError as e:
        res.append(e.__str__() + " for " + folder_path)
    return res
