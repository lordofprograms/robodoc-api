from model import QAModel


if __name__ == '__main__':
    biobert_path = '../BioBertFolder/biobert_v1.0_pubmed_pmc/'
    bert_fnn_weights = '../assets/models/bertffn_crossentropy/bertffn'
    embedding_file = '../assets/Float16EmbeddingsExpanded5-27-19.pkl'

    model = QAModel(biobert_path, bert_fnn_weights, embedding_file)
    print(model.predict("I have pain in a pinky finger"))
