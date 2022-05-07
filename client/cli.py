import requests
import datetime
import argparse

# ----------------------------------------------------------------------------
# send request to API function:
def send_request(path):
    endpoint = 'http://127.0.0.1:8000/api/post/'
    data = {'dateUpload': str(datetime.datetime.now())}
    print(data)
    post_request = requests.post(
        endpoint,
        json=data,
        files={"fileName": open(filePath, "rb")})

    if post_request.ok:
        print(post_request.status_code)
        print(post_request.text)
        print('file successfully  uploaded...')

    else:
        print(post_request)

# ---------------------------------------------------------------------------------------------
# set arguments for run CLI.PY  in coomand line :
parser = argparse.ArgumentParser(
    description='for Upload your file to API.',
    add_help=True)

parser.add_argument(
    "--upload",
    "-f",
    help='path of file you want it to upload.')

argument = parser.parse_args()
filePath = argument.upload
send_request(filePath)


