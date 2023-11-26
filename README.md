# Запуск

```bash
docker compose -f build/docker-compose.yml up --build -d
```

# Тесты


1. Создает форму под названием template_2 с полями phone (тип phone), email (тип email)
2. Запрашивает форму с полями phone (тип phone), email (тип email), phone_2 (тип phone)
3. Запрашивает форму с полями phone (тип phone), email (тип email)
4. Запрашивает форму с полями phone (тип phone), email_2 (тип email)
5. Запрашивает форму с полями phone (тип phone), email (тип email),  date (тип date)
6. Обновляет форму template_2, делает поля phone (тип phone), email (тип email),  date (тип date), info (тип text)
7. Запрашивает форму с полями phone (тип phone), email (тип email),  date (тип date)


```bash
bash tools/test.sh 2>/dev/null
```

Чтобы увидеть в формате команда-ответ, нужно убрать 2>/dev/null
