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
## Set Webhook URL
https://slack.com/apps/A0F7XDUAZ--incoming-webhook-?tab=more_info
- Add the "Webhook URL" obtained from the above site to /workspace/secret/secret.yml.
```yaml
SLACK_WEBHOOK_URL: 'https://hooks.slack.com/services/XXXXXXXXX/QQQQQQQQQQQQQQQQQQQ'
```
# Usage
- use_gpu_ids : GPU Index.
- sleep_time_sec : Time interval to check the GPU operation.
- job_name : Job name to be displayed when notifying Slack.
```Bash
python gpu_operation_check.py --use_gpu_ids="1,2,3,4,5,6,7" --sleep_time_sec=600 --job_name='job name'
```
