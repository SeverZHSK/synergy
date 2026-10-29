#!/usr/bin/env python3
"""
Кейс-задача № 5 (производственная практика)

Генерирует HTML-страницу с заголовком "Наименование организации, на базе
которой проходит практика" и информацией об организации. Стили подключают
основной шрифт и дают переключатель из 5 дополнительных вариантов шрифта.

ВАЖНО про "официальный шрифт компании": открытого брендбука с фирменным
шрифтом Университета/Корпорации «Синергия» найти не удалось (сайты
synergy.ru и corporation.synergy.ru о типографике ничего не сообщают, а
инструменты этой сессии не дают прочитать их CSS напрямую). Поэтому ниже
используется ПРЕДПОЛАГАЕМЫЙ шрифт (Montserrat) как нейтральный вариант
современного корпоративного рубленого шрифта — это явно помечено и в коде,
и в самой странице. Если у вас есть реальный бренд-гайд компании — замените
PRIMARY_FONT и подпись ниже.
"""

ORG_FULL_NAME = 'Автономная некоммерческая организация высшего образования «Московский университет «Синергия»'
ORG_SHORT_NAME = 'Университет «Синергия»'

PRIMARY_FONT = "Montserrat"
PRIMARY_FONT_NOTE = (
    "официальный фирменный шрифт компании в открытых источниках не найден; "
    "здесь — предполагаемый вариант, замените на реальный при наличии брендбука"
)

# 5 дополнительных вариантов шрифта, как просит задание
ALT_FONTS = ["Roboto", "Open Sans", "PT Sans", "Inter", "Golos Text"]

ABOUT_PARAGRAPHS = [
    (
        "Полное официальное название — " + ORG_FULL_NAME + "; сокращённое — "
        + ORG_SHORT_NAME + ". Организационно-правовая форма — автономная "
        "некоммерческая организация (АНО). Университет входит в "
        "Корпорацию «Синергия» — EdTech-холдинг, объединяющий более 50 "
        "компаний в сфере образования, digital-маркетинга, "
        "event-менеджмента и смежных направлений."
    ),
    (
        "Основные услуги: высшее образование (бакалавриат, магистратура), "
        "среднее профессиональное образование (колледж), дополнительное "
        "профессиональное образование и переподготовка, MBA-программы "
        "(Школа Бизнеса «Синергия»), корпоративное обучение — всего более "
        "1000 образовательных программ."
    ),
    (
        "Территориальное размещение: головной офис и приёмные комиссии в "
        "Москве (Сокол, Семёновская, Охотный ряд, ВДНХ); представительства "
        "в регионах России (в т.ч. Санкт-Петербург, Екатеринбург, Уфа, "
        "Сыктывкар) и за рубежом (в т.ч. Ош); зарубежный кампус бизнес-школы "
        "в Дубае; программы двойного диплома с партнёрами в Сербии и Китае."
    ),
    (
        "Факультет, на базе которого выполняется индивидуальное задание — "
        "факультет информационных технологий."
    ),
]

SOURCES = [
    ("synergy.ru — приёмная комиссия (Ош)", "https://synergy.ru/about/branches/osh"),
    ("corporation.synergy.ru — о корпорации", "https://www.corporation.synergy.ru/"),
    ("corporation.synergy.ru — структура", "https://www.corporation.synergy.ru/structure"),
]


def build_html() -> str:
    alt_options = "\n".join(
        f'        <option value="{f}">{f}</option>' for f in ALT_FONTS
    )
    about_html = "\n".join(f"      <p>{p}</p>" for p in ABOUT_PARAGRAPHS)
    sources_html = "\n".join(
        f'        <li><a href="{url}" target="_blank" rel="noopener">{label}</a></li>'
        for label, url in SOURCES
    )

    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{ORG_SHORT_NAME}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&amp;family=Roboto:wght@400;700&amp;family=Open+Sans:wght@400;700&amp;family=PT+Sans:wght@400;700&amp;family=Inter:wght@400;700&amp;family=Golos+Text:wght@400;700&amp;display=swap" rel="stylesheet">
<style>
  :root {{
    --font-current: "{PRIMARY_FONT}", sans-serif;
    --bg: #ffffff;
    --fg: #1a1a1a;
    --accent: #c8102e;
    --muted: #6b6b6b;
    --border: #e4e4e4;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --bg: #15161a;
      --fg: #f1f1f1;
      --muted: #a3a3a3;
      --border: #30323a;
    }}
  }}
  :root[data-theme="dark"] {{
    --bg: #15161a;
    --fg: #f1f1f1;
    --muted: #a3a3a3;
    --border: #30323a;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 32px max(16px, (100% - 760px) / 2);
    background: var(--bg);
    color: var(--fg);
    font-family: var(--font-current);
    line-height: 1.55;
  }}
  h1 {{
    font-weight: 700;
    font-size: 1.9rem;
    margin: 0 0 4px;
    color: var(--accent);
  }}
  .subtitle {{
    color: var(--muted);
    margin: 0 0 24px;
    font-size: 0.95rem;
  }}
  .font-picker {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0 0 28px;
    padding: 12px 14px;
    border: 1px solid var(--border);
    border-radius: 10px;
  }}
  .font-picker label {{ font-size: 0.9rem; color: var(--muted); }}
  .font-picker select {{
    font: inherit;
    padding: 6px 10px;
    border-radius: 6px;
    border: 1px solid var(--border);
    background: var(--bg);
    color: var(--fg);
  }}
  .font-note {{
    font-size: 0.82rem;
    color: var(--muted);
    margin-top: -18px;
    margin-bottom: 24px;
  }}
  p {{ margin: 0 0 14px; }}
  ul {{ padding-left: 20px; }}
  footer {{
    margin-top: 32px;
    padding-top: 16px;
    border-top: 1px solid var(--border);
    font-size: 0.82rem;
    color: var(--muted);
  }}
</style>
</head>
<body>
  <h1>{ORG_SHORT_NAME}</h1>
  <p class="subtitle">Наименование организации, на базе которой проходит практическая подготовка</p>

  <div class="font-picker">
    <label for="font-select">Шрифт:</label>
    <select id="font-select">
      <option value="{PRIMARY_FONT}" selected>{PRIMARY_FONT} (по умолчанию)</option>
{alt_options}
    </select>
  </div>
  <p class="font-note">Шрифт «{PRIMARY_FONT}» использован как предполагаемый — {PRIMARY_FONT_NOTE}. Переключатель выше показывает ещё {len(ALT_FONTS)} вариантов.</p>

  <main>
{about_html}
  </main>

  <footer>
    <p>Источники:</p>
    <ul>
{sources_html}
    </ul>
  </footer>

<script>
  document.getElementById('font-select').addEventListener('change', function (e) {{
    document.documentElement.style.setProperty('--font-current', '"' + e.target.value + '", sans-serif');
  }});
</script>
</body>
</html>
"""


if __name__ == "__main__":
    html = build_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Сгенерировано: index.html")
