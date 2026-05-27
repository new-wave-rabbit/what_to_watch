import requests

HEADERS = {
    'Apl'
}


def upload_img(file):
    url = 'https://content.dropboxapi.com/2/files/upload'
    response = requests.post(
        url,
        headers=HEADERS,
        files=[file]
    )
    return response.json()
