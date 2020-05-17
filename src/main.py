from fastapi import FastAPI
from src.models import Answer
from src.qa_model import QAModel
from src.translator import Translator


app = FastAPI()

biobert_path = 'BioBertFolder/biobert_v1.0_pubmed_pmc/'
bert_fnn_weights = 'assets/models/bertffn_crossentropy/bertffn'
embedding_file = 'assets/Float16EmbeddingsExpanded5-27-19.pkl'
qa_model = QAModel(biobert_path, bert_fnn_weights, embedding_file)

translator = Translator(creds_path='gct_creds.json')


@app.get('/api/v1/ask', response_model=Answer)
async def ask(question: str, lang: str):
    if lang == 'uk':
        question = translator.translate(question, target=lang)
        # return only 1 answer
        orig_result = qa_model.predict(question)[0]
        trans_result = translator.translate(orig_result)
        return {"original_answer": orig_result, "translated_answer": trans_result}
    else:
        result = qa_model.predict(question)[0]
        return {"original_answer": result, "translated_answer": result}
