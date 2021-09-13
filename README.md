# gpu_notification
Send a notification to Slack when GPUs stop.

# SetUp
## Create Docker container
```Bash
git clone https://github.com/kubokoHappy/gpu_slack_notification.git
```
```Bash
cd gpu_slack_notification
```
```Bash
docker build -t gpu_slack_notification:latest .
```
```Bash
docker run -it --name gpu_slack_notification --gpus all gpu_slack_notification:latest
```
## Set Webhook URI
https://slack.com/apps/A0F7XDUAZ--incoming-webhook-?tab=more_info
- Add the "Webhook URL" obtained from the above site to /workspace/secret/secret.yml.
```yaml
SLACK_WEBHOOK_URL: 'https://hooks.slack.com/services/XXXXXXXXX/QQQQQQQQQQQQQQQQQQQ'
```
