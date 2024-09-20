import pandas as pd
pf = pd.read_csv('Client_data.csv')

print(pf.columns)

#Show all rows
#pd.set_option('display.max_columns',None)
#print(pf)

#values null
print (pf.isnull().sum())

#fill null values
#null_genders= pf[pf['Gender'].isnull()]
#print(missing_gender[['Name','Age']])

pf.loc[pf['Name']== 'Elizabeth Weaver','Gender']='Female'
pf.loc[pf['Name']== 'Kimberly Thomas', 'Gender']='Female'
pf.loc[pf['Name']== 'Alison Hernandez','Gender']='Female'
pf.loc[pf['Name']== 'Jeffrey Newman', 'Gender']='Male'
pf.loc[pf['Name']== 'Kristen Chambers','Gender']='Female' 
pf.loc[pf['Name']== 'Danielle Long','Gender']='Male'
pf.loc[pf['Name']== 'Laura Mccann','Gender']='Female'
pf.loc[pf['Name']== 'Kevin Collins','Gender']='Male'
pf.loc[pf['Name']== 'David Davis','Gender']='Male'
pf.loc[pf['Name']== 'Manuel Flores','Gender']='Male'
pf.loc[pf['Name']== 'Anthony Garcia','Gender']='Male'
pf.loc[pf['Name']== 'David Singh','Gender']='Male'
pf.loc[pf['Name']== 'Janet Williams','Gender']='Female'
pf.loc[pf['Name']== 'Justin Smith','Gender']='Male'
pf.loc[pf['Name']== 'Lindsay Crosby','Gender']='Female'
pf.loc[pf['Name']== 'Gabriella Townsend','Gender']='Female'
pf.loc[pf['Name']== 'Sabrina Gutierrez','Gender']='Female'
pf.loc[pf['Name']== 'Dr. Kyle Mcgrath','Gender']='Male'
pf.loc[pf['Name']== 'Erica Gordon','Gender']='Female'
pf.loc[pf['Name']== 'Calvin Smith','Gender']='Male'
pf.loc[pf['Name']== 'Katie Robinson','Gender']='Female'
pf.loc[pf['Name']== 'Daniel Smith','Gender']='Male'
pf.loc[pf['Name']== 'Roger Booth','Gender']='Male'
pf.loc[pf['Name']== 'Lisa Marsh','Gender']='Female'
pf.loc[pf['Name']== 'Haley Salinas','Gender']='Male'
pf.loc[pf['Name']== 'Joseph Vaughn','Gender']='Male'
pf.loc[pf['Name']== 'Amy Martinez','Gender']='Female'
pf.loc[pf['Name']== 'Kenneth Houston','Gender']='Male'
pf.loc[pf['Name']== 'Hector Beard','Gender']='Male'
pf.loc[pf['Name']== 'Heidi Keith','Gender']='Female'
pf.loc[pf['Name']== 'Amy Myers','Gender']='Female'
pf.loc[pf['Name']== 'Jerry David','Gender']='Male'
pf.loc[pf['Name']== 'Melanie Knight','Gender']='Female'
pf.loc[pf['Name']== 'Amanda Vargas','Gender']='Female'
pf.loc[pf['Name']== 'Michael Hopkins','Gender']='Male'
pf.loc[pf['Name']== 'Jeanette Graves','Gender']='Female'
pf.loc[pf['Name']== 'Tim Mccarty','Gender']='Male'
pf.loc[pf['Name']== 'Austin Bean','Gender']='Male'
pf.loc[pf['Name']== 'Christopher Brown','Gender']='Male'
pf.loc[pf['Name']== 'Jessica Wagner','Gender']='Female'
pf.loc[pf['Name']== 'Kelly Gomez','Gender']='Female'
pf.loc[pf['Name']== 'Lori Joseph','Gender']='Female'
pf.loc[pf['Name']== 'Donald Thomas','Gender']='Male'
pf.loc[pf['Name']== 'Edward Williams','Gender']='Male'
pf.loc[pf['Name']== 'Clinton Hall','Gender']='Male'
pf.loc[pf['Name']== 'Latoya Evans','Gender']='Female'
pf.loc[pf['Name']== 'Monica Stone','Gender']='Female'
pf.loc[pf['Name']== 'Jennifer Moore','Gender']='Female'
pf.loc[pf['Name']== 'Veronica Ford','Gender']='Female'
pf.loc[pf['Name']== 'Mr. David Cunningham','Gender']='Male'
pf.loc[pf['Name']== 'Kristina Choi','Gender']='Female'
pf.loc[pf['Name']== 'James Weiss','Gender']='Male'
pf.loc[pf['Name']== 'Nicholas Dunlap','Gender']='Male'
pf.loc[pf['Name']== 'Monica Harmon','Gender']='Female'
pf.loc[pf['Name']== 'Cindy Vargas','Gender']='Female'
pf.loc[pf['Name']== 'Jessica Blackwell','Gender']='Female'
pf.loc[pf['Name']== 'Michelle Benson','Gender']='Male'
pf.loc[pf['Name']== 'Patrick Ritter','Gender']='Male'

