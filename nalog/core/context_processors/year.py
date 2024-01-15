import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    today_year = datetime.datetime.today().year
    return {
        "year": today_year,
    }
