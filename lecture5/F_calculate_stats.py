def calculate_stats(num):
    t_sum = sum(num)
    average = t_sum / len(num)
    maximum = max(num)
    minimum = min(num)
    return t_sum, average, maximum, minimum

number = [5, 10 ,15, 20, 25]
total , avg, max_num, min_num = calculate_stats(number)
print(f"Total: {total}, Average: {avg}, Maximum: {max_num}, Minimum: {min_num}")