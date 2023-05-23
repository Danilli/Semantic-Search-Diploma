import requests
import user_query


def get_index(url="http://localhost:9200/", indeces_name="company_documents"):
    res = requests.get(url + indeces_name)
    return res.json()["company_documents"]


def get_doc(url="http://localhost:9200/", indeces_name="company_documents", doc_index="default_index"):
    res = requests.get(url + indeces_name + "/_doc/" + doc_index)
    return res.json()


def get_doc_by_title(url="http://localhost:9200/", indeces_name="company_documents", doc_name="default_name"):
    search_query = {
        "query": {
            "match": {
                "title.keyword": {
                    "query": doc_name
                }
            }
        }
    }
    try:
        res = requests.get(url + indeces_name + "/_search", json=search_query).json()["hits"]["hits"][0]
    except Exception as e:
        return f"CAN'T RESPONSE WITH ERROR:  {e}"
    return res


def create_elastic_response(user_resp: user_query.UserResponse, url="http://localhost:9200/", indeces_name="company_documents"):
    # elastic has no list type so the lists are converted into string for further query-push
    search_query = {
      "query": {
        "dis_max": {
          "queries": [
            {"match": {"text": user_resp["text"]}},
            {"match": {"topic": ' '.join(user_resp["topics"])}},
            {"match": {"key_words": ' '.join(user_resp["keywords"])}},
            {"match": {"named entityes": ' '.join(user_resp["names"]) if not user_resp["names"] else ""}}
          ],
          "tie_breaker": 0.3
        }
      }
    }
    try:
        res = requests.get(url + indeces_name + "/_search", json=search_query).json()["hits"]["hits"]
    except Exception as e:
        return f"CAN'T RESPONSE WITH ERROR:  {e}"
    if len(res) > 5:
        res = res[:5]
    return res
