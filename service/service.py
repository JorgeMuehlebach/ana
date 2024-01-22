
from scraping.scraper import scrape_game_report

from clients.gpt_client import text_2_comentary
from clients.text_2_client import text_2_speech



def generate_epl_mp3():
    game_text = scrape_game_report("671070")
    comentary = text_2_comentary(game_text)
    print("comentary \n", comentary.content)
    text_2_speech(comentary.content)