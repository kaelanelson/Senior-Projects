import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

def plot_earnings_vs_care(low16, medium16, high16):
    """Plots Personal earnings vs. Time devoted to personal care:
    Personal Earnings: This indicator refers to the average annual wages per full-time equivalent dependent employee
    Time devoted to personal care: This indicator measures the amount of minutes (or hours) per day that, on average,
    full-time employed people spend on leisure and on personal care activities.

    Life satisfaction: The indicator considers people's evaluation of their life as a whole. It is a weighted-sum of different response categories based on people's rates of their current life relative to the best and worst
    possible lives for them on a scale from 0 to 10, using the Cantril Ladder (known also as the "Self-Anchoring Striving Scale").
    low16: Low satisfied countries (4.8-5.8)
    medium16: Medium satisfied countries (5.8-6.7)
    high16: High satisfied countries (6.7-7.6)

    First plot contains all three categories on the same plot, with all of their lines of best fit
    Second plot shows low life satisfaction countries with line of best fit from OLS model
    Third plot shows low life satisfaction countries with line of best fit from OLS model
    Fourth plot shows low life satisfaction countries with line of best fit from OLS model"""

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(13,8))
    X = [low16["Personal earnings"], medium16["Personal earnings"], high16["Personal earnings"],low16["Personal earnings"],medium16["Personal earnings"], high16["Personal earnings"]]
    y = [low16["Time devoted to leisure and personal care"], medium16["Time devoted to leisure and personal care"], high16["Time devoted to leisure and personal care"],low16["Time devoted to leisure and personal care"], medium16["Time devoted to leisure and personal care"], high16["Time devoted to leisure and personal care"]]
    labels = ["Low Satisfaction", "Medium Satisfaction", "High Satisfaction", "Low Satisfaction", "Medium Satisfaction","High Satisfaction"]
    colors = ["b", "c", "g","b", "c", "g"]
    bins1 = [low16["Personal earnings"], medium16["Personal earnings"], high16["Personal earnings"], low16["Personal earnings"], medium16["Personal earnings"], high16["Personal earnings"]]
    bins2 = [low16["Time devoted to leisure and personal care"], medium16["Time devoted to leisure and personal care"],high16["Time devoted to leisure and personal care"],low16["Time devoted to leisure and personal care"], medium16["Time devoted to leisure and personal care"], high16["Time devoted to leisure and personal care"]]
    axes = [ax1, ax1, ax1, ax2, ax3, ax4]

    for x, y,ax, label, color, bin1, bin2 in zip(X, y, axes, labels, colors, bins1, bins2):
        x = sm.add_constant(x)
        results = sm.OLS(y, x).fit()
        x_lim = np.linspace(0, 70000)
        ax.plot(x_lim, results.params[0] + results.params[1]*x_lim,color=color)
        ax.scatter(bin1, bin2, label=label, color=color)
        ax.legend(loc="lower right")
        if ax != ax1:
            ax.set_title(f"$y = {results.params[0]} + ({results.params[1]})*x$")
        elif ax == ax1:
            ax.set_title("All Countries")

    #common x and y labels, title
    plt.suptitle('Personal care vs. Personal Earnings',fontsize = 14.5)
    fig.text(0.5, 0.04, 'Personal Earnings (US Dollars)', ha='center', va='center',fontsize = 14.5)
    fig.text(0.06, 0.5, 'Personal Care (Hours)', ha='center', va='center', rotation='vertical',fontsize = 14.5)

    plt.show()
