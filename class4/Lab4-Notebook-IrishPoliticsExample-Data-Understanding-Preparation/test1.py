import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

if __name__ == "__main__":
    df1 = pd.read_csv('ge16-results-elected.csv')
    df1.head(1)
