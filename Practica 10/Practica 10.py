import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from wordcloud import WordCloud


def open_file(path):
    content = ""
    with open(path, "r") as f:
        content = f.readlines()
    return " ".join(content)

def preprocess_text(text):
    text = text.lower()
    
    text = re.sub(r'\d+', 
                  lambda match: match.group(0) if match.group(0).startswith('t') else '',
                  text)
    text = re.sub(r'[^\w\s]', '', text)
    
    tokens = nltk.word_tokenize(text)
    
    return tokens

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    new_stopwords = ["compartir", "downvote", "upvote", "avatar", "hace",
                     "h", "now", "de", "nov.", "nov", "publicación", "comment",
                     "pr", "wr", "one", "game", "dont" ,"cant", "thought", "comment",
                     "see", "lng", "every", "want", "ver", "publicacion", "completa",
                     "thing", "something", "next", "im", "play", "played", "still",
                     "comment", "even", "think", "people", "playing", "got", "much",
                     "maybe", "yeah", "didnt", "player", "comments", "make", "upvote", "votas",
                     "neta", "lot", "say", "need", "players", "upvotevotar", "world", "going",
                     "team", "fa", "always", "seen", "back", "day", "feel", "ive", "go", "mil", "come", "seem",
                     "really", "better", "find", "well", "post", "bit", "way", "agreement", "since", "youtube", "watch", "ugandalf",
                     "league", "legends", "rleagueoflegends", "spoiler", "year", "th", "ever", "trymbi", "also", "know", "lane", "like",
                     "games", "around", "end", "verbal", "start", "end", "made", "doesnt", "nd","able", "could", "enough", "fact", "actually",
                     "uzokalii", "w", "seguir", "sound", "original", "mas", "que", "siguiendo", "sonido", "edicion", "las", "un", "hay",
                     "denunciar", "compartir", "capcut", "yes","parati", "fyp", "foryoupage", "es", "foryou", "years", "sources", "went", "never", "reached",
                     "new", "long", "many", "already"]
    for word in new_stopwords:
        stop_words.add(word)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def clean_text(text):
    tokens = preprocess_text(text)
    filtered_tokens = remove_stopwords(tokens)
    clean_text = ' '.join(filtered_tokens)
    return clean_text


def generate_wc(all_words, path):
    wc = WordCloud(
        background_color = "white", min_font_size = 5
    ).generate(all_words)

    plt.close()
    plt.figure(figsize=(10,10), facecolor=None)
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.savefig(path)
    plt.close()

def generate_words(path, n):
    all_words = ""
    texto = open_file(path)
    cleaned_text = clean_text(texto)
    palabras = cleaned_text.rstrip().split(" ")

    c = Counter(" ".join(palabras).split()).most_common(80)
    for word in c:
        all_words += " " + word[0]
    
    return all_words

all_words = generate_words("LolReddit.txt", 80)
generate_wc(all_words, "WordCloud_LolReddit.png")

all_words = generate_words("Tiktok.txt", 70)
generate_wc(all_words, "WordCloud_Tiktok.png")
