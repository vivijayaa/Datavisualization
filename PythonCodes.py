import pandas as pd

df = pd.read_excel(r'C:/Users/user/Documents/GitHub/Datavisualization/Dataset/FDA_Assignment.xlsx')
#print (df)
#-------------------------------------------------------------------------------------------------------------------------------
#1.	How well were the course materials organized and presented? 

import matplotlib.pyplot as plt
# Extract the integer ratings from the column and store them in a new column
df['Rating'] = df['How well did the teachers prepare for the classes?'].str.extract('(\d+)').astype(int)

# Plot a bar chart of the extracted ratings
plt.bar(df.index, df['Rating'])

# Customize the plot as needed
plt.xlabel('Sample Index')
plt.ylabel('Rating')
plt.title('Teacher Preparation Ratings')
plt.xticks(df.index)  # Use sample indices as x-axis ticks

# Show the plot
plt.show()
print(df.columns)
#---------------------------------------------------------------------------------------------------------------------------------------------------
#2.	How well did the course align with your career goals and interests? 
ratings_count=df["The institute takes active interest in promoting internship, student exchange, and field visit opportunities for students.*"].value_counts().sort_index()
fig,ax=plt.subplots()
ax.bar(ratings_count.index,ratings_count.values)
ax.set_xlabel("Rating")
ax.set_ylabel("Number of respomses")
ax.set_title("Course alignment with career goals and interest rating")
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#3.How satisfied were you with the level of interaction and engagement with your classmates and instructors?# Count the number of responses for each rating value (0-4)
ratings_count = df["How well were the teachers able to communicate?"].value_counts().sort_index()

# Plot the bar chart
fig, ax = plt.subplots()
ax.bar(ratings_count.index, ratings_count.values)
ax.set_xlabel("Rating")
ax.set_ylabel("Number of responses")
ax.set_title("Satisfaction with interaction and engagement with classmates and instructors rating")
plt.show()

# ------------------------------------------------------------------------------------------------------------------
# 4.How effective were the assignments and assessments in helping you learn and apply the course material? 
ratings_count = df["Teachers encourage you to participate in extracurricular activities"].value_counts().sort_index()

# Plot the bar chart
fig, ax = plt.subplots()
ax.bar(ratings_count.index, ratings_count.values)
ax.set_xlabel("Rating")
ax.set_ylabel("Number of responses")
ax.set_title("Effectiveness of assignments and assessments in learning and applying course material rating")
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------
# 5.To what extent were you able to develop your critical thinking and problem-solving skills in this course? 
target_question = "To what extent were you able to develop your critical thinking and problem-solving skills in this course?"
male_responses = df.loc[df["Gender"] == "Male", target_question]
female_responses = df.loc[df["Gender"] == "Female", target_question]

# Count the number of responses for each rating value (0-4)
male_ratings_count = male_responses.value_counts().sort_index()
female_ratings_count = female_responses.value_counts().sort_index()

# Plot the bar chart
fig, ax = plt.subplots()
ax.bar(male_ratings_count.index - 0.2, male_ratings_count.values, width=0.4, label="Male")
ax.bar(female_ratings_count.index + 0.2, female_ratings_count.values, width=0.4, label="Female")
ax.set_xlabel("Rating")
ax.set_ylabel("Number of responses")
ax.set_title("Development of critical thinking and problem-solving skills by gender")
ax.set_xticks(range(5))
ax.set_xticklabels(["0", "1", "2", "3", "4"])
ax.legend()
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------
# 6.	Were the instructors able to effectively incorporate technology and multimedia into their teaching? 

df_q6 = df[['     Programme/Degree', 'What percentage of teachers use ICT tools such as LCD projector, Multimedia, etc. while teaching ?']]

# Group the data by programme and count the number of responses for each value
df_q6_grouped = df_q6.groupby(['     Programme/Degree', 'What percentage of teachers use ICT tools such as LCD projector, Multimedia, etc. while teaching ?']).size().unstack(fill_value=0)

# Create the bar plot
ax = df_q6_grouped.plot(kind='bar', figsize=(10,6))

# Set the axis labels and title
ax.set_xlabel('Programme/Degree')
ax.set_ylabel('Number of Responses')
ax.set_title('Effectiveness of Incorporating Technology and Multimedia by Programme/Degree')

# Show the plot
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------

# 7.	How well did the instructors provide feedback on your assignments and performance in the  course? 

# Filter the data for the specific question
df_q1 = df[['Teachers inform you about your expected competencies, course outcomes and programme outcomes']]

# Count the number of responses for each value
df_q1_counts = df_q1.value_counts(sort=False)

# Create the bar plot
ax = df_q1_counts.plot(kind='bar', color='yellow', figsize=(8,6))

# Set the axis labels and title
ax.set_xlabel('Rating')
ax.set_ylabel('Number of Responses')
ax.set_title('Effectiveness of Instructor Feedback on Assignments and Performance')

# Show the plot
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------
# 8.	Did the course provide opportunities for practical and hands-on learning experiences? 

df_q9 = df[['    The teachers illustrate the concepts through examples and applications.']]

# Count the number of responses for each value
df_q9_counts = df_q9.value_counts(sort=False)

# Create the bar plot
ax = df_q9_counts.plot(kind='bar', figsize=(8,6))

# Set the axis labels and title
ax.set_xlabel('Response')
ax.set_ylabel('Number of Responses')
ax.set_title('Opportunities for Practical and Hands-On Learning Experiences')

# Show the plot
plt.show()



