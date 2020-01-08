from random import choice
import requests
from bs4 import BeautifulSoup
from csv import DictWriter, DictReader
from os import path

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    url = "/page/1"
    all_quotes = []
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        print(f"Now scraping {BASE_URL}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
            next_btn = soup.find(class_="next")
            url = next_btn.find("a")["href"] if next_btn else None
    return all_quotes


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote:")
    print(quote["text"])
    print(quote["author"])
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses} \n")
        if guess.lower() == quote['author'].lower():
            print("Correct!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place} ")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with: {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)? ")
        if again.lower() in ('yes', 'y'):
            return start_game(quotes)
        else:
            print("OK, Goodbye!")


def write_quotes(quotes):
    with open("quotes.csv", "w") as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


rescrape = input("Check for updated quotes (y/n)? ")
if rescrape.lower() in ('n', 'no') and path.isfile('quotes.csv'):
    all_quotes = read_quotes("quotes.csv")
else:
    all_quotes = scrape_quotes()
    save_prompt = input("Save these quotes for future games (y/n)? ")
    if save_prompt.lower() in ('y', 'yes'):
        write_quotes(all_quotes)

start_game(all_quotes)
