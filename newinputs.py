import pandas as pd
import random

# Read the original data from input.xlsx
original_data = pd.read_excel("input.xlsx")

# Define the mood list
mood_list = ['Neutral', 'Happy', 'Sad', 'Rad', 'Angry', 'Lonely', 'Depressed']

# Additional generated data
additional_data = pd.DataFrame({
    'Day': [random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']) for _ in range(100)],
    'Mood': [random.choice(mood_list) for _ in range(100)],
})

# Define meaningful activities for each mood
activities_by_mood = {
    'Neutral': ['Work', 'Exercise', 'Socializing', 'Hobby', 'Rest', 'Reflect'],
    'Happy': ['Celebration',  'Outdoor activities', 'Creative hobbies', 'Volunteering'],
    'Sad': ['Reflecting on loss', 'Watching sad movies', 'Experiencing rejection','Illness'],
    'Rad': ['Adventure sports', 'Exploring new places', 'Attending events', 'Trying new activities'],
    'Angry': ['Office Politics', 'Team Conflict', 'Unfinished tasks', 'Argument'],
    'Lonely': ['Routine', 'Daily Monotony', 'No work'],
    'Depressed': ['Past Failures', 'Negative Thoughts',' Ongoing Challenges',' Traumatic Events']
}

additional_data['Activity-1'] = additional_data['Mood'].apply(lambda mood: random.choice(activities_by_mood[mood]))
additional_data['Activity-2'] = additional_data.apply(lambda row: random.choice([act for act in activities_by_mood[row['Mood']] if act != row['Activity-1']]), axis=1)

# Concatenate the original data with the additional data
combined_data = pd.concat([original_data, additional_data], ignore_index=True)

# Save the combined data to a new Excel file
combined_data.to_excel("combined_input.xlsx", index=False)
