## resume_build_work
![サンプル画像](material/imgs/sample.png "hero")

### 使い方
1 poetryインストール  
2 python3.10をpyenvなどを使って利用できるようにしておく  
3 git clone
```
git clone {this_repository}
```

4 poetry install
```
cd resume_build_work
poetry install
```

5 .envファイルの用意
```
vi env_file/.env
# 以下を記載
API_KEY={write your api key}
USE_MODEL={use model type ex) gpt-4  (他にもgpt3.5-turboとかも指定できるよ)}
```

6 デモ実行
```
cd src
python app.py
```