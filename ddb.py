import boto3
import pprint
from types import SimpleNamespace
import json

client = boto3.resource("dynamodb").meta.client


def get_event():
    pass


class comment:
    def __init__(self, pk, sk, type, content) -> None:
        self.pk = pk
        self.sk = sk
        self.type = type
        self.content = content

    def __str__(self):
        return "Comment says: " + self.content


class event:
    def __init__(self, pk, sk, type, content) -> None:
        self.pk = pk
        self.sk = sk
        self.type = type
        self.content = content

    def __str__(self):
        return "Event is: " + self.content


def get_event_details(eventId):
    """
    Returns the event and its corresponding comments
    """
    response = client.query(
        TableName="EventsSingleTable",
        # IndexName='',
        Select="ALL_ATTRIBUTES",
        KeyConditionExpression="pk = :pk",
        ExpressionAttributeValues={":pk": eventId},
    )

    items = response["Items"]

    for item in items:
        if item["sk"] == item["pk"]:
            e = event(**item)
            pprint.pprint(str(e))
        else:
            c = comment(**item)
            pprint.pprint(str(c))


if __name__ == "__main__":
    get_event_details("e#1")
