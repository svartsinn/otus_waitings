from datetime import datetime


def get_timestamp():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return str(int(timestamp))