import matplotlib.pyplot as plt
import numpy as np
import time

# --- Setup ---
# Set the plot to interactive mode (crucial for real-time updates)
plt.ion()

# Create the figure and axes once
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Real-Time Random Number Generation (Normal Distribution)")
ax.set_xlabel("Time Step")
ax.set_ylabel("Generated Value (Random Walk)")
ax.grid(True, linestyle='--', alpha=0.6)

# Initialize data lists
time_steps = []
data_values = []
current_value = 0.0  # Start point for a 'Random Walk'

# Initialize the plot line object (for faster updating)
line, = ax.plot(time_steps, data_values, color='cyan', linewidth=2, alpha=0.8)

print("Plotting started. Close the window to stop the program.")

# --- Main Plotting Loop ---
step_count = 0
while plt.get_fignums():  # Loop continues as long as the figure window is open
    try:
        # 1. Generate New Data
        # Generate a new random step from a standard normal distribution (mean=0, std dev=1)
        random_step = np.random.randn() * 0.5
        current_value += random_step

        # Add the new data point
        time_steps.append(step_count)
        data_values.append(current_value)

        # 2. Update Plot Data
        line.set_xdata(time_steps)
        line.set_ydata(data_values)

        # 3. Auto-scale Axes (crucial for keeping the plot viewable)
        ax.relim()
        ax.autoscale_view()

        # 4. Draw the new frame and flush events
        fig.canvas.draw()
        fig.canvas.flush_events()

        # 5. Wait for a short time (controls update speed)
        time.sleep(0.05)  # Update every 50 milliseconds

        step_count += 1

    except Exception as e:
        # This handles cases where the window is closed forcefully
        # print(f"Plotting stopped due to error: {e}")
        break

plt.ioff()  # Turn off interactive mode
print("Program finished.")