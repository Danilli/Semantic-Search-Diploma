from typing import TypedDict
from semantic_work import topic_modeling, take_ner


# create a user-type for ease
class UserResponse(TypedDict):
    text: str
    topics: list
    names: list
    keywords: list


def parse_user_sentence(sentence: str) -> UserResponse:
    """parsing the user's sentence into UserResponse type but keyword we got in the special way"""
    topics = topic_modeling.get_topics_of_doc(sentence)
    names = take_ner.get_ner(sentence)
    user_query: UserResponse = {"text":sentence,
                            "topics":topics,
                            "names":names,
                            "keywords":[]}
    return user_query


