import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from rules import create_rules

# --- Define fuzzy variables ---

# Inputs
sleep_duration = ctrl.Antecedent(np.arange(0, 3, 1), 'sleep_duration')  # 0: Short, 1: Ideal, 2: Long
screen_time = ctrl.Antecedent(np.arange(0, 3, 1), 'screen_time')        # 0: Minimum, 1: Moderate, 2: Extensive
stress_level = ctrl.Antecedent(np.arange(0, 3, 1), 'stress_level')      # 0: Low, 1: Medium, 2: High
room_environment = ctrl.Antecedent(np.arange(0, 3, 1), 'room_environment')  # 0: Poor, 1: Moderate, 2: Optimal

# Output
sleep_quality = ctrl.Consequent(np.arange(0, 5, 1), 'sleep_quality')  # 0: Poor, 1: Fair, 2: Good, 3: Very Good, 4: Excellent

# --- Define membership functions ---

# Sleep Duration
sleep_duration['short'] = fuzz.trimf(sleep_duration.universe, [0, 0, 1])
sleep_duration['ideal'] = fuzz.trimf(sleep_duration.universe, [0, 1, 2])
sleep_duration['long'] = fuzz.trimf(sleep_duration.universe, [1, 2, 2])

# Screen Time
screen_time['minimum'] = fuzz.trimf(screen_time.universe, [0, 0, 1])
screen_time['moderate'] = fuzz.trimf(screen_time.universe, [0, 1, 2])
screen_time['extensive'] = fuzz.trimf(screen_time.universe, [1, 2, 2])

# Stress Level
stress_level['low'] = fuzz.trimf(stress_level.universe, [0, 0, 1])
stress_level['medium'] = fuzz.trimf(stress_level.universe, [0, 1, 2])
stress_level['high'] = fuzz.trimf(stress_level.universe, [1, 2, 2])

# Room Environment
room_environment['poor'] = fuzz.trimf(room_environment.universe, [0, 0, 1])
room_environment['moderate'] = fuzz.trimf(room_environment.universe, [0, 1, 2])
room_environment['optimal'] = fuzz.trimf(room_environment.universe, [1, 2, 2])

# Sleep Quality
sleep_quality['poor'] = fuzz.trimf(sleep_quality.universe, [0, 0, 1])
sleep_quality['fair'] = fuzz.trimf(sleep_quality.universe, [0, 1, 2])
sleep_quality['good'] = fuzz.trimf(sleep_quality.universe, [1, 2, 3])
sleep_quality['very_good'] = fuzz.trimf(sleep_quality.universe, [2, 3, 4])
sleep_quality['excellent'] = fuzz.trimf(sleep_quality.universe, [3, 4, 4])

# --- Get rules from rules.py ---
rules = create_rules(sleep_duration, screen_time, stress_level, room_environment, sleep_quality)

# --- Controller setup ---
def get_fuzzy_controller():
    quality_ctrl = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(quality_ctrl)

# Recommendation mapping
recommendation_mapping = {
    "poor": [
        "Consider developing a calming evening routine to wind down before bed. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Minimize distractions in your sleeping space to improve restfulness. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Engage in relaxing activities like journaling or reading before sleep. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Explore mindfulness practices to promote mental calmness before bedtime. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Stay consistent with your bedtime and wake-up time, even on weekends. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep."
    ],
    "fair": [
        "Small improvements can lead to better sleep. Focus on winding down earlier. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Aim to reduce overstimulation in the evening for a smoother sleep transition. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Keep your sleep environment tidy and free of noise or bright lights. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Try light stretching or relaxation exercises before bed. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Explore gentle evening routines to support deeper sleep. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep."
    ],
    "good": [
        "You're maintaining a solid foundation. Keep observing your sleep habits. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Look for small enhancements like adjusting lighting or room temperature. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Maintain consistency with your sleep schedule throughout the week. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Incorporate moments of calm during your day to promote better nighttime rest. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep.",
        "Consider winding down with non-digital activities in the evening. Try to balance sleep duration, screen time before bed, stress level, and room environment for better sleep."
    ],
    "very_good": [
        "You're doing great! Minor tweaks can elevate your rest even more.",
        "Continue reinforcing your healthy habits with regular routines.",
        "Ensure your bedroom setup continues to feel relaxing and comfortable.",
        "Keep prioritizing relaxation before bed — it’s clearly working.",
        "Be mindful of late-day stressors and how they might impact your sleep."
    ],
    "excellent": [
        "Fantastic sleep quality! You're the sleep champion!",
        "Share your sleep strategies — others can learn from you.",
        "Use your well-rested energy to fuel positive habits throughout the day.",
        "Celebrate your success and aim to keep consistency long-term!"
    ]
}



# Track recommendation rotation
recommendation_index_tracker = {key: 0 for key in recommendation_mapping.keys()}

def get_recommendation(quality_level):
    """Retrieve the next recommendation for a given quality level."""
    if quality_level.lower() not in recommendation_mapping:
        return "No specific recommendation available."
    
    index = recommendation_index_tracker[quality_level.lower()]
    recommendation = recommendation_mapping[quality_level.lower()][index]
    recommendation_index_tracker[quality_level.lower()] = (index + 1) % len(recommendation_mapping[quality_level.lower()])
    
    return recommendation
