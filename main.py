import requests
from bs4 import BeautifulSoup

# Add the list of urls here
urls = [] 

all_transcripts = []

for url in urls:

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # You're going to have to check the HTML as well as the BeautifulSoup docs to figure out how to grab whattever data you want.
    content_div = soup.find("div", class_="mw-parser-output")

    paragraphs = content_div.find_all("p")

    for p in paragraphs:

        all_transcripts.append(p.get_text())

combined_transcript = "\n\n".join(all_transcripts)

# instead of "Dragon_Ball_Z_Abridged.txt", put whatever name you want fo ryour file
with open("Dragon_Ball_Z_Abridged.txt", "w", encoding="utf-8") as file:
    file.write(combined_transcript)