# %% 
import pandas as pd

# %% 
df = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)
df = df[0]
df

# %% zd.1
df.rename(columns={'TITLE':'TYTUŁ','ARTIST':'ARTYSTA','YEAR':'ROK', 'HIGH POSN':'MAX POZ'}, inplace=True)
df

# %% zd.2
df['ARTYSTA'].nunique()

# %% zd.3
df['ARTYSTA'].value_counts()

# %% zd.4
df.columns = ['Pos', 'Tytuł', 'Artysta', 'Rok', 'Max Poz']

# %% zd.5
df.drop('Max Poz', axis=1, inplace=True)

# %% zd.6
df['Rok'].value_counts()

# %% zd.7
df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)]['Tytuł'].count()

# %% zd.8
df['Rok'].min()

# %% zd.9
df.groupby('Artysta')['Rok'].min()

# %% zd.10
df.to_csv('artists_data.csv')