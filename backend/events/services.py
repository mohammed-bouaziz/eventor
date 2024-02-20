
def _get_duration(start_time, end_time):
    minutes = None
    if end_time and start_time:
            duration_time = end_time - start_time
            total_seconds = duration_time.total_seconds()
            minutes = total_seconds / 60
            minutes = round(minutes, 2)
    return minutes