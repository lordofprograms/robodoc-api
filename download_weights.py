import os
import shutil
import requests
import urllib.request
import zipfile
import tarfile


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == '__main__':
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(
        'https://github.com/naver/biobert-pretrained/releases/download/v1.0-pubmed-pmc/biobert_v1.0_pubmed_pmc.tar.gz',
        'BioBert.tar.gz')

    if not os.path.exists('BioBertFolder'):
        os.makedirs('BioBertFolder')

    tar = tarfile.open("BioBert.tar.gz")
    tar.extractall(path='BioBertFolder/')
    tar.close()
    os.remove('BioBert.tar.gz')
    print('Downloaded BioBert!')

    file_id = '1uCXv6mQkFfpw5txGnVCsl93Db7t5Z2mp'
    download_file_from_google_drive(file_id, 'Float16EmbeddingsExpanded5-27-19.pkl')
    print('Downloaded file from Google Drive')

    file_id = \
        'https://onedrive.live.com/download?cid=9DEDF3C1E2D7E77F&resid=9DEDF3C1E2D7E77F%2132792&authkey=AEQ8GtkcDbe3K98'
    urllib.request.urlretrieve(file_id, 'DataAndCheckpoint.zip')
    print('Downloaded DataAndCheckpoint.zip')

    if not os.path.exists('assets'):
        os.makedirs('assets')

    zip_ref = zipfile.ZipFile('DataAndCheckpoint.zip', 'r')
    zip_ref.extractall('assets')
    zip_ref.close()
    os.remove('DataAndCheckpoint.zip')
    shutil.move('Float16EmbeddingsExpanded5-27-19.pkl', 'assets')
    print('All files were successfully downloaded!')
