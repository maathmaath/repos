import slack

SLACK_API_TOKEN = "xoxb-52455058582-3552597451472-oqECf9n06tpNlV59hiOszswI"
#SLACK_API_TOKEN = "xoxb-52455058582-3541220060465-jFAcmqbKcgkDYJ2L5iXeC9D9"
#SLACK_API_TOKEN = "xoxb-52455058582-2295118049556-7U1xH5Cc30op3yy8RukFL6oT"
client = slack.WebClient(token=SLACK_API_TOKEN)
response = client.users_lookupByEmail(email="manjunathk@tekion.com")
slack_id = response['user']['id']
print(slack_id)
msg = "hello maath!!!"
slack_response = client.chat_postMessage(channel=slack_id, text=msg)
if slack_response["ok"]:
	print("Notification sent to Slack for user.")
else:
	print("Notification not sent.")
