
from src.dates_helper import get_dates_in_interval
from src.dates_helper import get_default_date_data


def test_get_dates_in_interval_returns_singleelement_list():
    start_date = '9/12/2022'
    end_date = '9/12/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is not None, 'Expected non null list'
    assert '9/12/2022' in dates, f'Expected {start_date} in list'
    # ejecutar desde la raiz
    # pytest para ejecutar


def test_get_dates_in_interval_returns_none():
    start_date = None
    end_date = None

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None


def test_get_dates_in_interval_period_days():
    start_date = '9/12/2022'
    end_date = '9/15/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert '9/12/2022' in dates
    assert '9/13/2022' in dates
    assert '9/14/2022' in dates
    assert '9/15/2022' in dates


def test_get_dates_in_interval_start_date_greater():
    start_date = '9/15/2022'
    end_date = '9/10/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None


def test_get_default_date_data_participants():
    start_date = '9/12/2022'
    end_date = '9/12/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '9/12/2022', 'participants': -99999} in dates


def test_get_default_date_data_default_value_none():
    start_date = '9/12/2022'
    end_date = '9/15/2022'
    default_value = None

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '9/12/2022', 'participants': None} in dates
    assert {'date': '9/13/2022', 'participants': None} in dates
    assert {'date': '9/14/2022', 'participants': None} in dates
    assert {'date': '9/15/2022', 'participants': None} in dates


def test_get_default_date_data_completed():
    start_date = '9/12/2022'
    end_date = '9/15/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '9/12/2022', 'participants': -99999} in dates
    assert {'date': '9/13/2022', 'participants': -99999} in dates
    assert {'date': '9/14/2022', 'participants': -99999} in dates
    assert {'date': '9/15/2022', 'participants': -99999} in dates


def test_get_default_date_data_return():
    start_date = '9/15/2022'
    end_date = '9/10/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert len(dates) == 0


def test_get_default_date_data_date_none():
    start_date = None
    end_date = None
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert len(dates) == 0
