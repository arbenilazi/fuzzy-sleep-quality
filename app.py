from flask import Flask, render_template, request, jsonify
from fuzzy_system import get_fuzzy_controller, get_recommendation
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

@app.route('/get_sleep_quality', methods=['POST'])
def get_sleep_quality():
    try:
        # Get form values
        sleep_duration = int(request.form['sleepDuration'])      # 0 = Short, 1 = Ideal, 2 = Long
        screen_time = int(request.form['screenTime'])            # 2 = Extensive, 1 = Moderate, 0 = Minimum
        stress_level = int(request.form['stressLevel'])          # 2 = High, 1 = Medium, 0 = Low
        room_environment = int(request.form['roomEnvironment'])  # 0 = Poor, 1 = Moderate, 2 = Optimal

        # Get fuzzy controller
        sim = get_fuzzy_controller()

        # Set input values
        sim.input['sleep_duration'] = sleep_duration
        sim.input['screen_time'] = screen_time
        sim.input['stress_level'] = stress_level
        sim.input['room_environment'] = room_environment

        # Compute the output
        sim.compute()

        # Get crisp result
        output_value = sim.output['sleep_quality']
        
        # Map the numerical output to a quality level
        quality_levels = ["poor", "fair", "good", "very_good", "excellent"]
        quality_index = round(output_value)
        if quality_index < 0:
            quality_index = 0
        elif quality_index >= len(quality_levels):
            quality_index = len(quality_levels) - 1
            
        quality = quality_levels[quality_index]
        
        # Get recommendation based on quality level
        recommendation = get_recommendation(quality)

        return jsonify({
            'sleepQuality': quality.capitalize(),
            'recommendation': recommendation
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
