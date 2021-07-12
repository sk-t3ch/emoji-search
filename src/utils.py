import json
import numpy as np
import pandas as pd
import gensim
import numpy as np
from numpy import dot
from numpy.linalg import norm


def word_averaging(model, return_json=False):
    """
    Finds mean word vector from a list of words
    """
    def func(text):
        words = text.split(" ")
        word_vectors = [ model.syn0norm[model.vocab[word].index] for word in words if word in model.vocab]
        if len(word_vectors) > 0:
            mean_vector = np.array(word_vectors).mean(axis=0)
            unit_vector = gensim.matutils.unitvec(mean_vector).astype(np.float32).tolist()
        else:
            unit_vector = np.zeros(model.vector_size, ).tolist()
        if not return_json:
            return unit_vector
        else:
            return json.dumps(unit_vector)
    return func


def find_sim(search_vector):
    """
    Given two vectors finds the cosine similarity
    """
    def func(emoji_vector):
        b_emoji = np.array(emoji_vector)
        cos_sim = dot(search_vector, b_emoji) / (norm(search_vector) * norm(b_emoji))
        return cos_sim
    return func


def EmojiSearchBuilder(model, emoji_df):
    def func(body):
        """
        Find recommendation based on a search string as to what
        n most similar emojis are
        """
        quantity = body.get('quantity', 5)
        search = body['search']
        word_processor = word_averaging(model)
        s = np.array(word_processor(search))
        find_sim_to_search = find_sim(s)
        emoji_df['score'] = emoji_df['v'].apply(find_sim_to_search)
        best = emoji_df.nlargest(quantity, 'score')
        best_filtered = best[['score', 'emoji', 'description']]
        most_similar =  best_filtered.to_dict(orient='records')
        return {"most_similar": most_similar}
    return func

