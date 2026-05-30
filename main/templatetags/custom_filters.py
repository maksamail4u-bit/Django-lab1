from django import template
from decimal import Decimal
from datetime import date

register = template.Library()



@register.filter(name='capitalize_name')
def capitalize_name(value):
    if not value:
        return ''
    return ' '.join(word.capitalize() for word in value.split())

@register.filter(name='currency_format')
def currency_format(value):
    try:
        price = Decimal(str(value))
        return f"{price:.2f} ₽"
    except:
        return "0.00 ₽"

@register.filter(name='date_format')
def date_format(value):
    if not value:
        return "Дата не указана"
    return value.strftime("%d.%m.%Y")



@register.simple_tag(name='status_badge')
def status_badge(status):
    if status == "available":
        return "✓ В наличии"
    elif status == "unavailable":
        return "✗ Нет в наличии"
    return "Статус не определен"

@register.simple_tag(name='book_summary')
def book_summary(book):
    if not book:
        return "Нет информации"
    return f"'{book.title}' - {book.author.name}, {book.published_year} г."

@register.simple_tag(name='year_format')
def year_format(year):
    if not year:
        return "Год не указан"
    
    current_year = date.today().year
    age = current_year - int(year)
    
    if age < 0:
        return f"{year} г. (будущее)"
    elif age < 5:
        return f"{year} г. (новинка)"
    elif age < 20:
        return f"{year} г."
    else:
        return f"{year} г. (классика)"