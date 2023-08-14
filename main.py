from src.functions import ask_for_url, set_api_key, get_article_text, options, audio_or_text

def main():
    print("Welcome to the Guardian article podcast service! Before listening to the article, you can choose to either shorten it, change the tone, get the main points, or keep the full length. Furthermore, you have the option get a readbility score or main topics as text outputs.")

    # Get the API's response
    set_api_key()

    # Get a link to the article of interest
    url = ask_for_url()

    # Get the article text
    article_text = get_article_text(url)
    
    # Get the user's choice
    result = options(article_text)

    # audio or text option
    audio_or_text(result)    

if __name__ == "__main__":
    main()