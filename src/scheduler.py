def compute_score(task, completed, planning_days, alpha=2.0, beta=1.5):
    priority = task["priority"]
    effort = task["effort"]
    deadline = task["deadline"]
    dependencies = task["dependencies"]

    # Base score
    base = priority / effort

    # Urgency factor
    urgency = (planning_days - deadline + 1) / planning_days
    urgency_weight = alpha * urgency

    # Dependency penalty
    unmet_dependencies = sum(1 for d in dependencies if d not in completed)
    dependency_penalty = beta * unmet_dependencies

    return base + urgency_weight - dependency_penalty


def schedule_tasks(data):
    daily_capacity = data["daily_capacity"]
    planning_days = data["planning_days"]
    tasks = data["tasks"]

    completed = set()
    schedule = {day: [] for day in range(1, planning_days + 1)}
    total_priority = 0
    unscheduled = []

    remaining_tasks = tasks.copy()

    for day in range(1, planning_days + 1):
        capacity = daily_capacity

        # Filter tasks that:
        # - Not completed
        # - Deadline not exceeded
        available_tasks = [
            t for t in remaining_tasks
            if t["id"] not in completed and t["deadline"] >= day
        ]

        # Compute score dynamically
        available_tasks.sort(
            key=lambda t: compute_score(t, completed, planning_days),
            reverse=True
        )

        for task in available_tasks:
            task_id = task["id"]
            effort = task["effort"]

            # Check dependencies satisfied
            if all(dep in completed for dep in task["dependencies"]):
                if effort <= capacity:
                    schedule[day].append(task_id)
                    completed.add(task_id)
                    total_priority += task["priority"]
                    capacity -= effort

        remaining_tasks = [t for t in remaining_tasks if t["id"] not in completed]

    # Remaining tasks → unscheduled
    for task in remaining_tasks:
        reason = "Dependency not completed"
        if any(dep not in completed for dep in task["dependencies"]):
            reason = "Dependency not completed"
        else:
            reason = "Insufficient capacity or deadline exceeded"
        unscheduled.append((task["id"], reason))

    return schedule, total_priority, unscheduled
