import re
from nltk.corpus import stopwords
import pymorphy2

IS_NORMALIZE = True
import nltk
nltk.download('stopwords')
STOP_WORDS = stopwords.words("russian")
STOP_WORDS_MONTHS = ['сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'январь', 'февраль', 'март', 'апрель', 'март', 'май',
                     'июнь', 'июль', 'август']
STOP_WORDS += STOP_WORDS_MONTHS
STOP_WORDS = set(STOP_WORDS)

morph = pymorphy2.MorphAnalyzer()


def get_text_on_pattern_replacement_func(html_text: str) -> str:
    patterns_to_replace = {
        '&nbsp;|&ndash;': ' ',  # замена пробела(&nbsp;) на пробел
        r'<.+?>|\\n|&[a-z]+;': '',  # замена всех тэгов, /n и выражений типа &ldquo; на пустую строку
        r'\s+': ' ',  # замена всех повторяющихся пробелов на один
        r'(.\.)(\S)': r'\g<1> \g<2>',  # добавление пробела после конца предложения, если дальше нет пробела и начинается буква
        r'\s+$': '',   # удаление пробелов с конца строки
        r'(.\.)\s(ru)': r'\g<1>\g<2>',  # если после любого символа идет точка и пробел и за ним ru, то уберет пробел
        r'([а-я])([А-Я])': r'\g<1>. \g<2>',  # если после а-я (low) большие А-Я (high), между ними вставит точку и пробел
    }

    for pattern, repl in patterns_to_replace.items():
        html_text = re.sub(pattern, repl, html_text)
    return html_text


def get_lst_of_normalized_tokens_without_stopwords(text, is_normalize=IS_NORMALIZE):
    pattern = re.compile(r"([-\s.,;!?])+")
    tokens = pattern.split(text)
    tokens = [x for x in tokens if
              x not in STOP_WORDS and x not in '- \t\n.,;!?' and not x[0].isupper() and len(x) > 2 and x.isalpha()]
    if is_normalize:
        first_filter = [morph.normal_forms(x)[0] for x in tokens]
        return [x for x in first_filter if x not in STOP_WORDS]

    return tokens

# текст сразу?