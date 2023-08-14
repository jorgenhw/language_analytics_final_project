import requests
from bs4 import BeautifulSoup
import openai
import textdescriptives as td
import numpy as np
import nltk
import os
from gtts import gTTS
from dotenv import load_dotenv # pip3 install python-dotenv For loading the environment variables (API keys and playlist URI's)

# Only download the punkt tokenizer once
nltk.download('punkt', quiet=True)

def set_api_key():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

#os.environ["OPENAI_API_KEY"]=("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")
#openai.api_key = os.environ["OPENAI_API_KEY"]

def ask_for_url():
    return input("Enter a URL to an article from The Guardian website: ")

def get_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    article = soup.find('div', {'class': 'article-body-commercial-selector'})

    for unwanted_element in article(['script', 'style', 'aside', 'figure']):
        unwanted_element.decompose()

    text = ' '.join([paragraph.text for paragraph in article.find_all('p')])

    return text

def keep_full_length(text):
    return text

def shorten_with_gpt(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant. Summarize the following text."},
            {"role": "user", "content": text},
        ]
    )
    return response['choices'][0]['message']['content']

def change_tone_elim5(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant. Explain the following text like I'm 5."},
            {"role": "user", "content": text},
        ]
    )
    return response['choices'][0]['message']['content']

def get_text_characteristics(text):
    df = td.extract_metrics(text=text, spacy_model="en_core_web_lg", metrics=["readability", "coherence"])
    flesch_reading_ease = f"Reading score: {round(float(df['flesch_reading_ease'][0]),1)} (0 is reasy, 100 is hard, 60-70 is normal)"
    return flesch_reading_ease

def main_points_with_gpt(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant. Provide the main points of the following text as bullet points."},
            {"role": "user", "content": text},
        ]
    )
    return response['choices'][0]['message']['content']


def text_to_audio(text, language='en', output_folder='audio_output', output_file='output.mp3'):
    """
    Converts input_text to audio and saves it as an MP3 file.

    Args:
        input_text (str): The text to convert to audio.
        language (str): The language in which to convert the text. Default is 'en' (English).
        output_folder (str): The folder in which to save the output audio file. Default is 'audio_output'.
        output_file (str): The name of the output MP3 file. Default is 'output.mp3'.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, output_file)
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save(output_path)
    print(f"Audio version of the text saved as {output_path}")

# Example usage
result_text = "This is the result text that you want to process."
text_to_audio(result_text, output_folder='audio_output', output_file='output.mp3')


def options(article_text):
    option = input("Choose an option: 1.Shorten 2.ELIM5 3.Characteristics 4.Main points 5.Keep full length ")

    if option == '1':
        result = shorten_with_gpt(article_text)
    elif option == '2':
        result = change_tone_elim5(article_text)
    elif option == '3':
        result = get_text_characteristics(article_text)
    elif option == '4':
        result = main_points_with_gpt(article_text)
    elif option == '5':
        result = keep_full_length(article_text)
    else:
        result = "Invalid option"
    return result

def audio_or_text(result):
    while True:
        audio_option = input("Would you like the text read aloud? (yes/no) ").strip().lower()
        
        if audio_option in ['yes', 'y']:
            text_to_audio(result)
            break
        elif audio_option in ['no', 'n']:
            print(result)
            break
        else:
            print("Please either answer 'yes' or 'no'. You can also use 'y' or 'n'.")
