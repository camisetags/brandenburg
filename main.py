import base64
from typing import Dict
from brandenburg.services.marketing import MarketingService
from google.cloud.functions.context import Context


def salesforce(event: Dict[str, str], context: Context):
    """
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.

    param: event["data"]
    param: event["attibutes"]

    context 	The context object for the event.
    context.event_id 	A unique ID for the event. For example: "70172329041928".
    context.timestamp 	The date/time this event was created. For example: "2018-04-09T07:56:12.975Z".
    context.event_type 	The type of the event. For example: "google.pubsub.topic.publish".
    context.resource 	The resource that emitted the event.
    """
    MarketingService.execute(event, context)


def sms(event, context):
    pass


def email(event, context):
    pass


def whatsapp(event, context):
    pass


# if __name__ == "__main__":
#     salesforce({"data": "MTIz"}, "")
