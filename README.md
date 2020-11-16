

> db superuser

- root/rootでとりあえず開発中

> templates
    - [x] login後、custom pageに飛ぶ様に開発
    - [o] custom pageでデータをSSRし、jinjaで開発してもらえる様にする。


- Deploy
    
    - [ ] HEROKU上でdocker起動できる様にする
    - [ ] volumeを使える様にする。

- テスト
    - [ ] postでデータを送信できることを確認する。

- 追加開発
    - [ ] LINE bot に異常時に通知がいく機能を追加する。

【開発メモ】
- docker compose でdebugできる。 
    - `docker-compose run web python manage.py makemigrations home_monitoring`
    - `docker-compose run << CONTAINER_NAME >> command`