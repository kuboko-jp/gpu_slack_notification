# gpu_notification
Send a notification to Slack when GPUs stop.

# SetUp
```Bash
git clone https://github.com/kubokoHappy/gpu_slack_notification.git

cd gpu_slack_notification

docker build -t gpu_slack_notification:latest ./environment

docker run -it --name gpu_slack_notification --gpus all -v $(pwd):/workspace gpu_slack_notification:latest
```
