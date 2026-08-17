import pandas as pd
import numpy as np

#=========================================================================================================
# Sample data
drinks = pd.read_csv(r'http://bit.ly/drinksbycountry')
movies =  pd.read_csv(r'http://bit.ly/imdbratings')
stocks =  pd.read_csv(r'http://bit.ly/smallstocks')
titanic = pd.read_csv(r'http://bit.ly/kaggletrain')
ufo = pd.read_csv(r'http://bit.ly/uforeports')
orders = pd.read_table(r'http://bit.ly/chiporders')
#=========================================================================================================
# Create a Series
data = [1, 7, 2]
series = pd.Series(data)

print(series)
print(series[0])

series2 = pd.Series(data, index=['x', 'y', 'z'])
print(series2['y'])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)
#=========================================================================================================
# Create a Data Frame
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data)
print(df) 

# Named index with specifc order of columns
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"], columns=['duration', 'calories'])
print(df) 
print(df.loc['day1']) 

# Create a Data Frame using list of lists
pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'red']], columns=['id', 'color'])

# Create a Data Frame using numpy method
arr = np.random.randint(1, 50, size= (4, 2))
pd.DataFrame(arr, columns= ['one', 'two'])

# Example of Creating random Data Frame
pd.DataFrame({'student': np.arange(100, 110), 'test scores': np.random.randint(30, 100, size= 10)}).set_index('student')

# concat Data Frame and Series
df = pd.DataFrame({'id':[100, 101, 102], 'color':['red', 'blue', 'red']}, columns=['color', 'id'], index=['a', 'b', 'c'])
s = pd.Series(['round', 'square'], index=['c', 'b'], name= 'shape')
pd.concat([df, s], axis= 1)
#=========================================================================================================
# Read a Data by read_table()
pd.read_table(r"https://bit.ly/chiporders")
# parameters: (path, sep, header, names, index_col, usecols, dtype, skiprows, nrows, na_values, encoding, parse_dates, skipfooter, engine)

# Manipulate with data by read_table()
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table(r'http://bit.ly/movieusers', sep= '|', header = None, names= user_cols, usecols=['user_id', 'occupation'], nrows=10)
users.head()
#=========================================================================================================
# Select a Series from Data Frame
ufo['City']

# Create a Series (with concatenation)
ufo['location'] = ufo['City'] + ', ' + ufo['State']
ufo.head()
#=========================================================================================================
# Some methods and attributes
movies.head() # --> shows the first 5 rows
movies.tail() # --> shows the last 5 rows

movies.describe()              # --> shows numerical description of Data Frame
movies.describe(include='all') # --> show the whole description of Data Frame
movies.info()

movies.shape   # --> shows the number of rows and columns
movies.dtypes  # --> show the type of every series in Data Frame
movies.columns # --> shows the names of columns
movies.index   # shows the (start, stop, step) of the indices
#=========================================================================================================
# Rename columns in Data Frame

# method 1:
ufo.rename(columns = {'Colors Reported': 'Colors', 'Shape Reported': 'Shape'}, inplace= True)
ufo.columns

# method 2:
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
ufo.columns

# rename columns while reading a Data Frame
ufo = pd.read_csv(r"http://bit.ly/uforeports", names = ufo_cols, header = 0) 
ufo.head() # header equals 0 means that column names has already existed in Data Frame

# rename columns using str methodes
ufo.columns = ufo.columns.str.replace(" ", "_")
ufo.columns

# add prefix and suffix in The dataFrame
df = pd.DataFrame({'col one': [100, 200], 'col two': [300, 400]})
df.add_prefix('X_')
df.add_suffix('_Y')
#=========================================================================================================
# Remove columns from a Data Frame

# remove single column
ufo.drop('Colors Reported', axis= 1,  inplace= True)
ufo.head()

# remove multiple column
ufo.drop(['City', 'State'], axis= 1, inplace= True)
ufo.head()

# remove rows
ufo.drop([0, 1], axis= 0,  inplace= True)
ufo.head()
#=========================================================================================================
# Sort a Data Frame or Series

# sort a Series
movies['title'].sort_values() # ascending order
movies['title'].sort_values(ascending= False) # decending order

# sort a Data Frame by a Series
movies.sort_values('title')

# sort a Data Frame by multiple Series
movies.sort_values(['content_rating', 'duration'])
#=========================================================================================================
# Filter rows of a Data Frame by column value

