from src.functions import process_user_choice, set_api_key, get_article_text, options, audio_or_text
from src.classes import bcolors

def main():
    print("#############################################")
    print("#############################################")
    print(f'{bcolors.HEADER}Welcome to the Guardian article program! Here you can process articles in different ways before either reading or listening to them.{bcolors.ENDC}')

    # Get the API's response
    set_api_key()

    # Get a link to the article of interest
    url = process_user_choice()

    # Get the article text
    article_text = get_article_text(url)
    
    # Get the user's choice
    result = options(article_text)

    # audio or text option
    audio_or_text(result)    

if __name__ == "__main__":
    main()