from utils.nvidiasmi import get_gpu_info
from utils.slack_notification import notify_to_slack
from pprint import pprint
import time
import fire


def check_gpu_operation(gpus_n:int, sleep_time_sec:int, job_name:str, debug=False):
    before_gpu_utilizations_list = [0] * gpus_n
    while True:
        gpu_status = get_gpu_info()
        gpu_utilizations_list = [int(s['utilization.gpu']) for s in gpu_status]
        if debug:
            gpu_utilizations_list = [0] * gpus_n
        print('Checking ...')
        print('Before : ', before_gpu_utilizations_list)
        print('Now    : ', gpu_utilizations_list)
        match_count = 0
        for now_u, before_u in zip(gpu_utilizations_list, before_gpu_utilizations_list):
            if now_u == before_u:
                match_count += 1
        if match_count == gpus_n:
            push_txt = f"<{job_name}> has stopped."
            notify_to_slack(push_txt=push_txt)
        before_gpu_utilizations_list = gpu_utilizations_list
        time.sleep(sleep_time_sec)

def run(gpus_n=8, sleep_time_sec=300, job_name='Jukebox DGX-3', debug=False):
    setup_txt = f"Set parameters -> gpus_n:{gpus_n}, sleep_time_sec:{sleep_time_sec}, job_name:{job_name}, debug:{debug}"
    print(setup_txt)
    notify_to_slack(push_txt=setup_txt)
    check_gpu_operation(gpus_n=gpus_n, sleep_time_sec=sleep_time_sec, job_name=job_name, debug=debug)

if __name__ == '__main__':
    fire.Fire(run)
