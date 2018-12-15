import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

def plot_earningscare(oecd16):
    """Plots relationship between (personal earnings)* (personal care)
    and earnings*education

    oecd16: Cleaned data set
    """
    #create subplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(17,5))
    X1 = oecd16["Personal care*earnings"]
    y1 = oecd16["Life satisfaction"]
    #fit model
    X1 = sm.add_constant(X1)
    results1 = sm.OLS(y1, X1).fit()

    #plot line of best fit and Personal care*earnings vs. Life satisfaction
    x_lim1 = np.linspace(0, 900000)
    ax1.plot(x_lim1, results1.params[0] + results1.params[1]*x_lim1, color="r")
    ax1.scatter(oecd16["Personal care*earnings"], oecd16["Life satisfaction"],
                label="Country")
    ax1.set_xlabel("(Personal care)*earnings (hours*dollars)", fontsize = 14.5)
    ax1.set_ylabel("Life satisfaction (0-10)",fontsize = 14.5)
    ax1.set_title(f"$y = {results1.params[0]} + ({results1.params[1]})*x$",
                  fontsize = 14.5)
    ax1.legend()

    X2 = oecd16["earnings*education"]
    y2 = oecd16["Life satisfaction"]
    X2 = sm.add_constant(X2)
    #fit model
    results2 = sm.OLS(y2, X2).fit()
    x_lim2 = np.linspace(175, 325)
    #plot line of best fit and earnings*education vs. Life satisfaction
    ax2.plot(x_lim2, results2.params[0] + results2.params[1]*x_lim2, color="r")
    ax2.scatter(oecd16["earnings*education"], oecd16["Life satisfaction"],
                label="Country")

    #set labels and sizes
    ax2.set_xlabel("Earnings*education (dollars*years)", fontsize = 14.5)
    ax2.set_title(f"$y = {results2.params[0]} + ({results2.params[1]})*x$",
                  fontsize = 14.5)
    ax2.legend()
    plt.rcParams['xtick.labelsize']=20
    plt.rcParams['ytick.labelsize']=20
    plt.show()
