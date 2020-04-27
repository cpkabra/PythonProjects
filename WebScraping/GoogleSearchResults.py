import requests, bs4, webbrowser as wb, sys

python_tab_url = "https://pypi.org/"
python_query_url = "search/?q="
python_search_url = python_tab_url + python_query_url
search_query = input("Please enter what you would like to search : ")
python_request_response = requests.get(python_search_url + search_query)
python_request_response.raise_for_status()

tags = bs4.BeautifulSoup(python_request_response.text, "html.parser").select(".package-snippet")


num_open = min(5, len(tags))
for i in range(0,num_open):
    wb.open_new_tab(python_tab_url + tags[i].get('href'))