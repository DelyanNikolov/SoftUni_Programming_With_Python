
pool_volume = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
filling_hours = float(input())

filled_water = (first_pipe_debit + second_pipe_debit) * filling_hours
percentage_filled = filled_water / pool_volume * 100
first_pipe_percentage = round((first_pipe_debit * filling_hours) / filled_water * 100, 2)
second_pipe_percentage = 100 - first_pipe_percentage

if pool_volume >= filled_water:
    print(f"The pool is {percentage_filled}% full. "
          f"Pipe 1: {first_pipe_percentage}%. Pipe 2: {second_pipe_percentage}%.")
else:
    print(f"For {filling_hours} hours the pool overflows with {filled_water - pool_volume:.2f} liters.")
