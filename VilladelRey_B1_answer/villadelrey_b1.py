# -*- coding: utf-8 -*-
"""villadelrey_b1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-qpdg6b8cD8FzWlRsFCmWRay-iCZbLQ1
"""

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Exam/Exam_Table.csv', skip_blank_lines=True).dropna()

pd.DataFrame(df).to_csv('/content/drive/MyDrive/Colab Notebooks/Exam/b1_output1.csv')