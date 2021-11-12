﻿## Лабораторная работа "Эхо-сервер". Практикум по программированию
### **Цель работы**
Познакомиться с приемами работы с сетевыми сокетами в языке программирования Python.
### **Задания для самостоятельного выполнения**
1.Модифицируйте код сервера таким образом, чтобы при разрыве соединения клиентом он продолжал слушать данный порт и, таким образом, был доступен для повторного подключения. По логам можно заметить, что клиент отключался, а потом вновь подключался к серверу:

![image](https://user-images.githubusercontent.com/70803921/141524326-e658058f-4b3e-461d-97a3-d1684c30fdd1.png)

По логам видно, что пользователь подключился несколько раз.

2.Модифицируйте код клиента и сервера таким образом, чтобы номер порта и имя хоста (для клиента) они спрашивали у пользователя. Реализовать безопасный ввод данных и значения по умолчанию.

Если правильные значения или по умолчанию:

![image](https://user-images.githubusercontent.com/70803921/141524408-68d55464-68a4-4375-93c8-e7504fe5dd95.png)

Неправильные значения:

![image](https://user-images.githubusercontent.com/70803921/141524470-e221b7a5-89b5-4273-a8ea-44ac49ec3978.png)

3.Модифицировать код сервера таким образом, чтобы все служебные сообщения выводились не в консоль, а в специальный лог-файл.

![image](https://user-images.githubusercontent.com/70803921/141524517-ec6ff27e-d40a-445e-8be5-5d88961b7114.png)

4.Модифицируйте код сервера таким образом, чтобы он автоматически изменял номер порта, если он уже занят. Сервер должен выводить в консоль номер порта, который он слушает.

![image](https://user-images.githubusercontent.com/70803921/141526011-54eed395-b6db-475f-9ccc-10660ca2d1fd.png)
![image](https://user-images.githubusercontent.com/70803921/141526055-f0b811bc-21fb-46eb-88b1-d2e7dd5a6a1f.png)

5.Реализовать сервер идентификации. Сервер должен принимать соединения от клиента и проверять, известен ли ему уже этот клиент (по IP-адресу). Если известен, то поприветствовать его по имени. Если неизвестен, то запросить у пользователя имя и записать его в файл. Файл хранить в произвольном формате.

![image](https://user-images.githubusercontent.com/70803921/141524683-32b99653-fece-4e92-8835-0a6358848019.png)

Так как новый пользователь, нас сервер спрашивает имя и пароль. 

При повторном подключении:

![image](https://user-images.githubusercontent.com/70803921/141524734-7690e740-2258-4cf9-9367-21ea8760fe3f.png)

6.Реализовать сервер аутентификации. Похоже на предыдущее задание, но вместе с именем пользователя сервер отслеживает и проверяет пароли. Дополнительные баллы за безопасное хранение паролей. Дополнительные баллы за поддержание сессии на основе токена наподобие cookies

![image](https://user-images.githubusercontent.com/70803921/141524906-dc40a8b2-2a17-4b9f-b3c5-cbef07fdcfe6.png)

Сервер не спрашивает пароль и логин так как у профиля сохранён токен.

![image](https://user-images.githubusercontent.com/70803921/141524951-193fae15-c130-46d8-8fb8-a5da5f2908aa.png)

К каждому паролю создается уникальный ключ

![image](https://user-images.githubusercontent.com/70803921/141524989-4d6fe7a3-0eb7-47d0-b7cc-a680885bc899.png)

Если удалить токен, то автоматически вход не выполнится и программа запросит пароль(если ввести неправильный пароль, то сервер выдаст, что пароль неправильный)

![image](https://user-images.githubusercontent.com/70803921/141525043-07fa64a8-597c-45c8-8d51-a8ebf28ff330.png)

**Если ввести верный пароль** 

![image](https://user-images.githubusercontent.com/70803921/141525086-869406c3-1cd5-40eb-99ec-531d506f618e.png)

7.Напишите вспомогательные функции, которые реализуют отправку и принятие текстовых сообщений в сокет. Функция отправки должна дополнять сообщение заголовком фиксированной длины, в котором содержится информация о длине сообщения. Функция принятия должна читать сообщение с учетом заголовка. В дополнении реализуйте преобразование строки в байтовый массив и обратно в этих же функциях. Дополнително оценивается, если эти функции будут реализованы как унаследованное расширение класса socket библиотеки socket.

![image](https://user-images.githubusercontent.com/70803921/141525121-fcd57099-a27a-41d8-8735-0c7cf9c56e20.png)
![image](https://user-images.githubusercontent.com/70803921/141525149-4075d399-0660-4920-b9c2-6b343bbce1f8.png)


8.Дополните код клиента и сервера таким образом, чтобы они могли посылать друг другу множественные сообщения один в ответ на другое.

![image](https://user-images.githubusercontent.com/70803921/141525180-7523ae63-457f-4879-93e8-f38959b33eb3.png)

Клиент отправляет одно сообщение сервер в ответ 4 
