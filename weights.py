import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
import re
import matplotlib
from PIL import Image,ImageTk



df = pd.read_csv('data_finale.csv')

df['Workout Name'] = df['Workout Name'].apply(lambda x: re.sub(r'\s+', ' ', x.strip()))
df['Workout Name'] = df['Workout Name'].apply(lambda x: 'Push' if 'Push' in x else x)
df['Workout Name'] = df['Workout Name'].apply(lambda x: 'Legs' if 'Legs' in x else x)
df['Workout Name'] = df['Workout Name'].apply(lambda x: 'Pull' if 'Pull' in x else x)

print("Unique Workout Names:", df['Workout Name'].unique())

def plot_progress(workout_name, exercise_name):
    print(f"Filtering data for Workout: {workout_name}, Exercise: {exercise_name}")
    filter_df = df[(df['Workout Name'] == workout_name) & (df['Exercise Name'] == exercise_name)]
    
    if filter_df.empty:
        print("No data available for the selected workout and exercise.")
        return

    print(f"Filtered Data:\n{filter_df.head()}")

    filter_df = filter_df.copy()

    filter_df['Total Weight'] = filter_df['Weight'] * filter_df['Reps']
    plt.figure(figsize=(14, 7))
    sns.lineplot(x='Set Order', y='Weight', data=filter_df, markers='o')
    plt.title(f'Weight Progress for {exercise_name}')
    plt.xlabel('Set Order')
    plt.ylabel('Weight')
    plt.grid(True)
    plt.show()

    # Plot distribution of weights
    plt.figure(figsize=(14, 7))
    sns.boxplot(x='Set Order', y='Weight', data=filter_df)
    plt.title(f'Distribution of Weights by Set Order for {exercise_name}')
    plt.xlabel('Set Order')
    plt.ylabel('Weight')
    plt.grid(True)
    plt.show()

    # Plot total weight lifted per set
    plt.figure(figsize=(14, 7))
    sns.barplot(x='Set Order', y='Total Weight', data=filter_df, estimator=sum)
    plt.title(f'Total Weight Lifted per Set for {exercise_name}')
    plt.xlabel('Set Order')
    plt.ylabel('Total Weight')
    plt.grid(True)
    plt.show()

# Function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Workout Progress Visualizer")
    root.geometry('400x200')
    root.resizable(False,False)


    title_label = tk.Label(root, text="Workout Progress Visualizer", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10, fill=tk.X, expand=True)

    workout_label = tk.Label(frame, text="Workout Name:", font=("Helvetica", 12))
    workout_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    workout_names = df['Workout Name'].unique().tolist() 
    workout_var = tk.StringVar()
    workout_dropdown = ttk.Combobox(frame, textvariable=workout_var, values=workout_names, state='readonly')
    workout_dropdown.grid(row=0, column=1, padx=10, pady=5)

    exercise_label = tk.Label(frame, text="Exercise Name:", font=("Helvetica", 12))
    exercise_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    exercise_var = tk.StringVar()
    exercise_dropdown = ttk.Combobox(frame, textvariable=exercise_var, state='disabled')  
    exercise_dropdown.grid(row=1, column=1, padx=10, pady=5)


    def update_exercises(event):
        selected_workout = workout_var.get()
        if isinstance(selected_workout, list):  
            selected_workout = selected_workout[0]
        print(f"Selected Workout: {selected_workout}")  
        exercises = df[df['Workout Name'] == selected_workout]['Exercise Name'].unique().tolist()
        print(f"Available Exercises: {exercises}")  
        exercise_dropdown['values'] = exercises
        exercise_dropdown['state'] = 'normal' 
    
    workout_dropdown.bind("<<ComboboxSelected>>", update_exercises)

    plot_button = tk.Button(frame, text="Plot Progress", font=("Helvetica", 12), command=lambda: plot_progress(workout_var.get(), exercise_var.get()))
    plot_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

create_gui()
