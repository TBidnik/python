from sys import argv
hours_worked_out, rate_for_the_time, prize = argv
hours_worked_out = int(hours_worked_out)
rate_for_the_time = int(rate_for_the_time)
prize = int(prize)
result = int(hours_worked_out * rate_for_the_time + prize)
print(f"Зраработная плата сотрудника составит - {result}")
