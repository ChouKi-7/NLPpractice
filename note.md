# 通常LLMプロジェクト 全体フロー：
## step1 環境準備
必要に応じ、requirements.txt に記述したライブラリーをインストール

```bash
pip install -r requirements.txt
```

## step2 データを読み込み

## step3 データ前処理

### 1. 小文字化（Lowercasing）
全ての単語を小文字に統一します：
例：`"I LOVE NLP"` → `"i love nlp"`

### 2. 記号・数字の除去
句読点、絵文字、記号、URL、メールアドレスなどを削除します：
例：`"Check out https://example.com! 😄"` → `"Check out"`

### 3. ストップワードの除去（Stopword Removal）
意味の少ない単語（例："the", "is", "and"など）を削除します。

### 4. ステミング（Stemming）またはレンマタイゼーション（Lemmatization）
単語を基本形に変換します：
- Stemming: `"running"` → `"run"`（荒い）
- Lemmatization: `"better"` → `"good"`（文法的に正確）

### 5. トークン化（Tokenization）
文を単語やサブワードに分割します：
例：`"I love NLP"` → `["I", "love", "NLP"]`

### 6. スペル修正（Optional）
綴りの間違いを訂正する処理（例："recieve" → "receive"）

### 7. テキストの正規化（Optional）
例：
- `"u"` → `"you"`
- `"rly"` → `"really"`
- `"lol"` → `"laugh out loud"`

> **注意：BERTモデルは文のコンテキスト（文脈）を理解する設計なので、過度な加工は逆効果になることがあります。基本的にはTokenizerに任せるのが良いです。**

## step4 モデルのロードと準備
	•	Hugging Face Hub から事前学習済みモデルをロード
	•	タスクに合わせて AutoModelForSequenceClassification、CausalLM、TokenClassificationなど選択

## step5 Trainer を使ったファインチューニング
    •   Trainer は Hugging Face 提供の便利な学習フレームワーク
    •   Hugging Face の Trainer を使うためには、torch.utils.data.Dataset 型に変換する必要があります。

## step6 評価と予測
	•	trainer.evaluate() を使ってモデルを評価
	•	trainer.predict() で推論
	•	必要に応じて精度、F1スコア、混同行列などを可視化

## step7 モデル保存・アップロード
	•	trainer.save_model() でローカル保存
	•	Hugging Face Hub にアップロード（共有・デプロイ用）

## step8 推論・デプロイ(Optional)
	•	Streamlit, Gradio, FastAPI などで簡易Webアプリ化
	•	pip install gradio でインタラクティブに使えるUIが簡単に作れます
