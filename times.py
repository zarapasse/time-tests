import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    total_seconds = (end_time_s - start_time_s).total_seconds()
    total_gap = gap_between_intervals_s * (max(0, number_of_intervals - 1))
    if total_gap >= total_seconds:
        return []
    interval_length_s = (total_seconds - total_gap) / number_of_intervals
    
    ranges = []
    for i in range(number_of_intervals):
        interval_start = start_time_s + datetime.timedelta(seconds=i * (interval_length_s + gap_between_intervals_s))
        interval_end = interval_start + datetime.timedelta(seconds=interval_length_s)
        ranges.append((interval_start.strftime("%Y-%m-%d %H:%M:%S"), interval_end.strftime("%Y-%m-%d %H:%M:%S")))
    return ranges
    

def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            if low < high:
                overlap_time.append((low, high))
    return overlap_time