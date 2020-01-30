import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

def plot_health_vs_network(low16, medium16, high16):
    """Plots Self-reported health vs. Quality of support network:
    Self-reported health : This indicator refers to the percentage of the
    population aged 15 years old and over who report “good” or better health.

    low16: Low satisfied countries (4.8-5.8)
    medium16: Medium satisfied countries (5.8-6.7)
    high16: High satisfied countries (6.7-7.6)

    Quality of support network: The indicator is based on the question: “If
    you were in trouble, do you have relatives or friends you can count on
    to help you whenever you need them, or not?” and it considers the
    respondents who respond positively.

    First plot contains all three categories on the same plot, with all of their
    lines of best fit from OLS model.

    Second plot shows low life satisfaction countries with line of best fit
    from OLS model.
    Third plot shows low life satisfaction countries with line of best fit
    from OLS model.
    Fourth plot shows low life satisfaction countries with line of best fit
    from OLS model."""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row',
                                                 figsize=(13,8))
    X = [low16["Self-reported health"], medium16["Self-reported health"],
         high16["Self-reported health"],low16["Self-reported health"],
         medium16["Self-reported health"], high16["Self-reported health"]]
    y = [low16["Quality of support network"], medium16["Quality of support network"],
         high16["Quality of support network"],low16["Quality of support network"],
         medium16["Quality of support network"], high16["Quality of support network"]]
    labels = ["low satisfaction", "medium satisfaction", "high satisfaction", "low satisfaction", "medium satisfaction", "high satisfaction"]
    colors = ["b", "c", "g","b", "c", "g"]
    bins1 = [low16["Self-reported health"], medium16["Self-reported health"],
             high16["Self-reported health"], low16["Self-reported health"],
             medium16["Self-reported health"], high16["Self-reported health"]]
    bins2 = [low16["Quality of support network"], medium16["Quality of support network"],
             high16["Quality of support network"],low16["Quality of support network"],
             medium16["Quality of support network"], high16["Quality of support network"]]
    axes = [ax1, ax1, ax1, ax2, ax3, ax4]

    for x, y,ax, label, color, bin1, bin2 in zip(X, y, axes, labels, colors, bins1, bins2):
        x = sm.add_constant(x)
        results = sm.OLS(y, x).fit()
        x_lim = np.linspace(30, 90)
        ax.plot(x_lim, results.params[0] + results.params[1]*x_lim,color=color)
        ax.scatter(bin1, bin2, label=label, color=color)
        ax.legend(loc="lower right")
        if ax != ax1:
            ax.set_title(f"$y = {results.params[0]} + ({results.params[1]})*x$")
        elif ax == ax1:
            ax.set_title("All Countries")


    #common x and y labels, title
    plt.suptitle('Self-reported health vs. Quality of support network',fontsize = 14.5)
    fig.text(0.5, 0.04, 'Quality of support network (percentage)', ha='center',
             va='center',fontsize = 14.5)
    fig.text(0.06, 0.5, 'Self-reported health (percentage)', ha='center', va='center',
             rotation='vertical',fontsize = 14.5)

    plt.show()
