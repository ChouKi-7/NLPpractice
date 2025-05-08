# NLPpractice

## ディレクトリ構成:





## 実装内容
### データ前処理
load_data()：データ読み込み、いらない列を削除処理
clean_data():データ前処理
            ・小文字変換
            ・url変換
            ・@userに変換処理
            ・space変換処理

tokenize():Twitter専用の事前学習済みBERTモデル「vinai/bertweet-base」のTokenizerを読み込む。
