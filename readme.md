# 環境
* python: 3.10


# 設定
1. 仮想環境を作成する
    ```
    conda create --name python310_streamlit_login_and_signup python=3.10
    conda activate python310_streamlit_login_and_signup
    ```

2. ライブラリをインストールする 
    ```
    pip install -r requirements.txt
    ```

3. .envファイルを作る
    .env_sampleファイルをもとに.envファイルを作成して、Gemini用APIキーを入力する  


# 実行
1. 仮想環境を立ち上げる
    ```
    conda activate python310_streamlit_login_and_signup
    ```

2. Streamlitを実行する
    ```
    streamlit run 1_🏠_Home.py
    ```


# ログインフォーム
* テストユーザ名
    ```
    test_user
    ```

* テストパスワード
    ```
    test_password
    ```

# 新規登録フォーム
製作中