# create a series of boolens in "duration" column
filtered = movies['duration'] >= 200
filtered.head()

# create a filtered Data Frame
movies[movies['genre'] == 'Crime']

# select a specific column of filtered Data Frame
movies[movies['genre'] == 'Crime']['genre']
movies.loc[movies['genre'] == 'Crime', 'genre'] # more effecient
#=========================================================================================================
# Apply multiple filter criteria to a Data Frame

movies[(movies['duration'] >= 200) & (movies['genre'] == 'Drama')] # &: and
movies[(movies['duration'] >= 200) | (movies['genre'] == 'Drama')] # |: or
movies[(movies['duration'] >= 200) & ~(movies['genre'] == 'Drama')] # &, ~: and with not

movies[movies['genre'].isin(['Crime', 'Drama', 'Action'])] # filter with more category
#=========================================================================================================
# Iterate a Data Frame using iterrows
for index, row in ufo.iterrows():
    print(index, row['City'], row['State'])

# Iterate a Data Frame using itertuples
for row in ufo.itertuples(): 
    print(row.City) # faster than iterrows
#=========================================================================================================
# Using "axis" parameter in pandas

drinks.mean(numeric_only= True, axis = 0) # calculate mean for every column
drinks.mean(numeric_only= True, axis = 1) # calculate mean for every row

# ** You can use another functions like std or sum **
#=========================================================================================================
# Using string methods

# method 1
orders['item_name'].str.contains('Chicken')
orders[orders['item_name'].str.contains('Chicken')] # --> filter the data

# method 2
orders['item_name'].str.upper()

# method 3
orders['choice_description'].str.replace('[', '').str.replace(']', '')

# ** You can see the another methods in pandas API reference ** 
#=========================================================================================================
# changing data type of a Series
orders = pd.read_table(r'http://bit.ly/chiporders')

orders['item_price'].str.replace('$', '').astype(float) # remove "$" and convert into float type
orders['item_name'].str.contains('Chicken').astype(int) # contains and convert into int type

# change data type before reading
drinks = pd.read_csv(r'http://bit.ly/drinksbycountry', dtype= {'beer_servings': float})
drinks.dtypes

# convert data types at once
drinks = drinks.astype({'beer_servings':float, 'spirit_servings':float})
drinks.dtypes
#=========================================================================================================
# Analyze data by categorial Using "groupby"

# get the mean or any aggregation function of every categorial('continent') in 'beer_servings' column
drinks.groupby('continent')['beer_servings'].mean()
drinks.groupby('continent')['beer_servings'].agg(['count', 'min', 'max', 'mean'])

# get the mean of every numeric column for every categorial('continent')
drinks.groupby('continent').mean(numeric_only= True)

# Get a group from groupby
drinks.groupby('continent').get_group('Africa')

# describe with groupby
drinks.groupby('continent')['wine_servings'].describe()

# filter using groupby
gb = drinks.groupby('continent').filter(lambda x: x.name != 'Africa')
gb['wine_servings'].value_counts()
#=========================================================================================================
# Exploring a Series

movies['genre'].value_counts() # count every single category
movies['genre'].value_counts(normalize= True) * 100 # count every single category by proportion with broadcasting

movies['genre'].unique() # returns unique categories
movies['genre'].nunique() # returns number of unique values

# crosstab (index, columns, values, margins, aggfunc, normalize)
pd.crosstab(movies['genre'], movies['content_rating']) # clarify the relation of two columns
#=========================================================================================================
# Handling missing values

ufo.isnull().tail() # check if the Data Frame values is null or not
ufo.notnull().tail()

ufo.isnull().sum() # number of missing values of each column

ufo.dropna(how= 'any').shape
ufo.dropna(how= 'all').shape
ufo.dropna(subset= ['City', 'Shape Reported'], how= 'any').shape

ufo['Shape Reported'].value_counts(dropna = False) # value count and count missing values
ufo['Shape Reported'].fillna(value = "Unknown", inplace= True) # fill missing values
#=========================================================================================================
# Using index in a Data Frame and a Series

drinks.set_index('country', inplace= True)
drinks.head() # set country column as a row index
drinks = pd.read_csv(r'http://bit.ly/drinksbycountry', index_col = 'country') # set the index col while reading

drinks.index.name = None
drinks.head() # deal with index name

drinks.index.name = "Country"
drinks.reset_index("Country", inplace= True)
drinks.head() # reset country as a column and reset its name

