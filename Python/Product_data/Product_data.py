import pandas as pd
product = pd.read_csv('Product_data.csv')

print(product.columns)

#DATA CLEANING

      #Values null
print(product.isnull().sum())
      #Fill null values
      #I filled the null values with the median because 
      #it's fictitious data, and deleting values could alter the results, while adding values could also affect the outcome.
price_null = product[product['Price'].isnull()]
print(price_null[['Price']])
      #Complete average price
product['Price'] = product.groupby('Subcategory')['Price'].transform(lambda x: x.fillna(x.median()))
print("Fill values", product[['Subcategory', 'Price']])
      #Duplicate values
print('Duplicate values', product.duplicated().sum())
      #Type values
print("Type", product.dtypes)
      #Negative Values
negative_stock = product[product['Stock'] < 0]
print(negative_stock)
    #Convert all negative values to positive 
product['Stock'] = product['Stock'].apply(lambda x: abs(x))
print("Positive Stock Values", product[product['Stock']<0])

#DATA ANALYTICS

import seaborn as sns
import matplotlib.pyplot as plt

#CALCULATE TOTAL SALES

product['Total Sales USD'] = product['Stock'] * product['Price']
#GROUP BY PRODUCT NAME AND SUM THE TOTAL SALES
sales_by_product = product.groupby('Product Name')['Total Sales USD'].sum().reset_index()
#ORDER THE PRODUCTS BY TOTAL SALES IN DESCENDING ORDER
top_selling_products = sales_by_product.sort_values(by= 'Total Sales USD', ascending=False).head(10)
#View the top 10 selling products
plt.figure(figsize=(10,6))
sns.barplot(x='Total Sales USD', y='Product Name', data=top_selling_products, palette='viridis', hue='Product Name', legend=False)
plt.title('Top 10 best selling products (In USD)')
plt.xlabel('Total Sales USD')
plt.ylabel('Product Name')
plt.show()

#SALES ANALYSIS BY SPORT
#Identify which sports generate the most revenue in the store

product['Total Sales'] = product['Stock'] * product['Price']
       #Group by sports and sum the total sales
sales_by_sport = product.groupby('Sport')['Total Sales'].sum().reset_index()
       #Order Sports by sales in descending order
sales_by_sport = sales_by_sport.sort_values(by='Total Sales',ascending=False)
      #View sales by sports
plt.figure(figsize=(10,6))
sns.barplot(x='Total Sales', y='Sport', data=sales_by_sport, hue='Sport', palette='twilight', dodge=False,legend=False)
plt.title('Total Sales by Sport (In USD)')
plt.xlabel('Total Sales(USD)')
plt.ylabel('Sport')
plt.show()

#CORRELATION ANALYSIS BETWEEN STOCK AND SALES 
#Identify if there is any correlation between the available stock quantity and the sales generated.

         #Calculate correlation
correlation = product['Stock'].corr(product['Total Sales'])
print(f"Correlation between Stock and Total Sales: {correlation}")
         #Chart
plt.figure(figsize=(10,6))
sns.scatterplot(x='Stock', y='Total Sales', data=product)
plt.title('Stock and Total Sales')
plt.xlabel('Stock')
plt.ylabel('Total Sales USD')
plt.show()

       #Category Analysis
sales_by_category= product.groupby('Category')['Total Sales'].sum().reset_index()
sales_by_category= sales_by_category.sort_values(by='Total Sales', ascending=False)

plt.figure(figsize=(10,4))
sns.barplot(x='Total Sales', y='Category', data=sales_by_category)
plt.title('Total Sales by Category (In USD)')
plt.xlabel('Total Sales USD')
plt.ylabel('Category')
plt.show()

        #Subcategory Analysis
sales_by_subcategory = product.groupby('Subcategory') ['Total Sales'].sum().reset_index()
sales_by_subcategory = sales_by_subcategory.sort_values(by='Total Sales', ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x='Total Sales', y='Subcategory', data=sales_by_subcategory)
plt.title('Total Sales by Subcategory (In USD)')
plt.xlabel('Total Sales USD')
plt.ylabel('Subcategory')
plt.show()

for category in product['Category'].unique():
    subset = product[product['Category']== category]
    sns.scatterplot(x='Stock', y='Total Sales', data=subset)
    plt.title(f'Stock and Total Sales for {category}')
    plt.xlabel('Stock')
    plt.ylabel('Total Sales USD')
    plt.show()

for subcategory in product['Subcategory'].unique():
    subset = product[product['Subcategory']== subcategory]
    sns.scatterplot(x='Stock', y='Total Sales',data=subset)
    plt.title(f'Stock and Total Sales for {subcategory}')
    plt.xlabel('Stock')
    plt.ylabel('Total Sales USD')
    plt.show()

