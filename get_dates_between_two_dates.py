from datetime import datetime, timedelta


def get_dates_between_two_dates(from_date: datetime.date, to_date: datetime.date):
    """
    Get list of string dates between two dates.
    :param from_date: datetime.date, start date (included).
    :param to_date: datetime.date, end date (included).
    :return: List
    """

    dates_between = [from_date]

    diff = (to_date - from_date).days

    for i in reversed(range(diff)):
        day = to_date - timedelta(days=i)
        dates_between.append(day)

    return dates_between


if __name__ == "__main__":

    from_date = datetime(2023, 1, 1).date()
    to_date = datetime.now().date()
    
    r = get_dates_between_two_dates(from_date, to_date)
    
    for d in r:
        print(d)
