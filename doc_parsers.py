import json
from semantic_work import topic_modeling, take_ner


def parse_json(file_absolute_path) -> dict:
    """convert json into dict with strict fields and add new"""
    with open(file_absolute_path, 'r') as f:
        # Read the content of the file
        content = f.read()
    # Parse the JSON content
    data = json.loads(content)

    data["topic"] = topic_modeling.get_topics_of_doc(data['text'])
    data["named entityes"] = take_ner.get_ner(data["text"])
    data["path"] = file_absolute_path
    return data


def parse_txt(file_absolute_path) -> dict:
    pass


def parse_pdf(file_absolute_path) -> dict:
    pass

