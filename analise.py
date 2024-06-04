import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('punkt')
with open(
    "dados/msg.txt", 
    "r", 
    encoding="utf-8") as f:
    texto = f.read()
print(texto)
word = word_tokenize(texto)
print(word)
fdist = FreqDist(word)
print(fdist.most_common(5))

# Wordcloud
def plot(wordcloud):
    plt.figure(figsize=(40,30))
    plt.imshow(wordcloud)
    plt.show()

wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color='salmon',
    colormap = 'Pastel1',
    collocations= False
).generate(texto)
plot(wordcloud)