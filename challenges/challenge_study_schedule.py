def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    students = 0
    for period in permanence_period:
        if not period[0] or not period[1] \
                or type(period[0]) == str or type(period[1]) == str:
            return None
        if period[0] <= target_time <= period[1]:
            students += 1
    return students
