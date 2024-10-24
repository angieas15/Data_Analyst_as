import pandas as pd
canine = pd.read_csv('/Users/angiearagonsogamoso/Desktop/Data_Analyst_as/Python/Deportecanino/deportecanino_cost_csv.csv')

#name of columns 
print(canine.columns)

#UNITS SOLD BY PRODUCT 2022
#DATETIME
canine['Date'] = pd.to_datetime(canine['Date'])
#FILTER BY 2022 
canine_2022 = canine[canine['Date'].dt.year == 2022]
#GROUP BY PRODUCT
sales_product_2022 = canine_2022.groupby('Product_Name')['Units_Sold'].sum().reset_index()
#ORDER BY UNITS SALES
sales_product_2022 = sales_product_2022.sort_values(by='Units_Sold',ascending=False)
print('BY PRODUCT 2022')
print(sales_product_2022)


#UNITS SOLD BY PRODUCT 2023
#DATETIME
canine['Data'] = pd.to_datetime(canine['Date'])
#FILTER BY 2023
canine_2023 = canine[canine['Date'].dt.year == 2023]
#GROUP BY PRODUCT
sales_product_2023 = canine_2023.groupby('Product_Name')['Units_Sold'].sum().reset_index()
#ORDER BY UNITS SALES
sales_product_2023 = sales_product_2023.sort_values(by='Units_Sold',ascending=False)
print('BY PRODUCT 2023')
print(sales_product_2023)

#UNITS SOLD BY CATEGORY 2022
#DATETIME
canine['Data'] = pd.to_datetime(canine['Date'])
canine_category_2022 = canine[canine['Date'].dt.year == 2022]
sales_category_2022 = canine_category_2022.groupby('Product_Category')['Units_Sold'].sum().reset_index()
sales_category_2022 = sales_category_2022.sort_values(by='Units_Sold',ascending=False)
print('CATEGORY 2022: ')
print(sales_category_2022)

#UNITS SOLD BY CATEGORY 2023
#DATETIME
canine['Data'] = pd.to_datetime(canine['Date'])
canine_category_2023 = canine[canine['Date'].dt.year == 2023].copy()
sales_category_2023 = canine_category_2023.groupby('Product_Category')['Units_Sold'].sum().reset_index()
sales_category_2023 = sales_category_2023.sort_values(by='Units_Sold',ascending=False)
print('CATEGORY 2023')
print(sales_category_2023)




#CALCULATE THE CONTRIBUTION MARGIN 2022
canine['Data'] = pd.to_datetime(canine['Date'])
MC_canine_product_2022 = canine[canine['Date'].dt.year == 2022].copy()
#Create a new column CVT
MC_canine_product_2022.loc[: ,'CVT'] = canine['Cost_of_Production'] + canine['Shipping_Cost']
contribution_margin = MC_canine_product_2022.groupby('Product_Name').agg({
    'Unit_Price': 'first',
    'Cost_of_Production': 'first',
    'Shipping_Cost':'first',
    'CVT':'first',
    'Discount':'first',
}).reset_index()
contribution_margin['MC'] = contribution_margin['Unit_Price'] - contribution_margin['CVT']
contribution_margin = contribution_margin.sort_values('Unit_Price', ascending= False)
print('CONTRIBUTION MARGIN BY PRODUCT 2022')
print(contribution_margin[['Product_Name','Unit_Price','Cost_of_Production','Shipping_Cost','CVT','MC']])

#Calculate Discount
#New column Discount
contribution_margin ['MC'] = contribution_margin['Unit_Price'] - contribution_margin['CVT']
#Calculate the new unit price with descount 
contribution_margin ['Price_with_Discount'] = contribution_margin['Unit_Price'] * (1 - contribution_margin['Discount']) 
#Calculate the new contribution margin with the price discount 
contribution_margin['New_MC'] = contribution_margin['Price_with_Discount'] - contribution_margin['CVT']
#Calculate the reduction in the contribution margin
contribution_margin ['Reduction_MC'] = contribution_margin['MC'] - contribution_margin['New_MC']
contribution_margin = contribution_margin.sort_values('Reduction_MC', ascending=False)
print('Discount 2022')
print(contribution_margin[['Product_Name','Unit_Price','CVT','MC','Discount','Price_with_Discount','New_MC','Reduction_MC']])


