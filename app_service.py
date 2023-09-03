from services.google_spreadsheets import get_answers_list, find_answer_by_question, find_suggestions_by_question, find_links_by_question, get_links_list, get_suggestions_list
from difflib import get_close_matches

def get_answer(question:str) -> str | None:
    kb:[str] = get_answers_list()
    
    matches: list[str] = get_close_matches(
        word=question,
        possibilities=[q["question"] for q in kb],
        n=3,
        cutoff=0.6)
    
    if matches:
        # return result from question knowledge base
        return find_answer_by_question(question_as_key=matches[0],data_range=kb)
    else:
        return None
    
def get_suggestions(question:str) -> list | None:
    return find_suggestions_by_question(question_as_key=question,data_range=get_suggestions_list())

def get_links(question:str) -> list | None:
    return find_links_by_question(question_as_key=question,data_range=get_links_list())
        