# Series
drinks['continent'].value_counts().index # --> return an array of indices
drinks['continent'].value_counts().values # --> return an array of values

drinks['continent'].value_counts().sort_values() # --> sort the series by values
drinks['continent'].value_counts().sort_index() # --> sort the series by index

# make a Series
people = pd.Series([3000000, 85000], index= ['Albania', 'Andorra'], name= 'population', dtype= np.int32)
drinks['beer_servings'] * people  # Broadcasting

# Add this Series to the Data Frame using 'concat'
pd.concat([drinks, people], axis= 1)
#=========================================================================================================
# Using 'loc' and 'iloc'

# using 'loc' (the end inclusive)
ufo.loc[0]
ufo.loc[0:2]
ufo.loc[:, ['City', 'State']]
ufo.loc[0:2, 'City' : 'State']
ufo.loc[ufo['City'] == 'Oakland']['State'] # --> filter and it is more flexible and effecient

# using 'iloc' (the end exclusive)
ufo.iloc[:, 0:2]
ufo.iloc[0:3, :]
ufo.iloc[0:3, [0, 3]]
#=========================================================================================================
# Using 'category' type in a Data Frame
"""
category: special type in pandas used to store "Categorial Variables" e.g (male-female), (small-big).
It's very useful in memory effecincy because it stores a dictionary with unique value refers to a number with a column of numbers
Useful when you have object Categorial column and you want to improve the memory and perfomance

It's very useful in Ordered Categories e.g (small < medium < big)
"""

drinks.info(memory_usage= 'deep') # --> before converting 'continent' column to categorial type

drinks['continent'] = drinks['continent'].astype('category')
drinks.dtypes # --> convering 'continent' column to category type

drinks['continent'].cat.codes.head() # --> the refered numbers
drinks['continent'].cat.categories
drinks.memory_usage(deep= True) # memory improvement

# Ordered Categories
df = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']})

df['quality'] = pd.Categorical(df['quality'], categories= ['good', 'very good', 'excellent'], ordered= True)
df.sort_values('quality')
df.loc[df['quality'] > 'good'] # using boolen condition (filter)

# convert data type to category while reading
drinks = pd.read_csv(r'http://bit.ly/drinksbycountry', dtype={'continent':'category'})
drinks.dtypes
#=========================================================================================================
# Random samples from a Data Frame

ufo.sample(n=3, random_state= 42) # random state: seed
ufo.sample(frac= 0.75,  random_state=42) # frac: get 75% of rows
#=========================================================================================================
# Create dummy variables (Useful for Machine Learning)

# method 1
titanic['Sex_male'] = titanic['Sex'].map({'female': 0, 'male': 1})

# method 2
embarked_dummies = pd.get_dummies(titanic['Embarked'], prefix='Embarked', prefix_sep='-').iloc[:, 1:]
pd.concat([titanic, embarked_dummies], axis= 1)

# method 3 (flexible)
pd.get_dummies(titanic, columns=['Sex', 'Embarked'], drop_first= True) 
#=========================================================================================================
# Working with dates and times 

# to_datetime(dataframe of series, format)
ufo['Time'] = pd.to_datetime(ufo['Time']) # convert 'Time' column to datatime type
ufo.dtypes

ufo['Time'].dt.hour # get hours
ufo['Time'].dt.day_name() # get days name
ufo['Time'].dt.day_of_year # get day of the year
ufo['Time'].dt.weekday # the number of day in a week
ufo['Time'].dt.is_leap_year # check if it is a leap year

# convert to period (Y, M, Q, D)
ufo['month'] = ufo['Time'].dt.to_period('M')

# convet datetime to timestamp
ufo['month'] = ufo['month'].dt.to_timestamp(how='start')

# Dealing with time format
ufo['Time'] = ufo['Time'].dt.strftime('%d/%m/%Y')

# filter using dates and times
ts = pd.to_datetime('1/1/1999')
ufo.loc[ufo['Time'] >= ts, :].head()

(ufo['Time'].max() - ufo['Time'].min()).days

# create a datetime column from the entire DataFrame
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]], columns=['month', 'day', 'year', 'hour'])
pd.to_datetime(df)

# create a datetime column from a subset of columns
pd.to_datetime(df[['month', 'day', 'year']])

# overwrite the index
df.index = pd.to_datetime(df[['month', 'day', 'year']])
df

dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M', periods=6) # create a sereis with frequent by month
#=========================================================================================================
# Remove duplicate rows
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users  = pd.read_table(r'http://bit.ly/movieusers', sep='|', header= None, names= user_cols, index_col= 'user_id')

# number of duplicates in zip_code column
users['zip_code'].duplicated().sum()

# number of duplicates in the Data Frame
users.duplicated().sum()

users.loc[users.duplicated(keep = 'first'), :] # keep the first duplicates and get the anothers
users.loc[users.duplicated(keep = 'last'), :] # keep the last duplicates and the first
users.loc[users.duplicated(keep = False), :] # get the first and another duplicates

# delete duplicates (subset, keep, ignore_index, inplace)
users.drop_duplicates(keep= 'first').shape

# number of duplicates in the Data Frame in terms of age and zip_code columns
users.duplicated(subset= ['age', 'zip_code']).sum()

# drop duplicates in terms of age and zip_code columns
users.drop_duplicates(subset= ['age', 'zip_code']).shape
#=========================================================================================================
# Replace the values in Data Frame

# convert 'NOT RATED' value to Nan value
movies.loc[movies['content_rating'] == 'NOT RATED', 'content_rating'] = np.nan

# convert specific value
top_movies = movies.loc[movies['star_rating'] >=9, :]
top_movies.loc[0, 'duration'] = 150
top_movies.head()

# replace the values to Nan value in Data Frame
movies.replace(['UNRATED', 'NOT RATED'], np.nan)
#=========================================================================================================
# Display options in pandas

pd.get_option('display.max_rows') # --> 60

pd.set_option('display.max_rows', 100) # max_rows displayed: 100
pd.set_option('display.max_rows', None) # show all rows
pd.reset_option('display.max_rows') # return to default (60)
# ** There are the same options in columns **

train = pd.read_csv(r'http://bit.ly/kaggletrain')
pd.get_option('display.max_colwidth') # number of chars in each column: 50
pd.set_option('display.max_colwidth', 70) 

pd.get_option('display.precision') # --> round by number of decimals: 6
pd.set_option('display.precision', 2)

drinks['y'] = drinks['total_litres_of_pure_alcohol'] * 10000 # create a large column 
pd.set_option('display.float_format', '{:,}'.format) # format with float numbers only

pd.reset_option('all') # reset all options
#=========================================================================================================
# Apply a function to a Series or Data Frame (map, apply)
train = pd.read_csv(r'http://bit.ly/kaggletrain')
drinks = pd.read_csv(r'http://bit.ly/drinksbycountry')

# map: works on Series or do Data Frame to do simple function or generate a dictionary
train['Sex_num'] = train['Sex'].map({'female':0, 'male':1}) # dictionary
train.loc[0:4, ['Sex', 'Sex_num']]

train['Age plus 30'] = train['Age'].map(lambda x: x+30) # simple function
train.loc[0:4, ['Age', 'Age plus 30']]

drinks.loc[:, 'beer_servings':'wine_servings'].map(float) # Data Frame
#--------------------------------
# apply: works on Series and a DataFrame to do functions and it is more flexible than map
train['Name_length'] = train['Name'].apply(len)
train.loc[0:4, ['Name', 'Name_length']] # built in function

train['Fare_ceil'] = train['Fare'].apply(np.ceil).astype(np.int16)
train.loc[0:4, ['Fare', 'Fare_ceil']] # numpy function

def get_element(lst, position):
    return lst[position]
train['Name'].str.split(',').apply(get_element, position=0).head() # apply on function

train['Name'].str.split(',').apply(lambda x: x[0]).head() # lambda function

drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0)
drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=1).head() # apply function in terms of the axis

titanic['family_size'] = titanic.apply(lambda row: row['Pclass'] + row['SibSp'], axis=1) # apply DataFrame
#=========================================================================================================
# multi level index
stocks = pd.read_csv(r'http://bit.ly/smallstocks')

ser = stocks.groupby(['Symbol', 'Date'])['Close'].mean()
ser           # Series with multi index
ser.index     # Show the index of the Series
ser.unstack() # convert the series to a Data Frame

df = stocks.pivot_table(values= 'Close', index= 'Symbol', columns= 'Date')
df # make a Data Frame

# Select the location
ser.loc['AAPL', '2016-10-03']
ser.loc[:, '2016-10-03']

stocks.set_index(['Symbol', 'Date'], inplace= True)
stocks.sort_index(inplace= True)
stocks # convert the Data Frame with multi index Data Frame

