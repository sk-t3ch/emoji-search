from Service.utils import function_api_builder, load_schema
import json
import boto3
from utils import EmojiSearchBuilder
import os
import pandas as pd
import gensim

APP_FOLDER = os.path.dirname('.')
FIXTURES_FOLDER = os.path.join(APP_FOLDER, "fixtures")
GOOGLE_NEWS = os.path.join(
    FIXTURES_FOLDER, "GoogleNews-vectors-negative300-SLIM.bin.gz")
EMOJI_FILE = os.path.join(FIXTURES_FOLDER, "emoji_vectors.csv")
emoji_df = pd.read_csv(EMOJI_FILE, index_col=0)
emoji_df['v'] = emoji_df['vector'].apply(json.loads)

model = gensim.models.KeyedVectors.load_word2vec_format(
    GOOGLE_NEWS, binary=True)
model.init_sims(replace=True)

EmojiSearch = EmojiSearchBuilder(model, emoji_df)

schema_path = "schema/"
input_schema = load_schema(f'{schema_path}input.json')
output_schema = load_schema(f'{schema_path}output.json')
lambda_ = boto3.client('lambda', region_name='eu-west-1')
credits = 1
charge_lambda_name = os.environ['CHARGE_LAMBDA']
refund_lambda_name = os.environ['REFUND_LAMBDA']


function_api = function_api_builder(input_schema, output_schema, lambda_, charge_lambda_name, refund_lambda_name, credits, EmojiSearch)

def handler(event, context):
    return function_api(event, context) 