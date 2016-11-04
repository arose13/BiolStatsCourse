import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as graph
from scipy.stats import shapiro, probplot, gamma
from IPython.display import display, Markdown
from statsmodels.formula.api import ols, glm


sns.set(font_scale=1.2)
graph.style.use('fivethirtyeight')
warnings.simplefilter('ignore')