#!/usr/bin/env python
# coding: utf-8

# # Data Extraction and NLP(Test Assignment)
# 
# ### <U>WEB-SCRAPPING USING BEAUTIFUL SOUP<U>
#     

# In[25]:


import os
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

# Read the Excel file
df = pd.read_excel("C:\\Users\\Vanditha Dsouza\\Input.xlsx")

# Define the folder path to save the articles
folder_path = 'C:\\Users\\Vanditha Dsouza\\articles'

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define the specific pattern to search within the div class
specific_pattern = r'td-post-content tagdiv-type'

# Define a function to scrape the article content from a URL
def scrape_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')

        # Find the title of the article
        title_element = soup.find('title')
        title = title_element.text.strip() if title_element else ''

        # Find all div elements with the specific pattern in class attribute
        div_elements = soup.find_all('div', class_=re.compile(specific_pattern))

        for div_element in div_elements:
            # Find all paragraph elements within the div
            paragraphs = div_element.find_all('p')

            # Extract the text from the paragraph elements and convert to lowercase
            text = ' '.join(paragraph.get_text().lower() for paragraph in paragraphs)

            return title, text.strip()  # Strip leading/trailing whitespace
    return '', ''

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    title, article_text = scrape_article(url)
    file_path = os.path.join(folder_path, f'{url_id}.txt')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f'Title: {title}\n\n')
        file.write(article_text)

    # Add the file path to the DataFrame
    df.at[index, 'Path'] = file_path

    print(f"Article from URL_ID {url_id} saved as {file_path}")


# ![image-2.png](attachment:image-2.png)

# In[28]:


df.head(10)


# ### <u>TEXT ANALYSIS USING NLP

# #### IMPORTING MODULES

# In[29]:



import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
nltk.download("all")
#import pyphen


# #### TEXT PREPROCESSING

# In[31]:


extra_stopword=[]
with open("C:\\Users\\Vanditha Dsouza\\StopWords_Names.txt", 'r') as file:
   extra_stopword = [line.strip() for line in file.readlines()]
with open("C:\\Users\\Vanditha Dsouza\\StopWords_Geographic.txt", 'r') as file:
   extra_stopword = extra_stopword+[line.strip() for line in file.readlines()]
with open("C:\\Users\\Vanditha Dsouza\\StopWords_GenericLong.txt", 'r') as file:
   extra_stopword = extra_stopword+[line.strip() for line in file.readlines()]
with open("C:\\Users\\Vanditha Dsouza\\StopWords_Generic.txt", 'r') as file:
   extra_stopword = extra_stopword+[line.strip() for line in file.readlines()]
with open("C:\\Users\\Vanditha Dsouza\\StopWords_DatesandNumbers.txt", 'r') as file:
   extra_stopword = extra_stopword+[line.strip() for line in file.readlines()]
with open("C:\\Users\\Vanditha Dsouza\\StopWords_Auditor.txt", 'r') as file:
   extra_stopword = extra_stopword+[line.strip() for line in file.readlines()]
with open("C:\\Users\\Vanditha Dsouza\\StopWords_Currencies.txt", 'r') as file:
   for line in file:
       word = line.strip().split('|')[0].strip()
       extra_stopword.extend(word)
extra_stopword = [word.lower() for word in extra_stopword]
extra_stopword[0] = extra_stopword[0].replace('  | Surnames from 1990 census > .002%.  www.census.gov.genealogy/names/dist.all.last', '')
#stop_words=stopwords.words('english')+extra_stopword
df["contents"]=""
personal_pronouns = ['i', 'we', 'my', 'ours', 'us']

def remove_numbers(text):
   pattern=r'[^A-z\s]'
   return re.sub(pattern, '',text).lower()
for index, row in df.iterrows():
   file_path = row['Path']
   with open(file_path, 'r', encoding='utf-8') as file:
       text = file.read()

   # Tokenize the contents
   tokens = word_tokenize(text)
   sentences = sent_tokenize(text)
   # Remove stopwords
   filtered_tokens = [remove_numbers(token) for token in tokens if token.lower() not in extra_stopword and token.isalpha()]
   
   
   #lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
   
   # Update the DataFrame with filtered tokens
   df.at[index,'contents'] = filtered_tokens
   df.at[index, 'Num_Sentences'] = len(sentences)
   


