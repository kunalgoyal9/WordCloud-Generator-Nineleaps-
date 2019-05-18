# importing all necessery modules
import numpy as np
import pandas as pd 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 

#read Data
quotes = pd.read_csv('Quotes - quotes.csv')
words = pd.read_csv('Words - Sheet1.csv')

#convert quotes to lower
quotes = quotes['quote'].str.lower()
words = words['search_word'].str.lower()
words = pd.DataFrame(words)

data = {}

for i in words['search_word']:
    data[i] = 0

for i in words['search_word']:
    for j in quotes:
        if i in j:
            data[i]+=1

dataf = pd.DataFrame(list(data.keys()))
dataf[1] = data.values()

#WordCloud
df = dataf 
comment_words = ' '
stopwords = set(STOPWORDS) 

# iterate through the csv file 
for val in df[0]: 
    val = str(val)  
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
          
    for words in tokens: 
        comment_words = comment_words + words + ' '
  
  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate_from_frequencies(data) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.savefig('Cloud.jpg')
