from src.data_processing import load_data

def main():
    # Step 1: データ処理
    train_data = load_data()
    print(train_data)

    # Step 2: モデル作成
    # model = train_model(train_data)

    # Step 3: 評価
    # evaluate_model(model)

if __name__ == "__main__":
    main()