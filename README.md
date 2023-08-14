<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Datascience 2023</h1> 
  <h2 align="center">Final Project - News Article Processing</h2> 
  <h3 align="center">Language Analytics</h3> 
  <p align="center">
    Jørgen Højlund Wibe<br>
    Student number: 201807750
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About the project
This project is the final part of the portfolios for language analytics exam project.

The project aims to show how different natural language processing tools can function together in a simple and useful way. To showcase this we've developed a program that takes any article from [The Guardian](https://www.theguardian.com/international) as input (scraped using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)) and prompts the user with different ways to preprocess the article. Some of these methods are  text summarization, readability analysis and tone adjustment. Once preprocessed, the user can further on decide whether he/she wants to convert the text to audio using a text-to-speech software, print the text in the console or save it to drive as a .txt file. The script uses Python and several external libraries to achieve its functionality.

<!-- USAGE -->
## Usage
To use or reproduce the results you need to adopt the following steps.

**NOTE:** There may be slight variations depending on the terminal and operating system you use. The following example is designed to work using the Visual Studio Code version 1.77.3 (Universal). The terminal code should therefore work using a unix-based bash. The avoid potential package conflicts, the ```setup.sh``` bash files contains the steps necesarry to create a virtual environment, install libraries and run the project.


1. Get an OpenAI API key
2. Clone repository
3. Update the ```.env``` file
4. Run ```setup.sh```

### Get an OpenAI API key
Create an OpenAI account from their OpenAI's [website](https://openai.com/). Verify and log in to the account and navigate to the API section. Here you can create a new API key. If in doubt, refer to [this thourough guide](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt).

### Clone repository

Clone repository using the following lines in the unix-based bash:

```bash
git clone https://github.com/jorgenhw/language_analytics_assignment_4.git
cd language_analytics_final_project
```

### Update the ```.env``` file
Enter your ```OpenAI API key``` in the environment file ```.env```.

```bash
OPENAI_API_KEY = 'your-key-here'
```
Save the file. These are now global environment variables which the script can read when you run it.

### Run ```setup.sh```

To replicate the results, I have included a bash script that automatically 

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
4. Runs the script
5. Deactivates the virtual environment

Run the code below in your bash terminal:

```bash
bash setup.sh
```

## Your options in the script

Once you run ```setup.sh``` the remainder of the script is controlled via the command line.

When prompted, the user can select whether to work with an article from The Guardian of his/her own choice, or to work with the latest The Guardian Briefing.

Then the user gets the following options to choose from:

1: Shorten Text
2: Explain Like I'm 5 (ELIM5)
3: Text Characteristics (Readability Analysis)
4: Main Points
5: Keep Full Length
Depending on the option selected, the script will process the input text accordingly.

After processing, the user can choose whether he/she want the output text to be read aloud as audio, view it as text in the console or save it as a textfile.

<!-- REPOSITORY STRUCTURE -->
## Repository structure

This repository has the following structure:
```
│   main.py
│   README.md
│   requirements.txt
│   setup.sh
│
├───src
│       functions.py
│       classes.py
│
├───audio_output
│       empty folder
│
└──text_output
        empty folder
```

<!-- RESULTS -->
## Remarks on findings
Throughout the course of this project, several insights were gleaned from the application of various natural language processing techniques to news articles. The implemented text summarization method, powered by GPT-3, effectively condensed lengthy articles into concise summaries, making it an ideal tool for quickly grasping the core content of an article. The tone adjustment feature, which also utilizes GPT-3 to rephrase text in a simplified manner, proved useful for enhancing readability and catering to a wider audience. Furthermore, the readability analysis provided valuable insights into the complexity of the articles, enabling users to gauge their suitability for different readerships. The add-on option to get the article as an audio file speaks into a [growing tendency](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2022/young-audiences-news-media) for especially young people to listen to news instead of reading them. There are far better text-to-speech software to do this than the one used in this project and certainly more news agencies would benefit from looking into this. Very recently [Suno](https://www.suno.ai/) released [Bark](https://github.com/suno-ai/bark) which sounds identical to a human being. And it's open source.

The combination of these techniques offers a versatile toolkit for processing news articles, making them more accessible and informative. It also underscores the potential of AI-driven solutions in enhancing content consumption experiences, enabling individuals to consume news articles tailored to their preferences and comprehension levels.


## Conclusion
In conclusion, this project demonstrates the seamless integration of different natural language processing techniques into a unified framework for news article processing. By utilizing tools like GPT-3 and TextDescriptives, the script offers users the ability personalize how they recieve news to their liking.

This project not only showcases the capabilities of the applied techniques but also highlights the potential of AI-powered solutions in revolutionizing the way we interact with textual content. As a final project for the Cultural Data Science course, this endeavor serves as a testament to the intersection of technology and language analytics, paving the way for further exploration and innovation in the field.

However, there are also a number of things to be aware of when using AI-powered tools to alter existing news. For instance, there is no one checking if the 'main points' version of an article is actually capturing the essence of that article or if ELI5 is correctly explaining the content. Therefore we are running the risk of actually turning real news into fake news by altering them. This is why we should be extremely careful when using e.g. GPT-3 or GPT-4 to alter text in general. 

## Acknowledgements
I am  indebted to the team at OpenAI for providing access to their GPT-3 model through their API. This technology is a crucial element in implementing the various natural language processing functionalities within the project. 
Also thanks to [Lasse Hansen](https://github.com/HLasse) for developing and making [TextDescriptives](https://github.com/HLasse/TextDescriptives) open source for others to use.
