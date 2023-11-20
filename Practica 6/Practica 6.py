import numpy as np
import statsmodels as sm
import statsmodels.tools.tools as smTools
import statsmodels.regression.linear_model as smLinearModel
import pandas as pd
import matplotlib.pyplot as plt


#Linear regression + graph
def scatter(x,y,color,title,save, labelx, labely):
    plt.scatter(x,y, c=color, edgecolors='black', linewidths=1, alpha=0.75)
    plt.title(title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    linearRegression(x,y, color)
    plt.savefig(save)
    plt.clf()
    olsRegressionResult(x,y)
    
def linearRegression(x ,y, color):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    print(z)
    print(p)
    plt.plot(x, p(x), c=color, linewidth=3)
    
#Statsmodels OLS
def olsRegressionResult(x,y):
    x = smTools.add_constant(x)
    
    model = smLinearModel.OLS(y,x)
    
    results = model.fit()
    print(results.summary())

#Gold Distribution
def Dist(df, pos1, pos2, pos3, pos4):
    v1B = []
    v2B = []
    v1R = []
    v2R = []
    
    for data in df.values:
        v1B.append(data[pos1])
        v2B.append(data[pos2])
        v1R.append(data[pos3])
        v2R.append(data[pos4])
        
    return [v1B, v2B, v1R, v2R]    

#Read CSV
df = pd.read_csv("../Practica 2/cleaned_rankedGames.csv")
colorB = "#2d27a3"
colorR = "#eb4034"

gB, eB, gR, eR = Dist(df, 9, 10, 18, 19)
#Regresion para equipo azul Oro - Exp
scatter(gB,eB, colorB,"Distribucion Oro - Exp", "Scatter_OroExpBlue.png", "Oro", "Experiencia")
#Regresion para equipo rojo Oro - Azul
scatter(gR,eR, colorR,"Distribucion Oro - Exp", "Scatter_OroExpRed.png", "Oro", "Experiencia")

fB, kB, fR, kR = Dist(df, 6, 12, 15, 21)
#Regresion para equipo azul farmJG - Kills
scatter(fB, kB, colorB, "Distribuccion Asesinatos - Farm del Jg", "Scatter_KillsFarmJGBlue.png", "Kills", "Farm del Jg")
#Regresion para equipo rojo farmJG - Kills
scatter(fR, kR, colorR, "Distribuccion Asesinatos - Farm del Jg", "Scatter_KillsFarmJGRed.png", "Kills", "Farm del Jg")

wB, dB, wR, dR = Dist(df, 4, 15, 13, 6)
#Regresion para equipo azul Wards - Muertes
scatter(dB, wB, colorB, "Distribuccion Muertes - Wards", "Scatter_KillsWardsBlue.png", "Muertes", "Wards")
#Regresion para equipo rojo Wards - Muertes
scatter(dR, wR, colorR, "Distribuccion Muertes - Wards", "Scatter_KillsWardsRed.png", "Muertes", "Wards")

# #Output:
# [5.28697092e-01 9.20278119e+03]
 
# 0.5287 x + 9203
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.457
# Model:                            OLS   Adj. R-squared:                  0.457
# Method:                 Least Squares   F-statistic:                     8321.
# Date:                Thu, 19 Oct 2023   Prob (F-statistic):               0.00
# Time:                        17:49:18   Log-Likelihood:                -81046.
# No. Observations:                9879   AIC:                         1.621e+05
# Df Residuals:                    9877   BIC:                         1.621e+05
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const       9202.7812     96.067     95.795      0.000    9014.470    9391.092
# x1             0.5287      0.006     91.218      0.000       0.517       0.540
# ==============================================================================
# Omnibus:                      389.652   Durbin-Watson:                   1.973
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              534.705
# Skew:                          -0.403   Prob(JB):                    7.77e-117
# Kurtosis:                       3.807   Cond. No.                     1.79e+05
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [2] The condition number is large, 1.79e+05. This might indicate that there are
# strong multicollinearity or other numerical problems.
# [5.38354845e-01 9.08477510e+03]
 
# 0.5384 x + 9085
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.448
# Model:                            OLS   Adj. R-squared:                  0.448
# Method:                 Least Squares   F-statistic:                     8030.
# Date:                Thu, 19 Oct 2023   Prob (F-statistic):               0.00
# Time:                        17:49:19   Log-Likelihood:                -81109.
# No. Observations:                9879   AIC:                         1.622e+05
# Df Residuals:                    9877   BIC:                         1.622e+05
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const       9084.7751     99.466     91.335      0.000    8889.801    9279.749
# x1             0.5384      0.006     89.610      0.000       0.527       0.550
# ==============================================================================
# Omnibus:                      346.245   Durbin-Watson:                   1.983
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              430.825
# Skew:                          -0.403   Prob(JB):                     2.80e-94
# Kurtosis:                       3.629   Cond. No.                     1.84e+05
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [2] The condition number is large, 1.84e+05. This might indicate that there are
# strong multicollinearity or other numerical problems.
# [-0.36984419 52.79675589]
 
# -0.3698 x + 52.8
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.013
# Model:                            OLS   Adj. R-squared:                  0.013
# Method:                 Least Squares   F-statistic:                     126.6
# Date:                Thu, 19 Oct 2023   Prob (F-statistic):           3.38e-29
# Time:                        17:49:19   Log-Likelihood:                -36601.
# No. Observations:                9879   AIC:                         7.321e+04
# Df Residuals:                    9877   BIC:                         7.322e+04
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const         52.7968      0.226    233.551      0.000      52.354      53.240
# x1            -0.3698      0.033    -11.253      0.000      -0.434      -0.305
# ==============================================================================
# Omnibus:                       78.653   Durbin-Watson:                   2.013
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              103.710
# Skew:                           0.120   Prob(JB):                     3.02e-23
# Kurtosis:                       3.441   Cond. No.                         16.0
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [-0.36984419 52.79675589]
 
# -0.3698 x + 52.8
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.013
# Model:                            OLS   Adj. R-squared:                  0.013
# Method:                 Least Squares   F-statistic:                     126.6
# Date:                Thu, 19 Oct 2023   Prob (F-statistic):           3.38e-29
# Time:                        17:49:19   Log-Likelihood:                -36601.
# No. Observations:                9879   AIC:                         7.321e+04
# Df Residuals:                    9877   BIC:                         7.322e+04
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const         52.7968      0.226    233.551      0.000      52.354      53.240
# x1            -0.3698      0.033    -11.253      0.000      -0.434      -0.305
# ==============================================================================
# Omnibus:                       78.653   Durbin-Watson:                   2.013
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              103.710
# Skew:                           0.120   Prob(JB):                     3.02e-23
# Kurtosis:                       3.441   Cond. No.                         16.0
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [-1.60436081e-02  2.23867586e+01]
 
# -0.01604 x + 22.39
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.000
# Model:                            OLS   Adj. R-squared:                 -0.000
# Method:                 Least Squares   F-statistic:                   0.06740
# Date:                Thu, 19 Oct 2023   Prob (F-statistic):              0.795
# Time:                        17:49:19   Log-Likelihood:                -42582.
# No. Observations:                9879   AIC:                         8.517e+04
# Df Residuals:                    9877   BIC:                         8.518e+04
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const         22.3868      0.420     53.250      0.000      21.563      23.211
# x1            -0.0160      0.062     -0.260      0.795      -0.137       0.105
# ==============================================================================
# Omnibus:                     8523.970   Durbin-Watson:                   1.993
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):           254381.096
# Skew:                           4.137   Prob(JB):                         0.00
# Kurtosis:                      26.442   Cond. No.                         16.1
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [-0.20988432 23.66586119]
 
# -0.2099 x + 23.67
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.001
# Model:                            OLS   Adj. R-squared:                  0.001
# Method:                 Least Squares   F-statistic:                     11.59
# Date:                Thu, 19 Oct 2023   Prob (F-statistic):           0.000665
# Time:                        17:49:19   Log-Likelihood:                -42813.
# No. Observations:                9879   AIC:                         8.563e+04
# Df Residuals:                    9877   BIC:                         8.564e+04
# Df Model:                           1
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const         23.6659      0.424     55.818      0.000      22.835      24.497
# x1            -0.2099      0.062     -3.405      0.001      -0.331      -0.089
# ==============================================================================
# Omnibus:                     9304.399   Durbin-Watson:                   2.009
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):           422210.224
# Skew:                           4.576   Prob(JB):                         0.00
# Kurtosis:                      33.692   Cond. No.                         16.0
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.