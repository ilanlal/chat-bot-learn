import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r', -1, "utf-8" ) as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, knowledge_base: dict) -> None:
    with open(file_path, 'w',-1,"utf-8") as file:
        json.dump(knowledge_base, file, indent=2)

def find_best_match(user_question: str, knowledge_base: list[str]) -> str | None:
    matches: list[str] = get_close_matches(user_question, knowledge_base,n=1,cutoff=0.2)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base_item: dict) -> str | None:
    for q in knowledge_base_item["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def get_question_by_text(text: str, knowledge_base_item: dict) -> dict | None:
    for q in knowledge_base_item["questions"]:
        if q["question"] == text:
            return q
    return None