

> db superuser

- root/rootでとりあえず開発中

> templates
    - [x] login後、custom pageに飛ぶ様に開発
    - [o] custom pageでデータをSSRし、jinjaで開発してもらえる様にする。
        - サクッと出来そう。
        https://qiita.com/takuto_neko_like/items/62aeb4271614f6f0347f

- development
    - data送信API実装
    - https://www.django-rest-framework.org/tutorial/1-serialization/
    - 次はここから

- Deploy (11/18に実装予定)
    - [ ] HEROKU上でdocker起動できる様にする
    https://qiita.com/hagyyyy1992/items/466b5bab67118175be65
    - [ ] volumeを使える様にする。

- テスト
    - [ ] postでデータを送信できることを確認する。

- 追加開発
    - [ ] LINE bot に異常時に通知がいく機能を追加する。

【開発メモ】

- dev環境で、依存関係無くpostgresqlを実装できる様にdockerを利用して開発する。
- docker compose でdebugできる。 
    - `docker-compose run web python manage.py makemigrations home_monitoring`
    - `docker-compose run << CONTAINER_NAME >> command`

