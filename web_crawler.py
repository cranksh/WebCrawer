import requests
from bs4 import BeautifulSoup
import pyfiglet
from colorama import Fore, Style, init

init()

logo = pyfiglet.figlet_format("Super Crawler")
print(Fore.YELLOW + logo + Style.RESET_ALL)

url = input("Enter the URL to crawl: ")
max_depth = int(input("Enter the maximum depth to crawl: "))

visited_urls = set()

def crawl(url, depth=0):
    if depth > max_depth:
        return

    response = requests.get(url)

    if response.status_code == 200:
        print(Fore.GREEN + "Crawling:", url + Style.RESET_ALL)

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.title
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + '==================== Results ====================')
        if title is not None:
            print(Fore.CYAN + f"Page Title: {title.text.strip()}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "No page title found" + Style.RESET_ALL)

        links = soup.find_all('a')
        print(Fore.MAGENTA + "Links on the page:" + Style.RESET_ALL)
        for link in links:
            href = link.get('href')
            if href:
                print(Fore.LIGHTGREEN_EX + href)
            else:
                print(Fore.YELLOW + "Invalid link" + Style.RESET_ALL)

        tags_to_extract = ['h1', 'p', 'span']
        print(Fore.GREEN + "Other tags on the page:" + Style.RESET_ALL)
        for tag_name in tags_to_extract:
            tags = soup.find_all(tag_name)
            if tags:
                for tag in tags:
                    if tag.text.strip():
                        print(f"• {Fore.MAGENTA}{tag_name}: {Fore.GREEN}{tag.text.strip()}{Style.RESET_ALL}")
                    else:
                        print(f"• {tag_name}: {Fore.YELLOW}Empty{Style.RESET_ALL}")
            else:
                print(f"• {tag_name}: {Fore.YELLOW}Not found{Style.RESET_ALL}")

    else:
        print(Fore.RED + "Error accessing the URL:", url + Style.RESET_ALL)

crawl(url)
