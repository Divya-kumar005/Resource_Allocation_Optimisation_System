Resource Allocation Scheduler
 Project Overview

This project builds a Resource Allocation Scheduler that assigns tasks to limited daily working hours (for example, 8 hours per day).

The goal is to:

Select and schedule tasks in a way that maximizes total priority while respecting all constraints.

The scheduler generates:

A 7-day task plan

Total priority achieved

List of unscheduled tasks with reasons

Problem Statement

We are given:

A list of tasks, where each task has:

Priority score

Effort (hours required)

Deadline (day number)

Dependencies (optional)

Fixed daily capacity (e.g., 8 hours per day)

A planning period (e.g., 7 days)

The objective is:

Maximize total priority while ensuring all constraints are satisfied.

Features Implemented

 Daily capacity is never exceeded
 Tasks are completed before their deadline
 Task dependencies are enforced
 Circular dependencies are detected
 Tasks closer to deadline are prioritized
 Daily optimization using Knapsack algorithm
 Clear reporting of unscheduled tasks

 Approach Used

The scheduler uses a combination of smart rules (heuristics) and optimization techniques.

 Step 1: Handle Dependencies

Before scheduling, tasks are arranged using Topological Sort.

This ensures:

A task is never scheduled before its dependency.

Circular dependencies are detected and rejected.

Example:

If T2 depends on T1, then T1 will always come before T2.

 Step 2: Calculate Task Score

Each task is given a dynamic score:

Score = (Priority / Effort)
        + Urgency
        - Dependency Penalty

What each part means:

Priority / Effort → Measures how valuable the task is compared to time required.

Urgency → Increases as the deadline gets closer.

Dependency penalty → Reduces score if dependencies are not completed.

Urgency is calculated as:

Urgency = 1 / (Days Remaining)


This means tasks closer to their deadline become more important.

Step 3: Daily Optimization Using Knapsack

Instead of simply picking tasks one by one, the system uses the 0/1 Knapsack algorithm every day.
knapsack ensures the best combination of tasks is selected for each day.

 Step 4: Build the Schedule

For each day:

Select valid tasks:

Deadline not passed

Dependencies completed

Apply knapsack optimization

Assign selected tasks

Update completed task list

Move to next day