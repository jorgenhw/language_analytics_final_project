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

The project aims to show how different natural language processing tools can function together in a simple and useful way. To showcase this we've developed a program that takes any article from [The Guardian](https://www.theguardian.com/international) as input and prompts the user with different ways to preprocess the article. Some of these methods are  text summarization, readability analysis and tone adjustment. Once preprocessed, the user can further on decide whether he/she wants to convert the text to audio using a text-to-speech software, print the text in the console or save it to drive as a .txt file. The script uses Python and several external libraries to achieve its functionality.

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

## Conclusion
