# HappyBirthdayBot
Telegram-бот для поздравления другого человека с Днем рождения (или любым другим праздником) и запуска для этого человека увлекательного квеста по поиску подарков
Для корректной работы бота необходимо лишь создать файл .env и подставить туда свои переменные из файла sample.env

При запуске бота появляется приветственное сообщение, стикер и кнопка "Начать квест". После запуска квеста бот дает человеку подсказки о том, где искать каждый из подарков (предполагается, что их 4), причем бот каждый раз предлагает человеку написать некое кодовое слово, чтобы перейти к следующему этапу квеста. В моем случае кодовые слова были записаны на бумажках, прикрепленных к подаркам.

После того, как будет найти 4-й подарок, бот присылает финальное сообщение и стикер. Затем идет задержка 30 секунд (предполагается, что человек в это время закроет чат с ботом, уберет телефон и решит, что квест окончен), после чего бот отправляет последнее сообщение, в котором лично я указывала местонахождение ещё одного, пятого подарка.
