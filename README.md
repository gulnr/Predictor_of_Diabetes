# YAPILACAKLAR
 1) djongo'yu indirin: https://github.com/nesdis/djongo
 ```
 pip install djongo
 ```
 2) MongoDB'yi indirin: https://www.mongodb.com/download-center/community <br>
 Yapılması gereken özel bir ayar yok, varsayılanları kullanın.

 3) Robo 3T'yi indirin (Studio'ya gerek yok): https://robomongo.org/download

 4) Robo 3T'yi açıp Mongo database'lerini kontrol edin.

 5) Aşağıdakileri yapınca kendisi MongoDB'de "accounts" adında bir database oluşturacak, değişiklik yaptıkça refresh edip görebilirsiniz.
     ```
     python manage.py migrate
     ```
     ```
     python manage.py makemigrations
     ```
     ```
     python manage.py migrate
     ```
     ```
     python manage.py runserver
     ```

