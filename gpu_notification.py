import slackweb

slack = slackweb.Slack(url="コピーしたWebhookのURL")
slack.notify(text="pythonからslackさんへ")