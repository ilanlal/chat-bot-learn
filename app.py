import os
from app_service import get_suggestions,get_links,get_answer
from flask import Flask, request, jsonify,render_template
from googlesearch import search

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("chatbot.html")

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        question = data['message']
        bot_response = get_answer(question=question,n=3,cutoff=0.5)

        return jsonify({'response': bot_response})
    except:
        return jsonify({'response': None })

@app.route('/api/suggestions', methods=['POST'])
def suggestions():
    data = request.get_json()
    question = data['message']
    bot_response = get_suggestions(question)
    return jsonify({'suggestions': bot_response})

@app.route('/api/links', methods=['POST'])
def links():
    data = request.get_json()
    question = data['message']
    bot_response = get_links(question)
    return jsonify({'links': bot_response})

@app.route('/api/search', methods=['POST'])
def search_with_google():
    data = request.get_json()
    question = data['message']
    limit = data['limit'] or 1 # this will result in 1
    if limit>10: 
        limit=10

    language = 'he'
    results = []
    
    for result in search(term=question, num_results=limit,advanced=True,lang=language):
        results.append({"description":result.description,"title":result.title,"url":result.url})

    return jsonify({'response': results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))