#CALCULATE THE CONTRIBUTION MARGIN 2023
canine['Data'] =  pd.to_datetime(canine['Date'])
MC_canine_product_2023 = canine[canine['Date'].dt.year == 2023].copy()
#Create a new column CVT
MC_canine_product_2023.loc[:, 'CVT'] = canine['Cost_of_Production'] + canine['Shipping_Cost']
contribution_margin_2023 = MC_canine_product_2023.groupby('Product_Name').agg({
    'Unit_Price': 'first',
    'Cost_of_Production':'first',
    'Shipping_Cost':'first',
    'CVT': 'first',
    'Discount':'first',
}).reset_index()
contribution_margin_2023['MC'] = contribution_margin_2023 ['Unit_Price'] - contribution_margin_2023 ['CVT']
contribution_margin_2023 = contribution_margin_2023.sort_values('Unit_Price', ascending=False)
print('CONTRIBUTION MARGING BY 2023')
print(contribution_margin_2023 [['Product_Name','Unit_Price','Cost_of_Production','Shipping_Cost','CVT','MC']])

#Claculate Discount
#New Column Discount
contribution_margin_2023['MC'] = contribution_margin_2023['Unit_Price'] - contribution_margin_2023['CVT']
#Calculate the new unit price with discount
contribution_margin_2023['Price_with_Discount'] = contribution_margin_2023['Unit_Price'] * (1 - contribution_margin_2023['Discount'])
#Calculate the new contribution margin with the price discount
contribution_margin_2023['New_MC'] = contribution_margin_2023['Price_with_Discount'] - contribution_margin_2023['CVT']
#Calculate the reduction in the contribution margin
contribution_margin_2023['Reduction_MC'] = contribution_margin_2023['MC'] - contribution_margin_2023['New_MC']
contribution_margin_2023 = contribution_margin_2023.sort_values('Reduction_MC', ascending=False)
print('Discount 2023')
print(contribution_margin_2023[['Product_Name', 'Unit_Price', 'CVT', 'MC', 'Discount', 'Price_with_Discount', 'New_MC','Reduction_MC']])



#Profit by product 2022
canine['Data'] = pd.to_datetime(canine['Date'])
profit_2022 = canine[canine['Date'].dt.year == 2022].copy()
result = profit_2022[['Product_Name','Profit']]
result = result.sort_values('Profit',ascending=False)
print('PROFIT BY PRODUCT 2022')
print(result)

#Profit by product 2023
canine['Data'] = pd.to_datetime(canine['Date'])
profit_2023 = canine[canine['Date'].dt.year == 2023].copy()
result_23 = profit_2023[['Product_Name','Profit']]
result_23 = result_23.sort_values('Profit',ascending=False)
print('PROFIT BY PRODUCT 2023')
print(result_23)

#Add column Analysis to CVS
sales_product_2022['Analysis'] = 'Sales by Product 2022'
sales_product_2023['Analysis'] = 'Sales by Product 2023'
sales_category_2022['Analysis'] = 'Sales by Category 2022'
sales_category_2023['Analysis'] = 'Sales by Category 2023'
contribution_margin['Analysis'] = 'Contribucition Margin 2022'
contribution_margin_2023['Analysis'] = 'Contribution Margin 2023'
result['Analysis'] = 'Profit by Product 2022'
result_23['Analysis'] = 'Profit by Product 2023'

#Combinable results
all_data_canine = pd.concat([sales_product_2022, sales_product_2023, sales_category_2022,sales_category_2023,
contribution_margin,contribution_margin_2023,result,result_23], ignore_index=True)

#Export
all_data_canine.to_csv('all_analysis_result.csv',index=False)