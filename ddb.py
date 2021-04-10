import boto3
import pprint

# Let's try out the meta client https://twitter.com/jsaryer/status/1380593403705065486
client = boto3.resource("dynamodb").meta.client


def get_event():
    pass


class Comment:
    def __init__(self, pk, sk, type, content) -> None:
        self.pk = pk
        self.sk = sk
        self.type = type
        self.content = content

    def __str__(self):
        return "Comment says: " + self.content


class Event:
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

    # Try serializing multiple entities from a single request
    for item in items:
        if item["sk"] == item["pk"]:
            e = Event(**item)
            pprint.pprint(str(e))
        else:
            c = Comment(**item)
            pprint.pprint(str(c))


if __name__ == "__main__":
    get_event_details("e#1")
