from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data - replace with actual values
    feet_per_second = 12.5
    total_distance = 1250.75
    longest_run = 450.25
    
    return render_template('index.html',
                         speed=feet_per_second,
                         distance=total_distance,
                         duration=longest_run)

if __name__ == '__main__':
    app.run(debug=True)