def schedule_tasks(tasks, daily_capacity, planning_days):

   
    tasks_sorted = sorted(
        tasks,
        key=lambda x: x["priority"] / x["effort"],
        reverse=True
    )

    schedule = {day: [] for day in range(1, planning_days + 1)}
    remaining_capacity = {day: daily_capacity for day in range(1, planning_days + 1)}
    completion_day = {}
    unscheduled = []

    for task in tasks_sorted:
        assigned = False

       
        if task["dependencies"]:
            dep_days = []
            for dep in task["dependencies"]:
                if dep not in completion_day:
                    unscheduled.append((task["id"], "Dependency not completed"))
                    assigned = True
                    break
                dep_days.append(completion_day[dep])
            if assigned:
                continue
            earliest_day = max(dep_days) + 1
        else:
            earliest_day = 1

     
        for day in range(earliest_day, min(task["deadline"], planning_days) + 1):
            if remaining_capacity[day] >= task["effort"]:
                schedule[day].append(task["id"])
                remaining_capacity[day] -= task["effort"]
                completion_day[task["id"]] = day
                assigned = True
                break

        if not assigned:
            unscheduled.append((task["id"], "Insufficient capacity or deadline exceeded"))

    total_priority = sum(
        task["priority"]
        for task in tasks
        if task["id"] in completion_day
    )

    return schedule, total_priority, unscheduled
