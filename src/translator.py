import os
import six
import html
from google.cloud import translate_v2 as translate


class Translator:
    def __init__(self, creds_path: str):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = creds_path
        self._client = translate.Client()

    def translate(self, text, target='uk'):
        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        result = self._client.translate(text, target_language=target)
        return html.unescape(result['translatedText'])
