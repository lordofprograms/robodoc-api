from pydantic import BaseModel


class Answer(BaseModel):
    original_answer: str = None
    translated_answer: str = None
