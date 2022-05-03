# course_iot
my custom drink detector
Мое небольшое приложение для курсовой работы по IoT

## Инструкция 
Для началаподними Mqtt брокер в данной работе это mosquitto
# Server
Копируем папку server на свой сервер
Для запуска необхходимо поднять свою маквлан сеть(возможен запуск и в сети докера). Инструкция https://blog.oddbit.com/post/2018-03-12-using-docker-macvlan-networks/
Затем билдим образ с помощью docker файла. docker build docker/Dockerfile. -t mosq
После билда запускаем контейнер в нем необходимо настроить переадресации на локальный порт. Для этого используем следующие команды
    iptables -t nat -I PREROUTING -i eth0 -p tcp --dport 1883  -j DNAT --to 127.0.0.1:1883
    sysctl -w net.ipv4.conf.eth0.route_localnet=1
Mqtt брокер готов

# Host-server
Для запуска помещаем папку src на свой хост сервер, из директории src запускаем run.sh файл и создается контейнер с сервером Flask и всем необходимым

# ML-server
Копируем на сервер для ML(желательно наличие видеокарты) файлы из папки ML-server
Для запуска распознавания запускаем convert.py командой "python convert.py"


Для установки python билиотек по папкам лежат файлы requirements
