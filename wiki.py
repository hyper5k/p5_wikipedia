import wikipediaapi
import time

user_agent = "p3_wikipedia (kurtpablic0@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

# function to return list of links
def fetch_links(page): 
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    links = fetch_links(start_page)

    # make a loop that checks every utem in links and prints out a message if 
    # target_page.title is in that list




# start and end pages for our wikipedia game
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Counter Strike Global Offensive")
wikipedia_game_solver(start_page, target_page)

links_list = [start_page, target_page] 
for target_page in links_list:
    print(target_page)

print(fetch_links(start_page))