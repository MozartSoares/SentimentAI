# cleaning text steps:
#   1) create a text file and take text from it
#   2) Convert the letters into lowercase ('Apple' != 'apple')
#   3) remove punctuationss like .,!? etc. ('Hi! this is Mozart Soares.')
import string
from collections import Counter
from matplotlib import pyplot

def preprocess_text(file_name='read.txt'):
  # cleaning text
  text = open(file_name,encoding='utf-8').read()
  
  lower_text = text.lower()
  
  cleaned_text = lower_text.translate(str.maketrans('','',string.punctuation))
  
  # tokenizing text
  tokenized_words = cleaned_text.split() 
  
  # stop words are words that have no meaning for the sentence to be analised using NLP
  stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
  
  final_words = [] 
  # removing stop words from tokenized words
  for word in tokenized_words:
    if word not in stop_words:
      final_words.append(word)
  return final_words 

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


def main():
  processed_words = preprocess_text()
  emotions_list = check_emotions(processed_words)
  # print(processed_words)
  print(emotions_list)
  emotions_count = Counter(emotions_list)
  
  # creating graph
  fig, ax1 = pyplot.subplots()
  ax1.bar(emotions_count.keys(), emotions_count.values())
  fig.autofmt_xdate()
  
  pyplot.savefig('emotions_graph.png')
  pyplot.show()
if __name__ == '__main__':
  main()  