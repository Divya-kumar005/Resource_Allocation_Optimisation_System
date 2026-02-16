def print_report(schedule, total_priority, unscheduled):

    print("\n===== 7-Day Schedule =====")
    for day in schedule:
        print(f"Day {day}: {schedule[day]}")

    print("\nTotal Priority Achieved:", total_priority)

    print("\nUnscheduled Tasks:")
    if not unscheduled:
        print("None")
    else:
        for task_id, reason in unscheduled:
            print(f"{task_id} → {reason}")
print("End")