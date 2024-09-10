import os
import upload
import requests
import download


if __name__ == '__main__':
    name = download.download_pdf()
    upload.run(name)
