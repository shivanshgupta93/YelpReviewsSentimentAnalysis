import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import re

def sentiment_calculator(review_data):

    para_words = []
    final_words = []

    for word in review_data['description'].lower().split():
        if 'https' in word:
            continue
        words_list = re.findall(r"[\w']+", word)
        for item in words_list:
            if item == '—':
                continue
            if item == "'":
                continue
            else:
                para_words.append(re.sub("[()“”:…]+", "", item.replace("’","'").replace('.','').replace(',','').replace('—','')))

    clean_words = para_words[:]
    
    stop_words = stopwords.words('english')

    for word in para_words:
        if word.lower() in stop_words:
            clean_words.remove(word)

    word_count = {}

    for word in clean_words:
        if (word == '\-') or (word == ''):
            continue
        if word not in word_count:
            word_count[word] = 1
        
        if word in word_count:
            word_count[word] += 1

    for key, value in word_count.items():
        sentiment_value = ''
        word_dict = {}
        sentiment_text = TextBlob(key)

        if sentiment_text.sentiment.polarity < 0:
            sentiment_value = 'negative'
        elif sentiment_text.sentiment.polarity > 0:
            sentiment_value = 'positive'
        else:
            sentiment_value = 'neutral'

        word_dict['review_id'] = review_data['review_id']
        word_dict['keyword'] = key
        word_dict['keyword_count'] = value
        word_dict['keyword_sentiment'] = sentiment_value
        final_words.append(word_dict)


    return {"data": final_words}
