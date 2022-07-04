from datetime import datetime
import pytz

def utc_makassar():
    utc = pytz.timezone('Asia/Makassar')
    datetime_utc = datetime.now(utc)

    return datetime_utc