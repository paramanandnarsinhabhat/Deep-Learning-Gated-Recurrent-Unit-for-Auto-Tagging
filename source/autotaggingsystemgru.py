#string matching
import re 

#reading files
import pandas as pd

#handling html data
from bs4 import BeautifulSoup

import zipfile
import os
#visualization
import matplotlib.pyplot as plt  

pd.set_option('display.max_colwidth', 200)

# Specify the path to the zip file
zip_file_path = 'data/archive (2).zip'

# Specify the directory to extract to
extract_to_dir = 'data/unzipped_contents'

# Create a directory to extract to if it doesn't exist
os.makedirs(extract_to_dir, exist_ok=True)

# Open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all the contents into the directory
    zip_ref.extractall(extract_to_dir)
    
    # List the contents of the extracted folder
    print(f"Contents of the zip file '{zip_file_path}':")
    for file_name in zip_ref.namelist():
        print(file_name)

# Now you can access files inside the unzipped directory
# For example, to open a file:
# with open(os.path.join(extract_to_dir, 'yourfile.txt'), 'r') as file:
#     print(file.read())

# load the stackoverflow questions dataset
questions_df = pd.read_csv('data/unzipped_contents/Questions.csv',encoding='latin-1')

#print first 5 rows
print(questions_df.head())

#data/unzipped_contents/
# load the tags dataset
tags_df = pd.read_csv('data/unzipped_contents/Tags.csv')

print(tags_df.head())

#print first 5 rows
questions_df.head()

# Text Cleaning
# Let's define a function to clean the text data.

def cleaner(text):

  text = BeautifulSoup(text).get_text()
  
  # fetch alphabetic characters
  text = re.sub("[^a-zA-Z]", " ", text)

  # convert text to lower case
  text = text.lower()

  # split text into tokens to remove whitespaces
  tokens = text.split()

  return " ".join(tokens)

# call preprocessing function
questions_df['cleaned_text'] = questions_df['Body'].apply(cleaner)

print(questions_df['Body'][1])

print(questions_df['cleaned_text'][1])

# Merge Tags with Questions

# count of unique tags
len(tags_df['Tag'].unique())

print(len(tags_df['Tag'].unique()))

print(tags_df['Tag'].value_counts())


# remove "-" from the tags
tags_df['Tag']= tags_df['Tag'].apply(lambda x:re.sub("-"," ",x))

# group tags Id wise
tags_df = tags_df.groupby('Id').apply(lambda x:x['Tag'].values).reset_index(name='tags')
tags_df.head()

print(tags_df.head())

# merge tags and questions
df = pd.merge(questions_df,tags_df,how='inner',on='Id')

df = df[['Id','Body','cleaned_text','tags']]
df.head()

print(df.head())

print(df.shape)

# Dataset Preparation
# check frequency of occurence of each tag
freq= {}
for i in df['tags']:
  for j in i:
    if j in freq.keys():
      freq[j] = freq[j] + 1
    else:
      freq[j] = 1

#Let's find out the most frequent tags.
# sort the dictionary in descending order
freq = dict(sorted(freq.items(), key=lambda x:x[1],reverse=True))

freq.items()

print(freq.items())

# Top 10 most frequent tags
common_tags = list(freq.keys())[:10]
common_tags

print(common_tags)

x=[]
y=[]

for i in range(len(df['tags'])):
  
  temp=[]
  for j in df['tags'][i]:
    if j in common_tags:
      temp.append(j)

  if(len(temp)>1):
    x.append(df['cleaned_text'][i])
    y.append(temp)

# number of questions left
len(x)

print(len(x))

print(y[:10])

from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer()
 
y = mlb.fit_transform(y)
y.shape

print(y.shape)

y[0,:]

print(y[0,:])

print(mlb.classes_)

