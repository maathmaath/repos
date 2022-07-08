import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

userAPI = "xoxe.xoxp-1-Mi0yLTUyNDU1MDU4NTgyLTI0MDg4MzQ5Mjg5NjMtMzUyODUzNTk4MDg5OS0zNTI1NjM2NTYzMjUzLWRiY2I2NGJhNWI0N2JhZmIxYWIwOTZhNjE0MDgxZDNjYTNmNmQ2MjU4NjAwYTVlM2I3OTViMDc0MWM3MTViNjY"
# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get(userAPI))
logger = logging.getLogger(__name__)
# ID of the channel you want to send the message to
channel_id = "C12345"

try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text="Hello maath!!!"
    )
    logger.info(result)

except SlackApiError as e:
    logger.error(f"Error posting message: {e}")