# swap level
stocks.groupby(['Date', 'Symbol'])['Close'].sum().swaplevel().sort_index()

# Select from Data Frame
stocks.loc['AAPL']
stocks.loc['AAPL', '2016-10-03']
stocks.loc['AAPL', '2016-10-03']['Close']
stocks.loc[('AAPL', '2016-10-03'), :]
stocks.loc[('AAPL', '2016-10-03'), 'Close']
stocks.loc[(['AAPL', 'MSFT'], '2016-10-03'), :]
stocks.loc[(slice(None), ['2016-10-03', '2016-10-04']), :] # --> slice(None): select all the index

# merge the Data Frames
close = stocks.loc[:, 'Close']
volume = pd.read_csv(r'http://bit.ly/smallstocks', usecols=[0, 2, 3], index_col= ['Symbol', 'Date'])

both = pd.merge(close, volume, left_index= True, right_index= True)
both
#=========================================================================================================
# Merge Data Frames
# merge: join the Data Frames in terms of common columns in the Data Frames
df1 = pd.DataFrame({'ID': [1, 2, 3, 4], 'Name': ['Ali', 'Sara', 'Mohamed', 'Ahmed']})
df2 = pd.DataFrame({'ID':[1, 2, 3, 4], 'Order':[100, 150, 200, 250]})
pd.merge(df1, df2) # If you do the merge without common in column you will get an error

# If you want to merge Data Frames if there is no common in columns
df1 = pd.DataFrame({'ID': [1, 2, 3, 4], 'Name': ['Ali', 'Sara', 'Mohamed', 'Ahmed']})
df2 = pd.DataFrame({'Customer ID':[1, 2, 3, 4], 'Order':[100, 150, 200, 250]})
pd.merge(df1, df2, left_on='ID', right_on='Customer ID') # The two columns must have the same values

# join by the two indices in the Data Frame
df1 = pd.DataFrame({'Name': ['Ali', 'Sara', 'Mohamed']}, index = [1, 2, 3])
df2 = pd.DataFrame({'Order': [100, 150, 200]}, index = [1, 2, 4])
pd.merge(df1, df2, left_index= True, right_index= True)

# join by the index of one Data Frame
df1 = pd.DataFrame({'Name': ['Ali', 'Sara', 'Mohamed']}, index = [1, 2, 3])
df2 = pd.DataFrame({'Order': [100, 150, 200]}, index = [1, 2, 4])
pd.merge(df1, df2, left_index= True, right_on= 'Order', how='outer')

# join types
A = pd.DataFrame({'color':['green', 'yellow', 'red'], 'num':[1, 2, 3]})
B = pd.DataFrame({'color': ['green', 'yellow', 'pink'], 'size':['S', 'M', 'L']})

pd.merge(A, B, how='inner') # show the columns values in common in the key column
pd.merge(A, B, how='outer') # show the columns values in two Data Frames
pd.merge(A, B, how='left') # show the columns values in left Data Frame
pd.merge(A, B, how='right') # show the columns values in right Data Frame
#=========================================================================================================
# Select columns by data type
drinks.select_dtypes(include='number') # --> select numeric columns
drinks.select_dtypes(include='object') # --> select object columns
drinks.select_dtypes(include= ['number', 'object', 'category', 'datetime']) # --> select multiple columns
drinks.select_dtypes(exclude='number') # select not numeric columns
#=========================================================================================================
# Convert strings to numbers and avoid errors
df = pd.DataFrame({'col one': ['1.1', '2.2', '3.3'],
                   'col two': ['4.4', '5.5', '6.6'],
                   'col three': ['7.7', '8.8', '-']})