#Verify
corrected_gender = pf[pf['Name'].isin([
    'Elizabeth Weaver','Kimberly Thomas','Alison Hernandez','Jeffrey Newman', 
    'Kristen Chambers','Danielle Long','Laura Mccann','Kevin Collins',
    'David Davis','Manuel Flores','Anthony Garcia','David Singh','Janet Williams',
    'Lindsay Crosby','Gabriella Townsend','Sabrina Gutierrez','Dr. Kyle Mcgrath',
    'Erica Gordon','Calvin Smith','Katie Robinson','Daniel Smith','Roger Booth',
    'Lisa Marsh','Haley Salinas','Joseph Vaughn','Amy Martinez','Kenneth Houston',
    'Hector Beard','Heidi Keith','Amy Myers','Jerry David','Melanie Knight',
    'Amanda Vargas','Michael Hopkins','Jeanette Graves','Tim Mccarty',
    'Austin Bean','Christopher Brown','Jessica Wagner','Kelly Gomez','Lori Joseph',
    'Donald Thomas','Edward Williams','Clinton Hall','Latoya Evans','Monica Stone',
    'Jennifer Moore','Veronica Ford','Mr. David Cunningham','Kristina Choi','James Weiss',
    'Nicholas Dunlap','Monica Harmon','Cindy Vargas','Jessica Blackwell','Michelle Benson',
    'Patrick Ritter'
])]
print(corrected_gender[['Name','Gender']])

#Verify remaining null values 
remaining_nulls = pf['Gender'].isnull().sum()
print(f"Remaining null values in 'Gender: {remaining_nulls}")

#show null values
null_genders= pf[pf['Gender'].isnull()]
print("Show remaining null values in Gender: ")
print(null_genders[['Name','Age','Gender']])


#values duplicate
print('duplicate',pf.duplicated().sum())

#Show all columns
pd.set_option('display.max_columns',None)
pd.reset_option('display.max_columns')
print(pf)

#data types
print(pf.dtypes)
#Correct Data Types
pf['Client ID'] = pf['Client ID'].astype(str)
pf['Name'] = pf['Name'].astype(str)
pf['Age'] = pf['Age'].astype(int)
pf['Gender'] = pf['Gender'].astype(str)
pf['City'] = pf['City'].astype(str)
pf['Registration Date'] = pd.to_datetime(pf['Registration Date'])
pf['Sport Preferences'] = pf['Sport Preferences'].astype(str)

print(pf.dtypes)

#Duplicate Data
duplicate = pf[pf.duplicated()]
print('Duplicate Data: ', duplicate)

#Negative age
negative = pf[pf['Age'] < 0 ]
print(negative)

#Convert negative values to positive
pf['Age'] = pf ['Age'].apply(lambda x: abs(x))
print("Positive values",pf[pf['Age']<0])

#show all values
pd.set_option('display.max_rows', 200)
print(pf)

#ANALYSIS
#Split Sport Preferences column

pf['Sport Preferences'] = pf['Sport Preferences'].str.split(', ')
pf_exploded = pf.explode('Sport Preferences')

print(pf_exploded.head(20))


#ANALYSIS / MOST PRACTICED SPORT

   #Frequency of practicing sport
sport_counts = pf_exploded['Sport Preferences'].value_counts()
print("Most practiced sport: ",sport_counts)

    #SHOW THE MOST PRACTICED SPORT 
most_practiced_sport = sport_counts.idxmax()
most_practiced_count = sport_counts.max()
#print(f"\nThe most practiced sport is: {most_practiced_sport} is practiced by {most_practiced_count} people")

    #BAR CHART
import seaborn as sns
import matplotlib.pyplot as plt

sport_counts = pf_exploded['Sport Preferences'].value_counts()

plt.figure(figsize=(12,8))
sns.barplot(x=sport_counts.index, y=sport_counts.values, palette='viridis')

plt.title('Most Practiced Sports')
plt.xlabel('Sport')
plt.ylabel('Number of person')
plt.xticks(rotation=45, ha='right')
#plt.show()

    #LINE CHART 
    #This chart allows us to visualize trends over several years.
pf_exploded['Year']= pd.DatetimeIndex(pf_exploded['Registration Date']).year
years = pf_exploded['Year'].value_counts().sort_index()
print("Years AQUI: ",years)


sport_trends = pf_exploded.groupby(['Year', 'Sport Preferences']).size().reset_index(name='Count')

plt.figure(figsize=(12,8))
sns.lineplot(data=sport_trends, x='Year', y='Count', hue='Sport Preferences', marker='o')


plt.title('Trends sports')
plt.xlabel('Years')
plt.ylabel('Number of persons')
plt.xticks(rotation=45, ha='right')
plt.ylim(0,30)
plt.legend(title='Sport', bbox_to_anchor=(1.05,1))
#plt.show()
  
    #Box Plot Chart
    #This chart allows us to visualize the ages of clients practicing each sport.
sports = pf_exploded['Sport Preferences'].unique()

plt.figure(figsize=(12,6))
sns.boxplot(x='Sport Preferences', y='Age',data=pf_exploded[pf_exploded['Sport Preferences'].isin(sports)])
plt.title('Ages distribution by sport')
plt.xlabel('Sport')
plt.ylabel('Ages')
plt.xticks(rotation=45)
#plt.show()

     #Box Plot Chart between Age, Gender and Sport
     #This chart helps to visualize how the age of each client varies between different genders and sports.

sns.set(style="whitegrid")

g=sns.catplot(
    data=pf_exploded, kind="box", #Dataset to be used and type of chart "Box plot"
    x="Gender", y="Age", col="Sport Preferences", #
    col_wrap=3, #Number of columns in the grid 
    height=4, aspect=0.7, #Size of each graph
    palette="Set3" #Colors of charts
)
g.set_axis_labels("Gender","Age")
g.set_titles("{col_name}")
plt.subplots_adjust(top=0.9)
g.figure.suptitle("Age Distribution by Gender and Sport")
plt.show()



