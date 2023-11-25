#!/usr/bin/env python
# coding: utf-8

# <center><img src="images/logo.png" alt="drawing" width="400" style="background-color:white; padding:1em;" /></center> <br/>
# 
# # ML through Application
# ## Module 1, Lab 3: Getting Started with AutoGluon
# 
# This notebook covers how to create a model to solve an ML problem by using [AutoGluon](https://auto.gluon.ai/stable/index.html#).
# 
# You will learn how to do the following:
# 
# - Import the AutoGluon library.
# - Import data to a Pandas DataFrame.
# - Train a model by using AutoGluon.
# 
# ---
# 
# You will explore a dataset that contains information about books. The goal is to predict book prices by using features about the books.
# 
# __Business problem:__ Books from a large database with several features cannot be listed for sale because one critical piece of information is missing: the price. 
# 
# __ML problem description:__ Predict book prices by using book features, such as genre, release data, ratings, and number of reviews.
# 
# This is a regression task (the training dataset has a book price column to use for labels).
# 
# ----
# 
# You will be presented with two kinds of exercises throughout the notebook: activities and challenges. <br/>
# 
# | <img style="float: center;" src="images/activity.png" alt="Activity" width="125"/>| <img style="float: center;" src="images/challenge.png" alt="Challenge" width="125"/>|
# | --- | --- |
# |<p style="text-align:center;">No coding is needed for an activity. You try to understand a concept, <br/>answer questions, or run a code cell.</p> |<p style="text-align:center;">Challenges are where you can practice your coding skills.</p>

# ## Index
# - [Importing AutoGluon](#Importing-AutoGluon)
# - [Getting the data](#Getting-the-data)
# - [Model training with AutoGluon](#Model-training-with-AutoGluon)

# ---
# ## Importing AutoGluon
# 
# Install and load the libraries that are needed to work with the tabular dataset.

# In[2]:


get_ipython().run_cell_magic('capture', '', '# Use pip to install libraries\n!pip install -U -q -r requirements.txt\n')


# In[3]:


# Import the libraries that are needed for the notebook
get_ipython().run_line_magic('load_ext', 'autoreload')
import pandas as pd
# Import utility functions and challenge questions
from MLUMLA_EN_M1_Lab3_quiz_questions import *

# Import the newly installed AutoGluon code library
from autogluon.tabular import TabularPredictor, TabularDataset


# ---
# ## Getting the data
# 
# Now get the data for the business problem. 
# 
# __Note:__ You will use the [Amazon Product Reviews](https://cseweb.ucsd.edu/~jmcauley/datasets.html#amazon_reviews) dataset. For more information about this dataset, see the following resources:
# 
# - Ruining He and Julian McAuley. "Ups and Downs: Modeling the Visual Evolution of Fashion Trends with One-Class Collaborative Filtering." Proceedings of the 25th International Conference on World Wide Web, Geneva, Switzerland, April 2016. https://doi.org/10.1145/2872427.2883037.
# 
# - Julian McAuley, Christopher Targett, Qinfeng Shi, Anton van den Hengel. "Image-Based Recommendations on Styles and Substitutes." Proceedings of the 38th International Association for Computing Machinery (ACM) Special Interest Group on Information Retrieval (SIGIR) Conference on Research and Development in Information Retrieval, Santiago, Chile, August 2015. https://doi.org/10.1145/2766462.2767755.

# To load the training and test data, and then show the first few rows of the training dataset, run the following cells.

# In[4]:


df_train = TabularDataset(data="data/train.csv")
df_test = TabularDataset(data="data/test.csv")


# In[5]:


df_train.head()


# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>It's time to check your knowledge!</i></h3>
#     <br>
#     <p style=" text-align: center; margin: auto;">To load the question, run the following cell.</p>
#     <br>
# </div> 

# In[6]:


# Run this cell for a knowledge check question
question_1


# ---
# ## Model training with AutoGluon
# 
# You can use AutoGluon to train a model by using a single line of code. You need to provide the dataset and tell AutoGluon which column from the dataset you are trying to predict.

# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>Try it yourself!</i></h3>
#     <br>
#     <p style="text-align:center;margin:auto;"><img src="images/activity.png" alt="Activity" width="100" /> </p>
#     <p style=" text-align: center; margin: auto;">To prepare the datasets, run the following cell.<br/>
#         This step is not required for AutoGluon to work, but it will reduce the time to train your first model.<br/>
# The code randomly selects 1,000 rows from the dataset and splits them into training and validation datasets.</p>
#     <br>
# </div>

# In[7]:


# Sampling 1,000
# Try setting the subsample_size to a much larger value to see what happens during training
subsample_size = 1000  # Sample a subset of the data for faster demo
df_train_smaller = df_train.sample(n=subsample_size, random_state=0)

# Print the first few rows
df_train_smaller.head()


# In[13]:


subsample_size = 100  
df_train_smaller = df_train.sample(n=subsample_size, random_state=2)

df_train_smaller.head()


# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>It's time to check your knowledge!</i></h3>
#     <br>
#     <p style=" text-align: center; margin: auto;">To load the question, run the following cell.</p>
#     <br>
# </div> 

# In[14]:


# Run this cell for a knowledge check question
question_2


# ### Training a model with a small sample
# 
# AutoGluon uses certain defaults. For example, AutoGluon uses `root_mean_squared_error` as an evaluation metric for regression problems. For more information, see [sklearn.metrics](https://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics) in the sklearn documentation.
# 
# __Note:__ Training on this smaller dataset will take approximately 3–4 minutes.

# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>Try it yourself!</i></h3>
#     <br>
#     <p style="text-align:center;margin:auto;"><img src="images/activity.png" alt="Activity" width="100" /> </p>
#     <p style=" text-align: center; margin: auto;">Use `TabularPredictor` to train the first version of the model along with the smaller 1000 sample training dataset so the model trains faster.<br>
# </p>
#     <br>
# </div>

# In[15]:


# Run this cell

smaller_predictor = TabularPredictor(label="Price", eval_metric = 'mean_squared_error').fit(train_data=df_train_smaller)


# ### Interpreting the training output
# AutoGluon outputs a lot of information about what happens during model training.

# <div style="border: 4px solid coral; text-align: center; margin: auto;"> 
#     <h3><i>Try it yourself!</i></h3>
#     <p style="text-align:center; margin:auto;"><img src="images/challenge.png" alt="Activity" width="100" /> </p>
#     <p style=" text-align: center; margin: auto;">After the training finishes, examine the output and answer the following questions based on the output.</p>
#     <br>
# </div>
# 

# 1. What is the shape of the training dataset?
# 2. What type of ML problem (such as classification or regression) does AutoGluon infer? (**Hint:** Remember, you didn't mention the problem type. You only provided the label column.)
# 3. What does AutoGluon suggest in case it inferred the wrong problem type?
# 4. What kind of data preprocessing and feature engineering did AutoGluon perform?
# 5. What are the basic statistics about the label in the print statements from AutoGluon?
# 6. How many extra features were generated in addition to the originals in the dataset? What was the runtime for that?
# 7. Which evaluation metric was used?
# 8. What does AutoGluon suggest in case it inferred the wrong metric?
# 9. What is the ratio between the training and validation dataset? (**Hint:** Look for `val` or `validation`.)
# 10. Where did AutoGluon save the predictor?
# 11. Which folder were the models saved in?
# 12. What file format are the models in? (**Note:** Look at the file name suffix. You don't need to open the file.)
# 
# Try to answer these questions before you check the solution.

# ### List your answers here:
# 1. 100x10
# 
# 2. Regression
# 
# 3. Manually specify the problem_type parameter during predictor init
# 
# 4. Feature Generators
# 
# 5. max, min, mean, stddev: (316.86, 2.0, 37.5039, 56.16986)
# 
# 6. 121 extra features; 1.64 seconds
# 
# 7. mean_squared_error
# 
# 8. specify the eval_metric parameter of Predictor()
# 
# 
# 9. 0.2
# 
# 10. AutogluonModels/ag-20231125_041132
# 
# 11. AutogluonModels
# 
# 12. ag
# 

# 

# ----
# ## Conclusion
# 
# The purpose of this notebook was to explore a dataset of information about books and to use AutoGluon to build a basic model to predict book prices based on book features.
# 
# ## Next lab
# In the next lab, you will learn how to use AutoGluon features to refine your model.
