def download_pdf():
    # 从api获取pdf文件的地址
    api_url = "https://customercenter.wsj.com/todaysPaper/"
    api_response = requests.request("GET", api_url, allow_redirects=False).headers

    # 从api的header返回的重定向地址
    url_302 = api_response['Location']
    print(url_302)

    # 从api的header返回的重定向地址中抠出来的，用于保存文件的文件名，同时也用于对比
    save_pdf_name = api_response['Location'].split('/')[-1].split("-", 1)[1]

    # 判断文件是否已经存在, 如果存在则不再下载
    for local_filename in os.listdir("."):
        if local_filename == save_pdf_name:
            return "文件已存在"

    # 下载pdf文件
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.114", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    pdf_download = requests.request("GET", url_302, headers=headers).content

    # 保存pdf文件
    open("{}".format(save_pdf_name), "wb+").write(pdf_download)
    print('下载完成')
    return save_pdf_name