import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import os

# Create the visualisations directory if it doesn't exist
os.makedirs("visualisations", exist_ok=True)

# General plotting function for input variables
def plot_input_membership(x, labels, title, filename):
    plt.figure()
    for i, label in enumerate(labels):
        # Build membership function centered on i
        left = i - 1 if i > 0 else i
        right = i + 1 if i < max(x) else i
        mf = fuzz.trimf(x, [left, i, right])
        plt.plot(x, mf, label=label)
    
    plt.title(f"{title} Membership Functions")
    plt.xlabel('Value')
    plt.ylabel('Membership')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"visualisations/{filename}.png")
    plt.close()

# Input: Sleep Duration (0: Short, 1: Ideal, 2: Long)
x_sleep = np.arange(0, 3, 0.01)
plot_input_membership(x_sleep, ['short', 'ideal', 'long'], "Sleep Duration", "sleep_duration")

# Input: Screen Time Before Bed (0: Minimum, 1: Moderate, 2: Extensive)
x_screen = np.arange(0, 3, 0.01)
plot_input_membership(x_screen, ['minimum', 'moderate', 'extensive'], "Screen Time Before Bed", "screen_time")

# Input: Stress Level (0: Low, 1: Medium, 2: High)
x_stress = np.arange(0, 3, 0.01)
plot_input_membership(x_stress, ['low', 'medium', 'high'], "Stress Level", "stress_level")

# Input: Room Environment (0: Poor, 1: Moderate, 2: Optimal)
x_env = np.arange(0, 3, 0.01)
plot_input_membership(x_env, ['poor', 'moderate', 'optimal'], "Room Environment", "room_environment")

# Output: Sleep Quality (0: Poor, 1: Fair, 2: Good, 3: Very Good, 4: Excellent)
x_quality = np.arange(0, 5, 0.01)
labels_quality = ['poor', 'fair', 'good', 'very_good', 'excellent']
plt.figure()
for i, label in enumerate(labels_quality):
    left = i - 1 if i > 0 else i
    right = i + 1 if i < max(x_quality) else i
    mf = fuzz.trimf(x_quality, [left, i, right])
    plt.plot(x_quality, mf, label=label)

plt.title("Sleep Quality Membership Functions")
plt.xlabel('Value')
plt.ylabel('Membership')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("visualisations/sleep_quality.png")
plt.close()
