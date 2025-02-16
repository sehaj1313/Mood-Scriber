import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("input.xlsx")
mood_by_day = data.groupby('Mood').size()
general_mood = mood_by_day.idxmax()
plt.figure(figsize=(8, 6))
mood_by_day.plot(kind='bar', color='lightgreen')
plt.title('General Mood of the Person Over the Week')
plt.xlabel('Mood')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.text(mood_by_day.index.tolist().index(general_mood), 
         mood_by_day[general_mood] + 1, 
         f"General Mood: {general_mood}", 
         ha='center')
plt.tight_layout()
plt.show()

activity_counts = pd.concat([data['Activity-1'], data['Activity-2']]).value_counts()
plt.figure(figsize=(10, 6))
activity_counts.plot(kind='bar', color='turquoise', width=0.8)
plt.title('Activity Frequency')
plt.xlabel('Activity')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

mood_by_day = data.groupby('Day')['Mood'].value_counts().unstack().fillna(0)
plt.figure(figsize=(10, 6))
mood_by_day.plot(kind='bar', stacked=True)
plt.title('Mood by Day')
plt.xlabel('Day')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.legend(title='Mood')
plt.tight_layout()
plt.show()

activity_mood_by_day = data.pivot_table(index='Activity-1', columns='Mood', 
                                        aggfunc='size', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(activity_mood_by_day, cmap='viridis', annot=True, fmt='d')
plt.title('Activity-Mood Relationship by Day')
plt.xlabel('Mood')
plt.ylabel('Activity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

mood_by_day = data.groupby(['Day', 'Mood']).size().unstack(fill_value=0)
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))
plt.subplots_adjust(hspace=0.5, wspace=0.3)
emotions = mood_by_day.columns
for i, emotion in enumerate(emotions):
    ax = axes[i // 3, i % 3]
    ax.bar(mood_by_day.index, mood_by_day[emotion], color='lightgreen', edgecolor='black', linewidth=1.2)
    ax.set_title(f'{emotion}', fontsize=10)  
    ax.set_xlabel('Day', fontsize=8)  
    ax.set_ylabel('Frequency', fontsize=8) 
    ax.tick_params(axis='x', rotation=45, labelsize=8)  
    ax.tick_params(axis='y', labelsize=8) 
    ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
