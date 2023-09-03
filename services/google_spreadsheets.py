import gspread

from oauth2client.service_account import ServiceAccountCredentials
QUESTIONS_WORKSHEET_NAME:str = "מאגר שאלות"
SUGGESTION_WORKSHEET_NAME:str = "חיבורים"
LINKS_WORKSHEET_NAME:str = "לינקים"

def get_full_kb():
    answers_data = get_answers_list()
    suggestions_data = get_suggestions_list()
    links_data = get_links_list()

    #build the knowledge base
    kb = { "questions":[] }
    for answer in answers_data:
        kb["questions"].append({
                "question":answer["question"],
                "answer":answer["answer"],
                "suggestions":[s["suggestion"] for s in suggestions_data if s["question"] == answer["question"]],
                "links":[{"title":l["title"],"url":l["url"]} for l in links_data if l["question"] == answer["question"]]
            } )
        
    return kb

def get_answers_list():
    answers_data = _get_google_sheet_data(QUESTIONS_WORKSHEET_NAME)
    
    #build the knowledge base full data answer
    questions = []
    for row in answers_data:
        questions.append({"question":row[0],"seo":row[1] or None,"answer":row[2]})
    
    return questions

def get_suggestions_list():
    suggestions_data = _get_google_sheet_data(SUGGESTION_WORKSHEET_NAME)
    
    #build the knowledge base full data answer
    suggestions = []
    for s in suggestions_data:
        suggestions.append({"question":s[0],"suggestion":s[1]})
    
    return suggestions

def get_links_list():
    links_data = _get_google_sheet_data(LINKS_WORKSHEET_NAME)
    
    #build the knowledge base full data answer
    links = []
    for l in links_data:
        links.append({"question":l[0],"title":l[1],"url":l[2]})
    
    return links

def find_answer_by_question(question_as_key:str,data_range:list):
    #build the knowledge base full data answer
    answer = [row for row in data_range if row["question"] == question_as_key][0] if data_range else None
    
    return answer

def find_suggestions_by_question(question_as_key:str,data_range:list):
    #build the knowledge base full data answer
    suggestions = [s for s in data_range if s["question"] == question_as_key] if data_range else None
    
    return suggestions

def find_links_by_question(question_as_key:str,data_range:list):
    #build the knowledge base full data answer
    links = [{"title":l["title"],"url":l["url"]} for l in data_range if l["question"] == question_as_key]
    
    return links

# Define the scope and load credentials from the JSON file
def _get_google_sheet_data(worksheet_name:str):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # Authenticate with Google Sheets
    client = gspread.authorize(creds)

    # Open the Google Spreadsheet by its title
    spreadsheet_id = '1SGCxlScKZIofgcSvM1IeE3osw6H9UIQ_ttxJ6jbWebk'  # Replace with your spreadsheet title
    spreadsheet = client.open_by_key(spreadsheet_id)

    # Select a specific worksheet by title or index (0-based)
    # worksheet = spreadsheet.get_worksheet(2)  # Replace 0 with the index of your desired worksheet
    worksheet = spreadsheet.worksheet(worksheet_name)

    # Read data from the worksheet
    data = worksheet.get_all_values()

    return data

if __name__ == '__main__':
    # print(get_full_kb())
    print(get_answers_list())
    # print(get_suggestions_list())
    # print(get_links_list())

    # print(find_answer_by_question('שלום היי',get_answers_list()))
    # print(find_links_by_question('שלום היי',get_links_list()))
    #print(find_suggestions_by_question('שלום היי',get_suggestions_list()))