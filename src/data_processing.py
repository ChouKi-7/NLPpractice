import pandas as pd
import re
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer


'''
モデル:bertweet-base
BERTモデルは文のコンテキスト(文脈)を理解する設計なので、
過度な加工は逆効果になることがあります。基本的にはTokenizerに任せるのが良いです。
'''

##　データ前処理
def clean_data(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", "http", text)
    text = re.sub(r"@\w+", "@user", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

##　データ読み込みと列処理
def load_data():
    train_data = pd.read_csv("data/raw/train.csv")

    # print(train_data.head())
    # print(train_data.shape)
    # print(train_data.info)
    # print(train_data.isnull().sum())

    train_data.drop(['id','keyword', 'location'], axis=1, inplace=True)

    class_counts = train_data['target'].value_counts().rename_axis("target").reset_index(name="count")
    
    print(class_counts)
    # print(train_data.head())
    # print(train_data.info)

    train_data["text"] = train_data["text"].apply(clean_data)
    return train_data

## 訓練用データと評価用データ
def split_data(data):
    train_texts, val_texts, train_labels, val_labels = train_test_split(
        data["text"].tolist(), 
        data["target"].tolist(), 
        test_size=0.2, 
        random_state=42
    )
    return train_texts, val_texts, train_labels, val_labels

# Twitter専用の事前学習済みBERTモデル「vinai/bertweet-base」のTokenizerを読み込む。
# このTokenizerは、ツイートテキストをモデルが理解できる形式（トークンIDやマスク）に変換する役割を持つ。
# ・"vinai/bertweet-base"：使用するモデル名を指定（事前学習済み）
# ・normalization=True：Unicode絵文字や特殊記号などの正規化を有効にする（Bertweetでは推奨）
def tokenize(data):
    tokenizer = AutoTokenizer.from_pretrained("vinai/bertweet-base", normalization=True)
    return tokenizer(data,truncation = True, padding = True, retrun_tensors="pt")