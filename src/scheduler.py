def knapsack(tasks, capacity):
    n = len(tasks)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        effort = tasks[i - 1]["effort"]
        priority = tasks[i - 1]["priority"]

        for w in range(capacity + 1):
            if effort <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - effort] + priority
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(tasks[i - 1])
            w -= tasks[i - 1]["effort"]

    return selected

def compute_score(task, completed, planning_days, current_day, alpha=2.0, beta=1.5):
    priority = task["priority"]
    effort = task["effort"]
    deadline = task["deadline"]
    dependencies = task["dependencies"]

    base = priority / effort

    days_left = deadline - current_day + 1
    urgency = 1 / days_left if days_left > 0 else 0
    urgency_weight = alpha * urgency

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

        available_tasks = [
            t for t in remaining_tasks
            if t["id"] not in completed
            and t["deadline"] >= day
            and all(dep in completed for dep in t["dependencies"])
        ]

        available_tasks.sort(
            key=lambda t: compute_score(t, completed, planning_days, day),
            reverse=True
        )

        
        selected_tasks = knapsack(available_tasks, daily_capacity)

        for task in selected_tasks:
            schedule[day].append(task["id"])
            completed.add(task["id"])
            total_priority += task["priority"]

        remaining_tasks = [t for t in remaining_tasks if t["id"] not in completed]

    for task in remaining_tasks:
        if any(dep not in completed for dep in task["dependencies"]):
            reason = "Dependency not completed"
        elif task["deadline"] < planning_days:
            reason = "Deadline missed"
        else:
            reason = "Insufficient capacity"
        unscheduled.append((task["id"], reason))

    return schedule, total_priority, unscheduled
