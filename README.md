Resource Allocation Scheduler
Project Overview

This project implements a Resource Allocation Scheduler that assigns tasks to limited daily capacity in order to maximize total priority score while respecting:

Daily capacity constraints

Task deadlines

Task dependencies

The system produces a 7-day schedule showing selected tasks, total priority achieved, and unscheduled tasks with reasons.


 Problem Statement

Given:

A list of tasks containing:

Priority score

Effort (hours)

Deadline (day number)

Dependency list (optional)

Fixed daily capacity (e.g., 8 hours/day)

Planning horizon (e.g., 7 days)

The goal is to:

Maximize total priority while ensuring feasibility of schedule.

 Features Implemented

 Daily capacity constraint 
 Deadline constraint
 Dependency ordering 
 Circular dependency detection
 Dynamic urgency handling
 Knapsack-based daily optimization
 Reporting of unscheduled tasks

 Approach Used

The system uses a  Heuristic + Optimization Approach:

Step 1: Dependency Resolution 

Before scheduling, tasks are sorted using Topological Sort to ensure:

A task always appears after its dependencies.

Circular dependencies are detected and rejected.

This guarantees structural correctness.

Step 2: Dynamic Priority Scoring

Each task receives a dynamic score:

Score = (Priority / Effort)
        + Urgency Weight
        - Dependency Penalty

Where:

Priority/Effort → Measures efficiency

Urgency → Increases as deadline approaches

Urgency increases dynamically:

Urgency = 1 / (Days Remaining)


This ensures tasks closer to deadlines are prioritized.

Step 3: Daily Optimization using 0/1 Knapsack

Instead of greedy selection, the scheduler uses 0/1 Knapsack per day:

Objective:

Maximize total priority within daily capacity

Step 4: Schedule Construction

For each day:

Filter valid tasks:

Deadline not passed

Dependencies completed

Apply knapsack optimization

Assign selected tasks

Update completed set