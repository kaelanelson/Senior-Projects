import numpy as np
import pandas as pd
def create_features(oecd16):
    """
    - oecd16: The cleaned dataset
    - Creates a new column that bins countries into "low life satisfaction"(4.8-5.8),
     "medium life satisfaction"(5.8-6.7), and "high life satisfaction"(6.7-7.6) categories.
    - Creates addition columns:(personal care)*(personal earnings) and (personal earnings)*(years in education)
    - Returns modified oecd16 with additional columns, and three dataframes grouped according to life satisfaction
    """
    bins = [4.8, 5.8, 6.7, 7.6]
    group_names = ["Low", "Medium", "High"]
    #Creating and adding new categories to each data set
    categories = pd.cut(oecd16["Life satisfaction"], bins, labels=group_names)
    oecd16['Satisfaction categories'] = pd.cut(oecd16["Life satisfaction"], bins, labels=group_names)
    oecd16['SatisfactionBinned'] = pd.cut(oecd16['Life satisfaction'], bins)
    #Group by satisfaction
    satisfaction16 = oecd16.groupby("Satisfaction categories")
    #Get low, medium, and high satisfaction groups
    low16 = satisfaction16.get_group("Low")
    medium16 = satisfaction16.get_group("Medium")
    high16 = satisfaction16.get_group("High")
    #Create new columns
    oecd16["Personal care*earnings"] = oecd16["Time devoted to leisure and personal care"]*oecd16["Personal earnings"]
    oecd16["earnings*education"] = oecd16["Time devoted to leisure and personal care"]*oecd16["Years in education"]
    return oecd16, low16, medium16, high16
