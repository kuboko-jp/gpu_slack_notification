import slackweb
import yaml

def notify_to_slack(push_txt:str):

    with open('secret/secret.yml') as f:
        SECRET = yaml.safe_load(f)

    slack = slackweb.Slack(url=SECRET['SLACK_WEBHOOK_URL'])
    slack.notify(text=push_txt)


if __name__ == '__main__':
    notify_to_slack(push_txt='Hello!')