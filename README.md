# Portfolio-Analysis-Tool
These excel files are being used to give a suggested asset allocation to ETFs for the AUS portfolio and individual companies and ETFs for the US portfolio

The first file is the mean-variance analysis of some AUS ETFs. The use of ETFs is due to my lower capital, so more exposure and diversification while not trying to lose
too much money to brokerage. These ETFs were selected from a Betashares growth model, and then run using the last 2 years of their returns. On the last page of the sheet, 
the dividend included returns were solved for Sharpe optimisation which gave the weights to invest into each ETF, with a constraint that there would be no shorting of ETFs.
The dividends were then looked into to make sure they cover interest payments on the margin loan which they did by 3 times.

The US mean variance excel sheet completes similiar analysis to the AUS ETFs analysis, except uses both shares and ETFs. The data used is adjusted close for the 
splits and dividends to be taken into account. There was also a maximum put on each individual weighting of 0.16 so that there would have to be at least 6 holdings in the
portfolio. This was the only constraint, aside from there being no shorting again.

As an extension on this I have coded a value screener that looks through all ASX companies, and all lower cap Russell 3000 companies and outputs in excel sheets ones that have 
certain value features. This list is going towards the investments into smaller cap companies as the satellites to the mega cap and index core.