df.astype({'col one': float, 'col two': float})
pd.to_numeric(df['col three'], errors='coerce').fillna(0)
#=========================================================================================================
# Filter a Data Frame by multiple categories
movies[movies['genre'].isin(['Action', 'Drama', 'Western'])]
movies[~movies['genre'].isin(['Action', 'Drama', 'Western'])] # --> using not
#=========================================================================================================
# Filter a DataFrame by largest categories
counts = movies['genre'].value_counts()
counts.nlargest(3)
movies[movies['genre'].isin(counts.nlargest(3).index)]
#=========================================================================================================
# Handle missing values
ufo.dropna(axis=1).head()
ufo.dropna(thresh=len(ufo)*0.9, axis=1) # drop the column if it has more than 10 percent of nan values
#=========================================================================================================
# Split a string into multiple columns
df = pd.DataFrame({'name':['John Arther Doe', 'Jane Ann Smith'], 'location': ['Los Angelose, CA', 'Washington, DC']})
df[['first', 'middle', 'last']] = df['name'].str.split(' ', expand=True)
#=========================================================================================================
# Expand a Series of lists into a Data Frame
df = pd.DataFrame({'col one': ['a', 'b', 'c'], 'col two':[[10, 40], [20, 50], [30, 60]]})
df_new = df['col two'].apply(pd.Series)
pd.concat([df, df_new], axis=1)
#=========================================================================================================
# Aggregate by multiple functions
orders.groupby('order_id')['item_price'].sum()  # 1835 rows
total_price = orders.groupby('order_id')['item_price'].transform('sum') # 4622 rows
orders['total_price'] = total_price
orders['percent_of_total'] = orders['item_price'] / orders['total_price']
#=========================================================================================================
# Reshape a multi indexed Series
titanic.groupby(['Sex', 'Pclass'])['Survived'].mean().unstack()

# Create a pivot table
titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc= 'mean')
titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc= 'mean', margins=True)
titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc= 'count', margins=True)
#=========================================================================================================
# Check for the equality
df = pd.DataFrame({'a':[1, 2, np.nan], 'b':[1, 2, np.nan]})
print(df['a'] == df['b']) # --> Series of boolens
print(np.nan == np.nan) # --> False
print(df['a'].equals(df['b'])) # --> True
#=========================================================================================================
# Check the correlation between two columns or more
drinks['beer_servings'].corr(drinks['total_litres_of_pure_alcohol'])
drinks.corr(numeric_only=True) # --> check the correlation of all numeric columns in Data Frame
#=========================================================================================================
# Check the outliers and drop it
Q1 = drinks['beer_servings'].quantile(0.25) 
Q3 = drinks['beer_servings'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = drinks[(drinks['beer_servings'] < lower_bound) | (drinks['beer_servings'] > upper_bound)]
drinks_cleaned = drinks[(drinks['beer_servings'] >= lower_bound) & (drinks['beer_servings'] <= upper_bound)]
#=========================================================================================================
# difference between qcut and cut
# cut: returns equaled range of values
# qcut: returns equaled number of elements (quantiles)
data = pd.Series([1, 10, 20, 30, 40, 50])
pd.cut(data, bins=3)
pd.qcut(data, q=3, labels=['Low', 'Medium', 'High'])
#=========================================================================================================
# unpivot using melt function
# melt(id_vars, value_vars, var_name, value_name)
df = pd.DataFrame({'Name': ['Alice', 'Bob'],'Math': [85, 90],'Science': [88, 92]})
print(pd.melt(df, id_vars=['Name'], var_name='Subject', value_name='Score')) # melt the Data Frame
#=========================================================================================================
# interpolate function (useful for data cleaning)
# interpolate(method, axis, inplace)
# common methods: (linear, polynomial, spline, bfill, ffill, time, index, nearest)
data = {'A': [57.4, 24.9, np.nan, 329.2, 23.10]}
df = pd.DataFrame(data)
df_interpolated = df.interpolate(method='linear')
df_interpolated
#=========================================================================================================
# Time Series in pandas

# create time series data
dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
locations = ['Cairo', 'Alexandria', 'Mansoura']
df = pd.DataFrame([(date, loc) for date in dates for loc in locations], columns=['Date', 'Location'])

np.random.seed(42)
df['Total Spent'] = (
    100 + 20 * np.sin(df['Date'].dt.dayofyear * 2 * np.pi / 365) + 
    np.random.normal(loc=0, scale=10, size=len(df)) 
).round(2)

# resample (period)
df.set_index('Date', inplace=True)
df['Total Spent'].resample('M').mean()

# rolling(window: (7 or '30M'), min_periods)
df['Total Spent'].rolling(window=7).mean()

# shift(periods, fill_value, freq)
df['Date'].shift(periods=1)
#=========================================================================================================
# explode function
movies['actors_list'] = movies['actors_list'].apply(lambda x: eval(x))
movies.explode('actors_list')
#=========================================================================================================
# diff, pct_change and expanding
drinks['beer_servings'].diff()
drinks['beer_servings'].pct_change() # same as diff but in percentage
drinks['beer_servings'].expanding().sum() # cummulative 