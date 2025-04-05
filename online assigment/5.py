def is_overlapping(schedule1, schedule2):
    for start1, end1 in schedule1:
        for start2, end2 in schedule2:
            if start1 < end2 and start2 < end1:
                return True
    return False

schedule1 = [(1, 3), (5, 6), (7, 9)]
schedule2 = [(2, 4), (6, 8)]

if is_overlapping(schedule1, schedule2):
    print("Schedules overlap")
else:
    print("Schedules do not overlap")