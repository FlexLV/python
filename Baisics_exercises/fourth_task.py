
days = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
temperatures = []

for i, day in enumerate(days):  
    temp = float(input(f"What is the temperature in {day}? "))
    temperatures.append(temp)

avg = sum(temperatures) / len(temperatures)
print("Average temperature:", avg)