# #### FINDING VARIABLES

# In[33]:


with open("C:\\Users\\Vanditha Dsouza\\positive-words.txt", 'r') as file:
    pos= [line.strip() for line in file.readlines()]
pos= [word.lower() for word in pos]
with open("C:\\Users\\Vanditha Dsouza\\negative-words.txt", 'r') as file:
    neg= [line.strip() for line in file.readlines()]
neg= [word.lower() for word in neg]
'''
dic = pyphen.Pyphen(lang='en')

Define a function to count the number of syllables in a word
def count_syllables(word):
    return len(dic.inserted(word).split('-'))
    we can use this pre-defined module to count syllables but 
    since you have asked to define our own function we are using the following
'''

def count_syllables(word):
    # Handling exceptions for words ending with "es" or "ed"
    word = re.sub(r'ed$', '', word)
    word = re.sub(r'es$', '', word)
    # Counting the number of vowels in the word
    vowels = re.findall(r'[aeiou]+', word, re.I)
    return len(vowels)
df['SYLLABLE PER WORD']=""
for index, row in df.iterrows():
    filtered_tokens = row['contents']

    # Calculate the positive score
    positive_score = sum((1 for token in filtered_tokens if token in pos))
    df.at[index, 'POSITIVE SCORE'] = positive_score

    # Calculate the negative score
    negative_score = sum((-1 for token in filtered_tokens if token in neg))*-1
    df.at[index, 'NEGATIVE SCORE'] = negative_score

    # Calculate the polarity score
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    df.at[index, 'POLARITY SCORE'] = polarity_score
    
    
    #Calulate the Subjectivity score
    Subjectivity_Score = (positive_score + negative_score)/ ((len(filtered_tokens)) + 0.000001)
    df.at[index, 'SUBJECTIVITY SCORE'] = Subjectivity_Score
    
     # Calculate the average sentence length
    average_sentence_length = len(filtered_tokens)/row['Num_Sentences']
    df.at[index, 'AVG SENTENCE LENGTH'] = average_sentence_length
    
    # Count the number of complex words
    complex_word_count = sum(1 for token in filtered_tokens if count_syllables(token) > 2)
    Percentage_of_Complex_words=(complex_word_count/len(filtered_tokens))
    
    df.at[index, 'PERCENTAGE OF COMPLEX WORDS']=Percentage_of_Complex_words
    #computing FOG index
    Fog_Index = 0.4 * (average_sentence_length + Percentage_of_Complex_words)
    df.at[index, 'FOG INDEX'] =Fog_Index
    
    
    df.at[index, 'COMPLEX WORD COUNT'] = complex_word_count

    #Word_count after cleaning
    df.at[index, 'WORD COUNT'] = len(filtered_tokens)
    
    #Syllable Count Per Word
    syllable_count_per_word = [count_syllables(word) for word in filtered_tokens]
    avg_syllable_count_per_word = sum([count_syllables(word) for word in filtered_tokens])/len(filtered_tokens)
    df.at[index, 'SYLLABLE PER WORD'] = syllable_count_per_word

    file_path = str(row['Path'])
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the contents
    tokens = word_tokenize(text)

    # Filter and preprocess the tokens
    filtered_tokens = [remove_numbers(token) for token in tokens if token.lower() not in extra_stopword and token.isalpha()]

    # Calculate the personal pronoun count
    personal_pronoun_count = sum([text.lower().count(word) for word in personal_pronouns])

    # Update the DataFrame with the personal pronoun count
    df.at[index, 'PERSONAL PRONOUNS'] = personal_pronoun_count

    # Calculate the total number of words
    total_word_count = len(filtered_tokens)

    # Calculate the sum of the total number of characters in each word
    total_char_count = sum([len(word) for word in filtered_tokens])

    # Calculate the average word length
    avg_word_length = total_char_count / total_word_count

    # Update the DataFrame with the average word length
    df.at[index, 'AVG WORD LENGTH'] = avg_word_length
    df.at[index, 'AVG SYLLABLE PER WORD'] = avg_syllable_count_per_word


# In[34]:


df=df.drop(["Path","contents","Num_Sentences"],axis=1)


# In[35]:


df


# In[37]:


df.to_excel('Output Data Structure.xlsx', index=False, engine='openpyxl')


# In[ ]:




