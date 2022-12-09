from transformers import pipeline
from transformers import AutoModelForQuestionAnswering, AutoTokenizer


class QA_Model:

    
    def Model_Portuguese(self, contexto, questao):
        tokenizer = AutoTokenizer.from_pretrained("eraldoluis/faquad-bert-base-portuguese-cased")
        model = AutoModelForQuestionAnswering.from_pretrained("eraldoluis/faquad-bert-base-portuguese-cased")
        
        nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)

        result = nlp(question=questao, context=contexto)
        return result
        print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")


    def Model_English(self, contexto, questao):

        tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2-covid")
        model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2-covid")

        nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
        res = nlp(question=questao, context=contexto)

        print(res) 
    
