def check_overlap(event1, event2):
    start1, end1 = event1
    start2, end2 = event2
    return not (end1 <= start2 or end2 <= start1)

def schedule_events(events):
    scheduled_events = []
    for event in events:
        overlap = False
        for scheduled_event in scheduled_events:
            if check_overlap(event, scheduled_event):
                overlap = True
                break
        if not overlap:
            scheduled_events.append(event)
    return scheduled_events

events = [(1, 3), (2, 4), (3, 5), (7, 8)]
scheduled_events = schedule_events(events)
print("Scheduled events:", scheduled_events)