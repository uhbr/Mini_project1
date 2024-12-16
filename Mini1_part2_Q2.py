import plotly.express as plty
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('laptop_price - dataset.csv') #reading the file
df_copy = df.copy() #copying the file to make sure to not harm it with me trying to write a code :)


def laptop_prices():
    '''A function that create a scatter graph of price by company''' 
    scatter_graph_price = plty.scatter(df_copy, x='Price (Euro)', y='Company', color='Company', 
                        title='Laptop price by company', labels={'Price': 'Price (Euro)'}, hover_data=['Product'])

    scatter_graph_price.show()


def mean_price():
    '''A function that calculate the mean price of each company's leptops'''
    mean_prices = df_copy.groupby('Company')['Price (Euro)'].mean().reset_index() #grouping by company and price, and calculating the mean of each one.
    mean_prices_sorted = mean_prices.sort_values(by='Price (Euro)', ascending=False) #sorting by price
    mean_prices_sorted = mean_prices_sorted.reset_index(drop=True) #reseting the index' to make it more clear and nice
    print(mean_prices_sorted)


def opsys_tests():
    '''A function that's doing different tests to the opsys column'''
    # first I'll unite the os by their type
    # (here I wrote a function that shows me all the operating systems that there are, and then deleted it when I finished using it)
    opsys_uni = df_copy.replace({"Windows 7":"Windows",
                                  "Windows 10":"Windows",
                                  "Windows 10 S": "Windows",
                                  "Mac OS X": "MacOS",
                                  "macOS":"MacOS"})
    opsys_uni_types = opsys_uni['OpSys'].unique() #finding the different types of OpSys
    print(opsys_uni_types) #printing the types
    

    # creating distribution plot for each OpSys 
    # for os in opsys_uni_types:
    #     os_data = opsys_uni[opsys_uni['OpSys'] == os]
    #     sns.histplot(os_data['Price (Euro)'], kde=True, bins=30, color='skyblue', 
    #                  stat="count")
        
    #     plt.title(f"Laptop Price Distribution for {os}")
    #     plt.xlabel('Price (Euro)')
    #     plt.ylabel('Amount (units)')
    #     plt.show()
    
    # I decided to show all the histograms plots in one window to make it more clear
    figure, plot_os = plt.subplots(2, 3)  #creating a window with 2 rows and 3 columns of plots
    
    plot_os = plot_os.flatten() #flatten the array cause it didn't work before I added it :) 

    # looping through the types list and ploting each one
    for i, os in enumerate(opsys_uni_types):
        os_data = opsys_uni[opsys_uni['OpSys'] == os]
        
        # plot each histogram
        sns.histplot(os_data['Price (Euro)'], kde=True, bins=30, color='skyblue', 
                     stat="count", ax=plot_os[i])
        
        # setting the titles of the plots
        plot_os[i].set_title(f"Laptop Price Distribution for {os}", fontsize=7) #making the font size smaller to avoid overlapping
        plot_os[i].set_xlabel('Price (Euro)')
        plot_os[i].set_ylabel('Amount (units)')

    plt.tight_layout() #another line to avoid overlap
    plt.show()

    # I wrote a histogram to show all of them on one another but decided it was less good
    # dist_graph = plty.histogram(sort_by_price, x="Price (Euro)", color="OpSys", 
    #                title="Laptop Price Distribution by Operating System",
    #                nbins=30)
    # dist_graph.show()


def ram_price_correlation():
    '''A function that calculate the correlation between the RAM and the price'''
    # calculating the correlation
    corr_ram_price = df_copy['RAM (GB)'].corr(df_copy['Price (Euro)'])
    print(f"The correlation between the RAM and the price: {corr_ram_price:.2f}") #printing the corr
    
    #creating a regression plot
    sns.regplot(x='RAM (GB)', y='Price (Euro)', data=df_copy, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
    
    plt.title('RAM-Price correlation')
    plt.xlabel('RAM (GB)')
    plt.ylabel('Price (Euro)')
    plt.show()


def new_storage_type():
    '''A function that create new column based on the Memory column'''
    storage_type = df_copy['Memory'].copy() #copying the column

    # here I printed all the Memory unique types, to know what I need to change. removed it when I was done with it.

    storage_sizes = ['1.0TB', '128GB', '16GB', '180GB', '1TB', '2TB', '240GB', 
                     '256GB', '500GB', '32GB', '508GB', '512GB', '64GB', '8GB', ' ']

    # looping through the list of the storage_sizes and removing them from the storage type
    for size in storage_sizes:
        storage_type = storage_type.str.replace(size, '')

    print(storage_type.unique())

# laptop_prices()
# mean_price()
# opsys_tests()
# ram_price_correlation()
# new_storage_type()


# Bonus question
# My question would be what is the strongest correlation?
# To solve it I would create a correlation matrix.

numeric_df = df_copy.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()