from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected
    
def test_no_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00")
    expected = []
    assert compute_overlap_time(range1, range2) == expected
    
def test_multiple_overlaps():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2)
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00", 2)
    expected = [("2010-01-12 11:00:00", "2010-01-12 12:00:00")]
    assert compute_overlap_time(range1, range2) == expected
    
def test_edge_case_touching_intervals():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    expected = []
    assert compute_overlap_time(range1, range2) == expected