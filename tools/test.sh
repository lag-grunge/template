set -x

curl -X 'POST' \
'http://localhost:8080/create_form/?name=template_2&phone=%2b7%20930%20888%2088&email=12%40mail%2eru' \

curl -X 'POST' \
'http://localhost:8080/get_form/?phone=%2b7%20931%20888%2088&email=12%40a.ru&phone_2=%2b7%20931%20888%2089' \

curl -X 'POST' \
'http://localhost:8080/get_form/?phone=%2b7%20931%20888%2088&email=12%40a.ru' \

curl -X 'POST' \
'http://localhost:8080/get_form/?phone=%2b7%20931%20888%2088&email=12%40a.ru&date=2023-11-20'

curl -X 'PUT' \
'http://localhost:8080/update_form/?name=template_2&phone=%2b7%20931%20888%2088&email=12%40a.ru&date=30.11.2023'

curl -X 'POST' \
'http://localhost:8080/get_form/?phone=%2b7%20931%20888%2088&email=12%40a.ru&date=2023-11-20'


