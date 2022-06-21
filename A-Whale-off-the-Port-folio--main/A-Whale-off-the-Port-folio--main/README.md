# A-Whale-off-the-Port-folio-
## Unit 4 Homework Assignment: A Whale Off the Port(folio)




### Assignment requirements

For this assignment it was required to analyze and visualize the major metrics of the portfolios across all of the areas given, and determine which portfolio outperformed the others. It was then required to create a custom portfolio of stocks and compare its performance to that of the other portfolios, as well as the larger market S&P TSX 60 Index.


---


### Steps

The first step was to read and clean the CSV files for analysis. The CSV files include whale portfolio returns, algorithmic trading portfolio returns, and S&P TSX 60 Index historical prices. 

The second step was to Use Pandas to read the CSV files as a DataFrame, and convert the dates to a DateTimeIndex.


The third step was to detect and remove null values.

Some columns had dollar signs and other characters other than numeric values, removal of these characters was needed and they had to be converted to a float variable.

The forth step was to convert the S&P TSX 60 CSV file which contained closing prices and convert the S&P TSX 60 closing prices to daily returns.

The fifth step was to Join Whale Returns, Algorithmic Returns, and theS&P TSX 60 Returns` into a single DataFrame with columns for each portfolio's returns.

The sixth step was to 

1. Calculate and plot daily returns of all portfolios.

2. Calculate and plot cumulative returns for all portfolios and check if  any portfolio outperform the S&P TSX 60?

3.  Create a box plot for each of the returns. 

4. Calculate the standard deviation for each portfolio. 

5. Determine which portfolios are riskier than the S&P TSX 60

6. Calculate the Annualized Standard Deviation.

7. Calculate and plot the rolling standard deviation for all portfolios using a 21-day window.

8. Calculate and plot the correlation between each stock to determine which portfolios may mimic the S&P TSX 60.

9. Choose one portfolio, then calculate and plot the 60-day rolling beta for it and the S&P TSX 60.

The seventh step was to 

1. Using the daily returns, calculate and visualize the Sharpe ratios using a bar plot.

2. Determine whether the algorithmic strategies outperform both the market (S&P TSX 60) and the whales portfolios.

The eighth step was to create a self portfolio and:

1. Visit [Google Sheets](https://docs.google.com/spreadsheets/) and use the built-in Google Finance function to choose 3 stocks for the portfolio.

2. Download the data as CSV files and calculate the portfolio returns.

3. Calculate the weighted returns for your portfolio, assuming equal number of shares per stock.

4. Add the portfolio returns to the DataFrame with the other portfolios.

5. Run the following analyses:

    * Calculate the Annualized Standard Deviation.
    * Calculate and plot rolling std with a 21-day window.
    * Calculate and plot the correlation.
    * Calculate and plot the 60-day rolling beta for your portfolio compared to the S&P 60 TSX.
    * Calculate the Sharpe ratios and generate a bar plot.

4. Comment on how the created portfolio compared to the other holdings


---


