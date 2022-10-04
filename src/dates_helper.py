import datetime


def get_dates_in_interval(start_date, end_date):
    if start_date is None:
        return
    start = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    # print((end-start).days)
    if (end-start).days < 0:
        return None
    else:
        date_generated = [
            start + datetime.timedelta(days=x) for x in range(0, (end-start).days + 1)]
        # print(date_generated,type(date_generated))
        result = []
        for date in date_generated:
            result.append(date.strftime("%m/%d/%Y").lstrip('0'))
            # print(date.strftime("%m/%d/%Y").lstrip('0'))
        return result


def get_default_date_data(start_date, end_date, default_value):
    result = []
    if get_dates_in_interval(start_date, end_date) is None:
        return result     
    for date in get_dates_in_interval(start_date, end_date):
        dictionary = {}
        dictionary['date'] = date
        dictionary['participants'] = default_value
        result.append(dictionary)
    print(result)
    return result

