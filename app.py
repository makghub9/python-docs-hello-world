from flask import Flask
from azure.storage. queue import QueueClient
from azure. identity import DefaultAzureCredential
processing_queue_name = "processing-queue"
connect_str = "DefaultEndpointsProtocol=https;AccountName=makstore;EndpointSuffix=core.windows.net"
# Using the managed identity of the App Service
credentials = DefaultAzureCredential()
app = Flask (__name__)

@app. route("/")
def index():

    # Create a queue client, using the application Azure AD credentials
    queue_client = Queuečlient.from_connection_string(connect_str, processing_queue_name, credential=credentials)
    # Peek at messages in the queue
    peeked_messages = queue_client.peek_messages (max_messages=5)

    html = """
   <!DOCTYPE html><html><body>
   <p>Hi students! Let's see the messages in the queue: </p>
   <ul>
   """
    for peeked_message in peeked_messages:
        html += "<li>" + peeked_message.content + "</li>"
