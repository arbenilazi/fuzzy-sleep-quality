import skfuzzy as fuzz
from skfuzzy import control as ctrl

def create_rules(sleep_duration, screen_time, stress_level, room_environment, sleep_quality):
    """
    Create all 81 fuzzy rules for the sleep quality recommendation system.
    
    Args:
        sleep_duration: Antecedent variable for sleep duration
        screen_time: Antecedent variable for screen time
        stress_level: Antecedent variable for stress level
        room_environment: Antecedent variable for room environment
        sleep_quality: Consequent variable for sleep quality
        
    Returns:
        List of all 81 fuzzy rules
    """
    rules = [
        # Rules for sleep_duration = short (27 rules)
        # screen_time = minimum
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['low'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['low'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['low'] & room_environment['optimal'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['medium'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['high'] & room_environment['moderate'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['minimum'] & stress_level['high'] & room_environment['optimal'], sleep_quality['fair']),
        
        # screen_time = moderate
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['low'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['low'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['low'] & room_environment['optimal'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['medium'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['high'] & room_environment['moderate'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['moderate'] & stress_level['high'] & room_environment['optimal'], sleep_quality['poor']),
        
        # screen_time = extensive
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['low'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['low'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['low'] & room_environment['optimal'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['medium'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['high'] & room_environment['moderate'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['short'] & screen_time['extensive'] & stress_level['high'] & room_environment['optimal'], sleep_quality['poor']),
        
        # Rules for sleep_duration = ideal (27 rules)
        # screen_time = minimum
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['low'] & room_environment['poor'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['low'] & room_environment['moderate'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['low'] & room_environment['optimal'], sleep_quality['excellent']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['medium'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['high'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['minimum'] & stress_level['high'] & room_environment['optimal'], sleep_quality['good']),
        
        # screen_time = moderate
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['low'] & room_environment['poor'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['low'] & room_environment['moderate'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['low'] & room_environment['optimal'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['medium'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['high'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['moderate'] & stress_level['high'] & room_environment['optimal'], sleep_quality['good']),
        
        # screen_time = extensive
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['low'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['low'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['low'] & room_environment['optimal'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['medium'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['high'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['ideal'] & screen_time['extensive'] & stress_level['high'] & room_environment['optimal'], sleep_quality['fair']),
        
        # Rules for sleep_duration = long (27 rules)
        # screen_time = minimum
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['low'] & room_environment['poor'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['low'] & room_environment['moderate'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['low'] & room_environment['optimal'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['medium'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['high'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['long'] & screen_time['minimum'] & stress_level['high'] & room_environment['optimal'], sleep_quality['good']),
        
        # screen_time = moderate
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['low'] & room_environment['poor'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['low'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['low'] & room_environment['optimal'], sleep_quality['very_good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['medium'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['high'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['long'] & screen_time['moderate'] & stress_level['high'] & room_environment['optimal'], sleep_quality['fair']),
        
        # screen_time = extensive
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['low'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['low'] & room_environment['moderate'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['low'] & room_environment['optimal'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['medium'] & room_environment['poor'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['medium'] & room_environment['moderate'], sleep_quality['fair']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['medium'] & room_environment['optimal'], sleep_quality['good']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['high'] & room_environment['poor'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['high'] & room_environment['moderate'], sleep_quality['poor']),
        ctrl.Rule(sleep_duration['long'] & screen_time['extensive'] & stress_level['high'] & room_environment['optimal'], sleep_quality['fair']),
    ]
    
    return rules 