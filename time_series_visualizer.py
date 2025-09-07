# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()

# # Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# df = None

# # Clean data
# df = None


# def draw_line_plot():
#     # Draw line plot





#     # Save image and return fig (don't change this part)
#     fig.savefig('line_plot.png')
#     return fig

# def draw_bar_plot():
#     # Copy and modify data for monthly bar plot
#     df_bar = None

#     # Draw bar plot





#     # Save image and return fig (don't change this part)
#     fig.savefig('bar_plot.png')
#     return fig

# def draw_box_plot():
#     # Prepare data for box plots (this part is done!)
#     df_box = df.copy()
#     df_box.reset_index(inplace=True)
#     df_box['year'] = [d.year for d in df_box.date]
#     df_box['month'] = [d.strftime('%b') for d in df_box.date]

#     # Draw box plots (using Seaborn)





#     # Save image and return fig (don't change this part)
#     fig.savefig('box_plot.png')
#     return fig

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data by removing top 2.5% and bottom 2.5%
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

def draw_line_plot():
    data = df.copy()

    plt.figure(figsize=(15,5))
    plt.plot(data.index, data['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    plt.savefig('lineplot.png')
    plt.show()  # <-- This will display the plot interactively
    return plt.gcf()

def draw_bar_plot():
    data = df.copy()
    
    # Add year and month columns
    data['year'] = data.index.year
    data['month'] = data.index.month
    
    # Pivot table to get average views per month per year
    df_bar = data.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Plot
    ax = df_bar.plot(kind='bar', figsize=(15,7))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    
    plt.savefig('barplot.png')
    plt.show()  # <-- Display plot
    return plt.gcf()

def draw_box_plot():
    data = df.copy()
    data.reset_index(inplace=True)
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.strftime('%b')
    data['month_num'] = data['date'].dt.month  # for sorting months correctly
    
    # Sort months by month number
    data = data.sort_values('month_num')
    
    fig, axes = plt.subplots(1, 2, figsize=(20,6))
    
    # Year-wise box plot (Trend)
    sns.boxplot(x='year', y='value', data=data, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot (Seasonality)
    sns.boxplot(x='month', y='value', data=data, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.savefig('boxplot.png')
    plt.show()  # <-- Display plot
    return plt.gcf()
