import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

def create_leisure_earnings_educ(oecd16):
    """Time devoted to leisure and personal care: This indicator measures the amount
    of minutes (or hours) per day that, on average, full-time employed people spend
    on leisure and on personal care activities.

    Personal earnings:This indicator refers to the average annual wages per full-
    time equivalent dependent employee

    Years in education:This indicator is the average duration of education in
    which a 5 year old child can expect to enrol during his/her lifetime until
    the age of 39.

    oecd16: Cleaned data set

    Plots the following along life satisfaction: Time devoted to leisure and personal care,
    Personal earnings, Years in education
"""
    #creates subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30,10))

    #1st plot:"Time devoted to leisure and personal care" vs. life satisfaction
    X1 = oecd16["Time devoted to leisure and personal care"]
    y1 = oecd16["Life satisfaction"]
    X1 = sm.add_constant(X1)
    #fit OLS model
    results1 = sm.OLS(y1, X1).fit()
    x_lim1 = np.linspace(11, 17)
    ax1.plot(x_lim1, results1.params[0] + results1.params[1]*x_lim1, color="r")
    ax1.scatter(oecd16["Time devoted to leisure and personal care"],
                oecd16["Life satisfaction"], label="Country")
    ax1.set_xlabel("Time devoted to leisure and personal care (Hours)",
                   fontsize = 25)
    ax1.set_ylabel("Life satisfaction (0-10)", fontsize = 25)
    ax1.set_title(f"$y = {results1.params[0]} + ({results1.params[1]})*x$",
                  fontsize = 21)
    ax1.legend()
    plt.rcParams['xtick.labelsize']=20
    plt.rcParams['ytick.labelsize']=20

    #2nd plot: Personal earnings vs. life satisfaction
    X2 = oecd16["Personal earnings"]
    y2 = oecd16["Life satisfaction"]
    X2 = sm.add_constant(X2)
    #fit OLS model
    results2 = sm.OLS(y2, X2).fit()
    x_lim2 = np.linspace(8000, 61000)
    ax2.plot(x_lim2, results2.params[0] + results2.params[1]*x_lim2, color="r")
    ax2.scatter(oecd16["Personal earnings"], oecd16["Life satisfaction"],
                label="Country")
    ax2.set_xlabel("Personal Earnings (US Dollars)", fontsize = 25)
    ax2.set_title(f"$y = {results2.params[0]} + ({results2.params[1]})*x$",
                  fontsize = 21)
    ax2.legend()

    #3rd plot: Years in education vs. life satisfaction
    X3 = oecd16["Years in education"]
    y3 = oecd16["Life satisfaction"]
    X3 = sm.add_constant(X3)
    #fit OLS model
    results3 = sm.OLS(y3, X3).fit()
    x_lim3 = np.linspace(14, 20)
    ax3.plot(x_lim3, results3.params[0] + results3.params[1]*x_lim3, color="r")
    ax3.scatter(oecd16["Years in education"], oecd16["Life satisfaction"],
                label="Country")
    ax3.set_xlabel("Years in education", fontsize = 25)
    ax3.set_title(f"$y = {results3.params[0]} + ({results3.params[1]})*x$",
                  fontsize = 21)
    ax3.legend()

    plt.rcParams['xtick.labelsize']=30
    plt.rcParams['ytick.labelsize']=30
    plt.tight_layout()
    plt.show()
