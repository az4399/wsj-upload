import requests


def get_token():
    headers = {
        'Authorization': 'Basic MDA1YTlkODI1MzkxODVlMDAwMDAwMDAxNzpLMDA1NW5aQ2dtYmszTSszTG4yWE9KbFpRVkVZQ1Nr'
    }
    token = \
        requests.request("GET", "https://api.backblazeb2.com/b2api/v3/b2_authorize_account", headers=headers).json()[
            "authorizationToken"]
    print("获取到了token")
    print(token)
    return token


def get_up_url(token):
    payload = "{\"bucketId\": \"8a992d78c245d3b99118051e\"}"
    headers = {
        'Authorization': str(token),
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", "https://api005.backblazeb2.com/b2api/v3/b2_get_upload_url", headers=headers,
                                data=payload).json()

    up_token = response["authorizationToken"]
    up_url = response["uploadUrl"]
    print("获取到了up_url和up_token")
    print(up_token, up_url)
    return up_token, up_url


def upload(up_token, up_url, file_name):
    headers = {
        'Authorization': str(up_token),
        'X-Bz-File-Name': file_name,
        'Content-Type': 'application/pdf',
        'X-Bz-Content-Sha1': 'do_not_verify',
        'X-Bz-Info-Author': 'unknown',
    }
    print("开始上传")
    requests.request("POST", up_url, headers=headers, data=open(file_name, 'rb').read())
    print("上传完成")


def run(file_path):
    file_name = file_path.split("/")[-1]
    t, u = get_up_url(get_token())
    upload(up_token=t, up_url=u, file_name=file_name)
