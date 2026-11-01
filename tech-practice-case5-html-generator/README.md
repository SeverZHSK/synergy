# Кейс-задача № 5 — генератор HTML-страницы об организации

`generate_report_page.py` — программа на Python, которая генерирует
`index.html` с заголовком «Наименование организации, на базе которой Вы
проходите практическую подготовку» и информацией об организации
(Университет «Синергия»).

## Запуск

```bash
python3 generate_report_page.py
# создаст/перезапишет index.html в текущей папке
```

## Шрифты

Страница подключает Google Fonts и по умолчанию показывает текст шрифтом
**Montserrat**.  Рядом с заголовком есть переключатель,
который «на лету» меняет шрифт текста ещё на 5 вариантов: Roboto, Open
Sans, PT Sans, Inter, Golos Text.


## Источники данных об организации

- https://synergy.ru/about/branches/osh
- https://www.corporation.synergy.ru/
- https://www.corporation.synergy.ru/structure
