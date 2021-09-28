import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime
from datetime import date
import requests
import math
import yfinance as yf

def Valuations(CompanyCode):
    Code = yf.Ticker(CompanyCode)
    count = 0
    Financials = Code.financials
    try:
        Gross_Margin = (Financials.loc['Total Revenue'][count]-Financials.loc['Cost Of Revenue'][count])/Financials.loc['Total Revenue'][count]
        if Gross_Margin < 0.5:
            return "",'','',''
    except:
        return '','','',''
    Balances = Code.balance_sheet
    Cashflow = Code.cashflow
    Number_Of_Shares = []
    Net_Income = []
    Total_Assets = []
    Operating_Cashflow = []
    ROE = []
    ROA = []
    Shareholder_Equity = []
    EPS = []
    try:
        while count < 4:
            Net_Income.append(float(Financials.loc['Net Income'][count]))
            Number_Of_Shares.append(float(Code.info['sharesOutstanding']))
            Shareholder_Equity.append(float(Balances.loc['Total Stockholder Equity'][count]))
            Total_Assets.append(Balances.loc['Total Assets'][count])
            Operating_Cashflow.append(float(Cashflow.loc['Total Cash From Operating Activities'][count]))
            ROE.append(round(Net_Income[count]/Shareholder_Equity[count],3))
            ROA.append(round(Net_Income[count]/Total_Assets[count],3))
            EPS.append(round(Net_Income[count]/Number_Of_Shares[count],3))
            count = count + 1
    except:
        return "",'','',''
    if ROE[0] < 0.07:
        return "",'','',''
    if ROA[0] < 0.07:
        return "",'','',''
    if EPS[0] < EPS[len(EPS)-1]:
        return "",'','',''
    if Operating_Cashflow[0]<Operating_Cashflow[1]:
        return "",'','',''
    try:
        PE_Ratio = Code.info['forwardPE']
        if PE_Ratio > 25:
            return "",'','',''
    except:
        PE_Ratio = Code.info['regularMarketPrice']/EPS[0]
        if PE_Ratio > 25:
            return "",'','',''
    return CompanyCode, ROA[0], ROE[0], PE_Ratio

def Screener_Runner():
    print("Screener is running... Let's find some value")
    df = pd.read_csv("US.csv")
    dick = 6
    while dick < 30:
        AUS = df['Code'][dick*100:(dick+1)*100]
        counter = 0
        Codes = []
        ROA = []
        ROE = []
        PE_Ratio = []
        for A in AUS:
            c,ra,re,pe = Valuations(A)
            if len(c)>0:
                Codes.append(c)
                ROA.append(ra)
                ROE.append(re)
                PE_Ratio.append(pe)
            print(counter)
            counter = counter + 1
        df2 = pd.DataFrame({'Company':Codes,'ROA':ROA,'ROE':ROE,'PE Ratio':PE_Ratio})
        filename = 'USQuality'+str(dick)+'.csv'
        print(filename)
        df2.to_csv(filename)
        print("Printed to csv")
        dick = dick + 1
    return


Screener_Runner()
