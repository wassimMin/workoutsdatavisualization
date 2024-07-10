import pandas as pd
import re

# Load the dataset
df = pd.read_csv('weightlifting_721_workouts_standardized1.csv')

# Mapping dictionary to standardize specific workout names
workout_mapping = {
    'Squat 1': 'Legs',
    'Squat': 'Legs',
    'Legs': 'Legs',
    '1 - Heavy Squats': 'Legs',
    '2 - Shoulders ': 'Push',
    'Back': 'Pull',
    'Back Heavier Chins': 'Pull',
    '2 - Back Heavy Chins': 'Pull',
    '1 Heavy   Rows': 'Pull',
    '2 Legs': 'Legs',
    'Back - Heavier Chins': 'Pull',
    'Back - Chins.  5x6': 'Pull',
    'Back - Light Chins, 8-10 Reps': 'Pull',
    'Back - Pyramid.  5max, Decrease 5 Sets': 'Pull',
    'Back Day 1 #4': 'Pull',
    'Back With Deadlift': 'Pull',
    'Back- Heavy 3x8 Chins #7': 'Pull',
    'Back Workout': 'Pull',
    'Squat Light #12': 'Legs',
    'Squat Light #11': 'Legs',
    'Back- Heavy 3x8 Chins #6': 'Pull',
    'Back Day 1 #2': 'Pull',
    'Squat Light #10': 'Legs',
    'Back - Pyramid.  5max, Decrease 5 Sets #26': 'Pull',
    'Squat Light #8': 'Legs',
    'Back Day 1 #1': 'Pull',
    'Back - Pyramid.  5max, Decrease 5 Sets #22': 'Pull',
    'Back - Pyramid.  5max, Decrease 5 Sets #24': 'Pull',
    'Back- Heavy 3x8 Chins #1': 'Pull',
    'Squat Light #2':'Legs',
    'Back - Light Chins, 8-10 Reps #20':'Pull',
    'Back - Light Chins, 8-10 Reps #21':'Pull',
    'Squat Light #3':'Legs',







    



}

df['Workout Name'] = df['Workout Name'].replace(workout_mapping)
df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'.*Push.*', 'Push', x))
df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'.*Legs.*', 'Legs', x))
df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'.*Pull.*', 'Pull', x))


df.to_csv('data_finale.csv', index=False)
