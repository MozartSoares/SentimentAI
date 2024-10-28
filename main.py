import string
from collections import Counter
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords # stop words are words that have no meaning for the sentence to be analised using NLP
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def preprocess_text(file_name='example.txt'):
  # cleaning text
  try:
    text = open(file_name,encoding='utf-8').read()
  except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    exit()

  lower_text = text.lower()
  
  cleaned_text = lower_text.translate(str.maketrans('','',string.punctuation))
  
  analyse_sentiment(cleaned_text)
  
  # tokenizing text
  tokenized_words = word_tokenize(cleaned_text,"english")
  final_words = []

  # removing stop words from tokenized words
  for word in tokenized_words:
    if word not in stopwords.words('english'):
      final_words.append(word)
  return cleaned_text,final_words 

def check_emotions(words_list):
  emotions_list = []
  with open('emotions.txt','r') as file:
    for line in file:
      clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
      word, emotion = clear_line.split(':')
      
      # if we find the current emotion for the word, we append it to the emotions_list
      if word in words_list:
        emotions_list.append(emotion.strip())

    return emotions_list

def analyse_sentiment(sentiment_text):
  score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
  negative = score['neg']
  positive = score['pos']
  if (negative > positive):
    sentiment = 'Negative Sentiment'
  elif (positive > negative):
    sentiment = 'Positive Sentiment'
  else: 
    sentiment = 'Neutral Sentiment'
    
  return sentiment

def visualize_emotions(sentiment,emotions_list):
    emotions_count = Counter(emotions_list)
    
    fig, ax1 = plt.subplots()
    ax1.bar(emotions_count.keys(), emotions_count.values())
    ax1.set_xlabel('Emotions')
    ax1.set_ylabel('Frequency')
    plt.title('Frequency of Emotions')
    
    facecolor = 'green' if sentiment == 'Positive Sentiment' else 'red' if sentiment == 'Negative Sentiment' else 'yellow'
    ax1.text(0.5, max(emotions_count.values()) * 0.9, f'Main sentiment: {sentiment}',horizontalalignment='center', fontsize=12, color='black', bbox=dict(facecolor=facecolor, alpha=0.5))
    
    plt.xticks(rotation=45)
    plt.tight_layout()  
    plt.savefig('emotions_graph.png')
    plt.show()

def main():
    # ask user for the filepath 
    print("Welcome to the Sentiment Analysis Tool!")
    print('If you just want to test it out with a sample text file, please use "example.txt", it contains a speech Steve Jobs gave at Stanford University.')
    filepath = input("Please insert the name for your text file (e.g. example.txt): ")

    # gets text from the file that the user chose
    cleaned_text, processed_words = preprocess_text(filepath)
    
    # gets overall sentiment of the text
    sentiment = analyse_sentiment(cleaned_text)
    
    # get emotions and compares it with the sample data 'emotions.txt', it gets emotions count and frequency for the graphs
    emotions_list = check_emotions(processed_words)
    
    # make chart to visualize the result
    visualize_emotions(sentiment,emotions_list)


if __name__ == '__main__':
  main()  