import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
import re

# Load the dataset
df = pd.read_csv('data_finale.csv')

# Clean and standardize the 'Workout Name' column
df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'Push.*', 'Push', x.strip()))
df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'Legs.*', 'Legs', x.strip()))
df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'Pull.*', 'Pull', x.strip()))

# Check unique workout names
print("Unique Workout Names:", df['Workout Name'].unique())

# Function to plot progress
def plot_progress(workout_name, exercise_name):
    print(f"Filtering data for Workout: {workout_name}, Exercise: {exercise_name}")
    filter_df = df[(df['Workout Name'] == workout_name) & (df['Exercise Name'] == exercise_name)]
    
    if filter_df.empty:
        print("No data available for the selected workout and exercise.")
        return

    print(f"Filtered Data:\n{filter_df.head()}")

    plt.figure(figsize=(14, 7))
    sns.lineplot(x='Set Order', y='Weight', data=filter_df, marker='o')
    plt.title(f'Weight Progress for {exercise_name}')
    plt.xlabel('Set Order')
    plt.ylabel('Weight')
    plt.show()

    plt.figure(figsize=(14, 7))
    sns.boxplot(x='Set Order', y='Weight', data=filter_df)
    plt.title(f'Distribution of Weights by Set Order for {exercise_name}')
    plt.xlabel('Set Order')
    plt.ylabel('Weight')
    plt.show()

    filter_df['Total Weight'] = filter_df['Weight'] * filter_df['Reps']
    plt.figure(figsize=(14, 7))
    sns.barplot(x='Set Order', y='Total Weight', data=filter_df, estimator=sum)
    plt.title(f'Total Weight Lifted per Set for {exercise_name}')
    plt.xlabel('Set Order')
    plt.ylabel('Total Weight')
    plt.show()

# Function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Workout Progress Visualizer")

    # Workout Name Dropdown
    workout_label = tk.Label(root, text="Workout Name:")
    workout_label.grid(row=0, column=0, padx=10, pady=10)
    workout_names = df['Workout Name'].unique()
    workout_var = tk.StringVar()
    workout_dropdown = ttk.Combobox(root, textvariable=workout_var, values=workout_names)
    workout_dropdown.grid(row=0, column=1, padx=10, pady=10)

    # Exercise Name Dropdown
    exercise_label = tk.Label(root, text="Exercise Name:")
    exercise_label.grid(row=1, column=0, padx=10, pady=10)
    exercise_var = tk.StringVar()
    exercise_dropdown = ttk.Combobox(root, textvariable=exercise_var)
    exercise_dropdown.grid(row=1, column=1, padx=10, pady=10)

    # Function to update exercises based on selected workout
    def update_exercises(event):
        selected_workout = workout_var.get()
        if isinstance(selected_workout, list):  # Ensure `selected_workout` is a string
            selected_workout = selected_workout[0]
        print(f"Selected Workout: {selected_workout}")  # Debugging line
        exercises = df[df['Workout Name'] == selected_workout]['Exercise Name'].unique()
        print(f"Available Exercises: {exercises}")  # Debugging line
        exercise_dropdown['values'] = exercises
    
    # Bind the update_exercises function to the workout dropdown selection event
    workout_dropdown.bind("<<ComboboxSelected>>", update_exercises)

    # Plot Button
    plot_button = tk.Button(root, text="Plot Progress", command=lambda: plot_progress(workout_var.get(), exercise_var.get()))
    plot_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# Run the GUI
create_gui()
