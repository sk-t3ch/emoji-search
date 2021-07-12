from emoji_data import EmojiSequence
import os
import pandas as pd
import gensim
from utils import word_averaging

print("starting")
APP_FOLDER = os.path.dirname('.')
FIXTURES_FOLDER = os.path.join(APP_FOLDER, "fixtures")
GOOGLE_NEWS = os.path.join(FIXTURES_FOLDER, "GoogleNews-vectors-negative300-SLIM.bin.gz")
EMOJI_FILE = os.path.join(FIXTURES_FOLDER, "emoji_vectors.csv")
emoji_df = pd.read_csv(EMOJI_FILE, index_col=0)
print("loading vectors")
model = gensim.models.KeyedVectors.load_word2vec_format(GOOGLE_NEWS, binary=True)
model.init_sims(replace=True)
print("loaded vectors")



def create_emoji_vectors(filename, limit=100):
    """
    Create Emoji Vectors from description and save to CSV
    """
    d = {'emoji': [], 'description': [], 'code_points': []}
    for (_, es) in EmojiSequence:
        d['emoji'].append(es.string)
        d['description'].append(es.description)
        d['code_points'].append(es.code_points)

    df = pd.DataFrame(d)

    # Remove with empty description as cannot be compared
    df = df[df['description'] != '']

    # Limit the number processed
    if limit:
        df = df[:limit]

    # Remove weird characters
    df['description'] = df['description'].str.split(
        ' skin tone').str[0].str.replace(':', '').str.replace(',', '').str.replace('-', ' ')
    df = df.drop_duplicates(subset=['description'])

    # Average words into word vector - these are json
    word_processor = word_averaging(model, return_json=True)
    df['vector'] = df['description'].apply(word_processor)

    del df['description']

    df.to_csv(filename)

if __name__ == "__main__":
    create_emoji_vectors(EMOJI_FILE, limit=False)
    # main()