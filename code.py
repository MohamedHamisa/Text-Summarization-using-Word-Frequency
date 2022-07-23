## input text article
article_text=" "


#Import Modules
import re
import nltk

article_text = article_text.lower()
article_text


# remove spaces, punctuations and numbers
clean_text = re.sub('[^a-zA-Z]', ' ', article_text)
clean_text = re.sub('\s+', ' ', clean_text)
clean_text


# split into sentence list
sentence_list = nltk.sent_tokenize(article_text)
sentence_list




#Word Frequencies
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
maximum_frequency = max(word_frequencies.values())

for word in word_frequencies:
    word_frequencies[word] = word_frequencies[word] / maximum_frequency
    

#Calculate Sentence Scores
sentence_scores = {}

for sentence in sentence_list:
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies and len(sentence.split(' ')) < 30:  #iterate through each sentence and combine the weighted score of the underlying word
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]
word_frequencies

sentence_scores

#Text Summarization
# get top 5 sentences
import heapq  
# Heap queue is a special tree structure in which each parent node is less than or equal to its child node. In python it is implemented using the heapq module
# It is very useful is implementing priority queues where the queue item with higher weight is given more priority in processing
summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

print(" ".join(summary))
