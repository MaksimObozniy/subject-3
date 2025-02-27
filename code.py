import smtplib
import os
user = os.environ['LOGIN']
password = os.environ['PASSWORD']
name_user = 'Максим'
website_send = 'https://dvmn.org/referrals/5nX9LqBZR8O7'
friend_name = 'Александр'
email_from = "hy8abyba@yandex.ru"
email_to = "hy8abyba@yandex.ru"


letter = """\
From: {emfrom}
To: {emto}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {fn}! {n} приглашает тебя на сайт {w}!
{w} — это новая версия онлайн-курса по программированию. 
     Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

     Как будет проходить ваше обучение на {w} 

     → Попрактикуешься на реальных кейсах. 
     Задачи от тимлидов со стажем от 10 лет в программировании.
     → Будешь учиться без стресса и бессонных ночей. 
     Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько,
     сколько можешь.
     → Подготовишь крепкое резюме.
     Все проекты — они же решение наших задачек — можно разместить на твоём GitHub.
     Работодатели такое оценят.Регистрируйся → {w}  
     На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу
     на имейл.""".format(fn=friend_name, n=name_user, w=website_send,
                         emfrom=email_from,emto=email_to)

letter = letter.encode('UTF-8')
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(user, password)
server.sendmail(email_from, email_to, letter )
server.quit
