
import requests
import os 
from typing import List

SIXGPT_API_URL = "https://api.sixgpt.xyz/v1-sixgpt"

def get_uniqueness_score(titles: List[str]) -> float:
    resp = requests.post(
        url=f"{SIXGPT_API_URL}/validator/uniqueness",
        json={"task": "uniqueness", "contexts": titles},
        headers={"x-api-key": f"{os.environ['SIXGPT_API_KEY']}"},
    )
    resp.raise_for_status()
    return resp.json()['rating']

def evaluate_question(question: str, context: str) -> float:
    resp = requests.post(
        url=f"{SIXGPT_API_URL}/validator/evaluate-question",
        json={"question": question, "context": context},
        headers={"x-api-key": f"{os.environ['SIXGPT_API_KEY']}"},
    )
    resp.raise_for_status()
    return resp.json()['rating']

def evaluate_answer(question: str, answer: str, context: str) -> float:
    resp = requests.post(
        url=f"{SIXGPT_API_URL}/validator/evaluate-answer",
        json={"question": question, "answer": answer, "context": context},
        headers={"x-api-key": f"{os.environ['SIXGPT_API_KEY']}"},
    )
    resp.raise_for_status()
    return resp.json()['rating']