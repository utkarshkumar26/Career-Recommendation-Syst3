# app.py

# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
import pickle  # Ensure pickle is imported
import numpy as np

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Necessary for flashing messages

# Load models and other resources
scaler = pickle.load(open("Models/scaler.pkl", 'rb'))
model = pickle.load(open("Models/model.pkl", 'rb'))
class_names = ['Lawyer', 'Doctor', 'Government Officer', 'Artist', 'Machanical Engineer',
               'Software Engineer', 'Teacher', 'Business Owner', 'Scientist',
               'Banker', 'Writer', 'Accountant', 'Designer',
               'Construction Engineer', 'Game Developer', 'Stock Investor',
               'Real Estate Developer']

# Recommendations function
def Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
                    weekly_self_study_hours, math_score, history_score, physics_score,
                    chemistry_score, biology_score, english_score, geography_score,
                    total_score, average_score):
    # Encode categorical variables
    gender_encoded = 1 if gender.lower() == 'female' else 0
    part_time_job_encoded = 1 if part_time_job else 0
    extracurricular_activities_encoded = 1 if extracurricular_activities else 0

    # Create feature array
    feature_array = np.array([[gender_encoded, part_time_job_encoded, absence_days, extracurricular_activities_encoded,
                               weekly_self_study_hours, math_score, history_score, physics_score,
                               chemistry_score, biology_score, english_score, geography_score, total_score,
                               average_score]])

    # Scale features
    scaled_features = scaler.transform(feature_array)

    # Predict using the model
    probabilities = model.predict_proba(scaled_features)

    # Get top three predicted classes along with their probabilities
    top_classes_idx = np.argsort(-probabilities[0])[:3]
    top_classes_names_probs = [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]

    return top_classes_names_probs

# Route for home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simple login logic (replace with your own logic)
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

# Route for recommendations
@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

# Route for prediction
@app.route('/pred', methods=['POST', 'GET'])
def pred():
    if request.method == 'POST':
        try:
            gender = request.form['gender']
            part_time_job = request.form['part_time_job'] == 'true'
            absence_days = int(request.form.get('absence_days', 0))  # Default to 0 if not provided
            extracurricular_activities = request.form['extracurricular_activities'] == 'true'
            weekly_self_study_hours = int(request.form.get('weekly_self_study_hours', 0))  # Default to 0 if not provided
            math_score = int(request.form.get('math_score', 0))  # Default to 0 if not provided
            history_score = int(request.form.get('history_score', 0))  # Default to 0 if not provided
            physics_score = int(request.form.get('physics_score', 0))  # Default to 0 if not provided
            chemistry_score = int(request.form.get('chemistry_score', 0))  # Default to 0 if not provided
            biology_score = int(request.form.get('biology_score', 0))  # Default to 0 if not provided
            english_score = int(request.form.get('english_score', 0))  # Default to 0 if not provided
            geography_score = int(request.form.get('geography_score', 0))  # Default to 0 if not provided
            total_score = float(request.form.get('total_score', 0.0))  # Default to 0.0 if not provided
            average_score = float(request.form.get('average_score', 0.0))  # Default to 0.0 if not provided

            # Call the recommendations function
            recommendations = Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
                                              weekly_self_study_hours, math_score, history_score, physics_score,
                                              chemistry_score, biology_score, english_score, geography_score,
                                              total_score, average_score)

            return render_template('results.html', recommendations=recommendations)
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('recommend'))

    return render_template('home.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
