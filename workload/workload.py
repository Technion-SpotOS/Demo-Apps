import argparse
import sys
import time
import signal
import os

import requests

app_name_env_var = 'APP_NAME'
rest_server_env_var = 'REST_SERVER'

appname = os.environ.get(app_name_env_var, default='golem-workload')
rest_server = os.environ.get(rest_server_env_var, default='http://spotos-rest-logger-service.golem.svc.cluster.local:3000/logger')


def check_env_vars():
    if appname is None or rest_server is None:
        return False

    return True


def post_msg(msg):
    try:
        _ = requests.post(rest_server, data={
            'appName': appname,
            'msg': msg
        })
    except Exception as e:
        print('err posting message', e)


def termination_handler(signum, frame):
    post_msg('My time has come')
    sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple workload that POSTs to REST_SERVER upon initialization and death.")
    # register handler
    signal.signal(signal.SIGTERM, termination_handler)

    # check env vars
    if not check_env_vars():
        print('environment variables are not set, closing down')
        exit(1)

    print('started as', appname)

    # post initialization
    post_msg('I am alive')

    while True:
        time.sleep(10)