# ---------------------------------------------------------------------------------------------------------------------------------

# 10.How well did the instructors adjust their teaching approach to accommodate different learning styles and abilities? 

q7 = df[["     Programme/Degree", "Class", "How well did the teachers prepare for the classes?"]]

# Group the data by Programme/Degree and Class
grouped = q7.groupby(["     Programme/Degree", "Class"])

# Calculate the mean for each group
means = grouped.mean()

# Reset the index to make "Programme/Degree" and "Class" columns again
means = means.reset_index()

# Pivot the table to make "Class" values into columns
pivoted = means.pivot(index="     Programme/Degree", columns="Class", values="prepare")

# Create a bar plot
colors = ["#ffcc00", "#ffa500", "#ff8c00", "#ff4500"]
ax = pivoted.plot(kind="bar", color=colors)

# Add labels and title
ax.set_xlabel("Programme/Degree")
ax.set_ylabel("Mean rating for 'prepare'")
ax.set_title("Effectiveness of instructors in preparing students for the course")
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------

#10.	How well did the course prepare you for the final exam or assessment? 

# filter for the relevant columns
df_prep = df[['     Programme/Degree', 'How well did the teachers prepare for the classes?']]

# group by program and calculate value counts
grouped_prep = df_prep.groupby('     Programme/Degree')['How well did the teachers prepare for the classes?'].value_counts().unstack()

# plot the bar plot
ax = grouped_prep.plot(kind='bar', figsize=(10, 6), width=0.8)

# add labels and title
plt.title('How well did the course prepare you for the final exam or assessment?')
plt.xlabel('Programme/Degree')
plt.ylabel('Count')
plt.xticks(rotation=0)

# show the plot
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------

# 11.	How much did you enjoy learning the course material? 

# filter for the relevant columns
df_enjoyment = df[['The institute takes active interest in promoting internship, student exchange, and field visit opportunities for students.*']]

# group by rating and calculate value counts
df_enjoyment_counts = df_enjoyment.groupby('The institute takes active interest in promoting internship, student exchange, and field visit opportunities for students.*').size().reset_index(name='counts')

# create the horizontal bar plot
plt.barh(df_enjoyment_counts['The institute takes active interest in promoting internship, student exchange, and field visit opportunities for students.*'], df_enjoyment_counts['counts'], color='green')
plt.title('How much did you enjoy learning the course material?')
plt.xlabel('Number of Responses')
plt.ylabel('Rating (0-4)')
plt.xlim(0, df_enjoyment_counts['counts'].max() * 1.1)
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------
# 12.	To what extent did the course challenge you intellectually? 


df_teaching = df[['     Programme/Degree', 'How well did the teachers prepare for the classes?']]

# group by program and calculate value counts
df_teaching_counts = df_teaching.groupby(['     Programme/Degree', 'How well did the teachers prepare for the classes?']).size().reset_index(name='count')

# pivot the data to have programs as columns
df_teaching_pivot = df_teaching_counts.pivot(index='How well did the teachers prepare for the classes?', columns='     Programme/Degree', values='count')

# plot the bar chart
ax = df_teaching_pivot.plot(kind='bar', color=['#ffcc00', '#f47f20'], figsize=(8,6))
ax.set_title('Instructors adjusting teaching approach to different learning styles and abilities')
ax.set_xlabel('Teaching approach')
ax.set_ylabel('Count')
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------
# 13.	How well did the instructors provide guidance and support for selfdirected learning? 

import seaborn as sns

df_sdl = df[['     Programme/Degree', 'Your mentor does a necessary follow-up with an assigned task to you']]

# group by program and calculate value counts
df_sdl_counts = df_sdl.groupby(['     Programme/Degree', 'Your mentor does a necessary follow-up with an assigned task to you']).size().reset_index(name='count')

# create a pivot table for easier plotting
df_sdl_pivot = df_sdl_counts.pivot(index='     Programme/Degree', columns='Your mentor does a necessary follow-up with an assigned task to you', values='count')

# create a bar plot using Seaborn
sns.set_style("whitegrid")
sns.set_palette("deep")
ax = df_sdl_pivot.plot(kind='bar', stacked=True)

# set the plot title and labels
ax.set_title("How well did the instructors provide guidance and support for self-directed learning?", fontsize=14)
ax.set_xlabel("Programme/Degree", fontsize=12)
ax.set_ylabel("Count", fontsize=12)

# display the plot
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------
# 14.	How well did the instructors foster an inclusive and respectful learning environment? 

# filter for the relevant columns
df_incl_respect = df[['     Programme/Degree', 'The overall quality of teaching-learning process in your institute is very good']]

# group by program and calculate value counts
df_incl_respect_counts = df_incl_respect.groupby(['     Programme/Degree', 'The overall quality of teaching-learning process in your institute is very good']).size().reset_index(name='count')

# create a pivot table for easy plotting
df_incl_respect_pivot = df_incl_respect_counts.pivot(index='     Programme/Degree', columns='The overall quality of teaching-learning process in your institute is very good', values='count')

# create a bar plot using Seaborn
sns.set_style("whitegrid")
sns.set_palette("deep")
ax = df_incl_respect_pivot.plot(kind='bar', stacked=True, figsize=(8,6))

# set the plot title and labels
ax.set_title("How well did the instructors foster an inclusive and respectful learning environment?", fontsize=14)
ax.set_xlabel("Program/Degree", fontsize=12)
ax.set_ylabel("Count", fontsize=12)

# display the plot
plt.show()

# ---------------------------------------------------------------------------------------------------------------------------------
















