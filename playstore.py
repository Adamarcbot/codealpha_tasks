import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.backends.backend_pdf

df = pd.read_csv("google playstore data.csv")
df = df[df['Rating'] <= 5]
df.dropna(inplace=True)
df['Installs'] = df['Installs'].str.replace('+', '', regex=False).str.replace(',', '').astype(int)
df['Price'] = df['Price'].str.replace('$', '', regex=False).astype(float)
df['Reviews'] = df['Reviews'].astype(int)

plt.figure(figsize=(8, 5))
sns.histplot(df['Rating'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of App Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Apps')

plt.figure(figsize=(6, 6))
df['Type'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'orange'])
plt.title('Free vs Paid Apps')
plt.ylabel('')

plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='Category', order=df['Category'].value_counts().index)
plt.title('Number of Apps per Category')
plt.xlabel('Count')
plt.ylabel('Category')

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Reviews', y='Rating', alpha=0.3)
plt.title('Reviews vs Ratings')
plt.xlabel('Reviews')
plt.ylabel('Rating')

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Type', y='Installs')
plt.title('Install Distribution by App Type')
plt.xlabel('Type')
plt.ylabel('Installs')

plt.figure(figsize=(12, 6))
category_installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(15)
category_installs.plot(kind='bar', color='slateblue')
plt.title('Top 15 Categories by Total Installs')
plt.xlabel('Category')
plt.ylabel('Total Installs')

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df[df['Price'] > 0], x='Price', y='Rating', color='darkred')
plt.title('Price vs Rating (Paid Apps)')
plt.xlabel('Price ($)')
plt.ylabel('Rating')

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Content Rating', palette='Set2')
plt.title('Content Rating Distribution')
plt.xlabel('Content Rating')
plt.ylabel('Number of Apps')
plt.xticks(rotation=45)

plt.figure(figsize=(12, 6))
top_categories = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)
top_categories.plot(kind='barh', color='mediumseagreen')
plt.title('Top 10 Categories by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Category')

summary = df.describe()
top_paid = df[df['Price'] > 0].sort_values('Price', ascending=False)[['App', 'Price']].head(5)
top_installed = df.sort_values('Installs', ascending=False)[['App', 'Installs']].head(5)

print("\n Summary Statistics:")
print(summary)
print("\n Top 5 Most Expensive Apps:")
print(top_paid)
print("\n Top 5 Most Installed Apps:")
print(top_installed)

pdf = matplotlib.backends.backend_pdf.PdfPages("Google_Play_Analysis_Report.pdf")
for fig_num in plt.get_fignums():
    pdf.savefig(plt.figure(fig_num))
pdf.close()

print("\n Report saved successfully as: Google_Play_Analysis_Report.pdf")
