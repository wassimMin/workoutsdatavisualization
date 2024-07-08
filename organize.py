import pandas as pd
import re

# Load the dataset
df = pd.read_csv('weightlifting_721_workouts_standardized.csv')

# Mapping dictionary to standardize specific workout names
workout_mapping = {
    'Squat 1': 'Legs',
    'Squat': 'Legs',
    'Legs': 'Legs',
}

df['Workout Name'] = df['Workout Name'].replace(workout_mapping)

df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'Legs.*', 'Legs', x))

df.to_csv('weightlifting_721_workouts_standardized1.csv', index=False)
