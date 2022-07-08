from flask import Flask, request, make_response
from slack_sdk.webhook import WebhookClient
from aiohttp import web
import os
from slack_sdk.signature import SignatureVerifier
# signature_verifier = "6c658ef3969ee7dad077e999bea6401d"
signature_verifier = SignatureVerifier(
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
    )


app = Flask(__name__)


@app.route("/slack/events", methods=["POST"])
def slack_app():
    # request: web.Request) -> web.Response:
    # Verify incoming requests from Slack
    # https://api.slack.com/authentication/verifying-requests-from-slack
    if not signature_verifier.is_valid(
            body=request.get_data(),
            timestamp=request.headers.get("X-Slack-Request-Timestamp"),
            signature=request.headers.get("X-Slack-Signature")):
        return make_response("invalid request", 403)

    # Handle a slash command invocation
    if "command" in request.form \
            and request.form["command"] == "/reply-this":
        response_url = request.form["response_url"]
        text = request.form["text"]
        webhook = WebhookClient(response_url)
        # Send a reply in the channel
        response = webhook.send(text=f"You said '{text}'")
        # Acknowledge this request
        return make_response("", 200)
    return make_response("", 404)


if __name__ == "__main__":
    # app = web.Application()
    # app.add_routes([web.get("/", slack_app)])
    # e.g., http://localhost:3000/?text=foo&text=bar
    # web.run_app(app, host="0.0.0.0", port=3000)
    app.run()
