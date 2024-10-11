import wikipediaapi
import time
from queue import Queue

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
    print("working on it.....")
    start_time = time.time()

    queue = Queue() # queue for which items to check next
    visited = set() # keeps track of visited links
    parent = {} # dictionary to keep track of parent

    # start off by adding the start page to our queue and visited
    queue.put(start_page.title)
    visited.add(start_page.title)

    # keep looping as long as queue is not empty
    while not queue.empty():
        # get next item in our queue
        current_page_title = queue.get()
        # break out of loop if we find page we're looking for
        if current_page_title == target_page.title:
            break

        # fetch all the links at the current page
        current_page = wiki.page(current_page_title)
        links = fetch_links(current_page)

        # go through each of the links and add them to queue
        for link in links:
            # if page hasn't already been visited
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link] = current_page_title
    
    # reconstruct path from target page to start page
    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]
    
    path.append(start_page.title)
    path.reverse()
    
    end_time = time.time()
    print("this algorithm took", end_time - start_time, "seconds.")
    return path

# start and end pages for our wikipedia game solver
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Counter Strike")
path = wikipedia_game_solver(start_page, target_page)
print(path)