from utils.nvidiasmi import get_gpu_info
from utils.slack_notification import notify_to_slack
from pprint import pprint
import time
import fire
import re


def check_gpu_operation(use_gpu_ids:list, sleep_time_sec:int, job_name:str, debug=False):
    print(use_gpu_ids)
    gpus_n = len(use_gpu_ids)
    before_gpu_utilizations_list = [0] * gpus_n
    while True:
        gpu_status = get_gpu_info()
        gpu_utilizations_list = [int(s['utilization.gpu']) for s in gpu_status if int(s['index']) in use_gpu_ids]
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

def run(use_gpu_ids="0,1,2,3,4,5,6,7", sleep_time_sec=300, job_name='Jukebox DGX-3', debug=False):
    use_gpu_ids = str(use_gpu_ids).split(',')
    use_gpu_ids = [int(re.sub('[() ]', '', s)) for s in use_gpu_ids]
    setup_txt = f"Set parameters -> gpus_n:{use_gpu_ids}, sleep_time_sec:{sleep_time_sec}, job_name:{job_name}, debug:{debug}"
    print(setup_txt)
    notify_to_slack(push_txt=setup_txt)
    check_gpu_operation(use_gpu_ids=use_gpu_ids, sleep_time_sec=sleep_time_sec, job_name=job_name, debug=debug)

if __name__ == '__main__':
    fire.Fire(run)
