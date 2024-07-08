import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk


df = pd.read_csv('weightlifting_721_workouts_modified.csv')

def plot_progress(workout_name,exercise_name):
    filter_df = df[(df['Workout Name']== workout_name)& (df['Exercise Name']==exercise_name)]
    if filter_df.empty:
        print("No Data available for the selected workout and exercise.")
        return

    plt.figure(figsize=(14,7))
    sns.lineplot(x='Set Order', y='Weight', data = filter_df , markers='o')
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




def create_gui():
    root = tk.Tk()
    root.title("Workout Progress Visualizer")


    workout_label = tk.Label(root,text = "Workout Name:")
    workout_label.grid(row=0, column=0, padx=10, pady=10)
    workout_names = df['Workout Name'].unique()
    workout_var = tk.StringVar()
    workout_dropdown = ttk.Combobox(root,textvariable=workout_var,values=workout_names)
    workout_dropdown.grid(row=0, column=1, padx=10, pady=10)

    exercise_label = tk.Label(root, text="Exercise Name:")
    exercise_label.grid(row=1, column=0, padx=10, pady=10)
    exercise_var = tk.StringVar()
    exercise_dropdown = ttk.Combobox(root, textvariable=exercise_var)
    exercise_dropdown.grid(row=1, column=1, padx=10, pady=10)

    def update_exercises(event):
        selected_workout = workout_var.get()
        exercises = df[df['Workout Name'] == selected_workout]['Exercise Name'].unique()
        exercise_dropdown['values'] = exercises
    
    workout_dropdown.bind("<<ComboboxSelected>>", update_exercises)
    plot_button = tk.Button(root, text="Plot Progress", command=lambda: plot_progress(workout_var.get(), exercise_var.get()))
    plot_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

create_gui()