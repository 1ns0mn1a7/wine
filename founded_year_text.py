from datetime import datetime


def calculate_age(start_year):
    current_year = datetime.now().year
    return current_year - start_year


def get_years_text(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    last_digit = age % 10
    if last_digit == 1:
        return "год"
    elif 2 <= last_digit <= 4:
        return "года"
    else:
        return "лет"


def get_founded_text(start_year=1920):
    age = calculate_age(start_year)
    word = get_years_text(age)
    return f"Уже {age} {word} с вами"
