def find_optimal_schedule(jobs):
 2 
 
    n = len(jobs)
 3 
 
    job_order = sorted(range(n), key=lambda x: -jobs[x][1] / jobs[x][0])  # Sort jobs in descending order
 4 
 
    # of profit/duration ratio
 5 
 
    schedule = []
 6 
 
    for job_index in job_order:
 7 
 
        schedule.append(jobs[job_index])
 8 
 
        total_time = sum(job[0] for job in schedule)
 9 
 
        if total_time > jobs[job_index][1]:
 10 
 
            schedule.remove(jobs[job_index])  # Remove the job if adding it exceeds the allowed time
 11 
 
    return schedule
 12 
 
 13 
 
def display_schedule(schedule):
 14 
 
    total_time = sum(job[0] for job in schedule)
 15 
 
    total_profit = sum(job[1] for job in schedule)
 16 
 
    print("Optimal Schedule:")
 17 
 
    for index, job in enumerate(schedule):
 18 
 
        print(f"Job {index + 1}: Duration={job[0]}, Profit={job[1]}")
 19 
 
    print(f"\nTotal Time: {total_time}")
 20 
 
    print(f"Total Profit: {total_profit}")
 21 
 
 22 
 
# Example usage
 23 
 
jobs = [(3, 5), (4, 6), (2, 2), (1, 8), (5, 10)]  # Format: (duration, profit)
 24 
 
optimal_schedule = find_optimal_schedule(jobs)
 25 
 
display_schedule(optimal_schedule)
