from googlesearch import search

def search_google(query):
    results = []
    for result in search(term=query, num_results=num_results,advanced=True):
        results.append(result)
    return results

if __name__ == '__main__':
    # Define the search query
    query = "מה השעה בישראל"  # Replace with your desired search query

    # Number of search results to fetch
    num_results = 2

    # Fetch and print search results
    for result in search(term=query, num_results=num_results,advanced=True):
        print(result)
