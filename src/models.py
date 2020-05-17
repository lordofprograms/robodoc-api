from pydantic import BaseModel


class Answer(BaseModel):
    question: str = None
    original_answer: str = None
    translated_answer: str = None
