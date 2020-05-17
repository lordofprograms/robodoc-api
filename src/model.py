from docproduct.predictor import RetreiveQADoc


class QAModel:
    def __init__(self, biobert_path: str, bert_fnn_weights: str, embedding_file: str):
        self._qa_model = RetreiveQADoc(pretrained_path=biobert_path,
                                       ffn_weight_file=None,
                                       bert_ffn_weight_file=bert_fnn_weights,
                                       embedding_file=embedding_file)

    def predict(self, question_text, search_by: str = 'answer', results_num: int = 1, answer_only: bool = True):
        results = self._qa_model.predict(question_text, search_by=search_by,
                                         topk=results_num, answer_only=answer_only)
        return results
