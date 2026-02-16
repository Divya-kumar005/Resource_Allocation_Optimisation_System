import os
from input_loader import load_data
from dependency import topological_sort
from scheduler import schedule_tasks
from Reporter import print_report


def main():
    filepath = os.path.join("..", "input", "data.json")

    data = load_data(filepath)

    tasks = data["tasks"]
    daily_capacity = data["daily_capacity"]
    planning_days = data["planning_days"]

    # Resolve dependency order
    sorted_ids = topological_sort(tasks)

    # Reorder tasks
    ordered_tasks = [next(t for t in tasks if t["id"] == tid) for tid in sorted_ids]

    schedule, total_priority, unscheduled = schedule_tasks(data)

    print_report(schedule, total_priority, unscheduled)


if __name__ == "__main__":
    main()
