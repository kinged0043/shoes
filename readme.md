MLOPs practice
---

This is my personal project for the month of july, the shoe sales csv files were generated from chatgpt using the prompts:
- generate a csv file containing 10 years worth of records for a shoe sales shop
- include the target gender and the gender that actually bought the shoe, then make a dirty version of the csv file

> NB:  while using the free version of chatgpt the you can only generate the clean version of the data, you'll have to wait for thr next day to generate the dirty version. so choose which one you want first before generating the data

there are two of the datasets
- one clean(delve straight into the work) 
- one dirty(for the purpose of practice)


process
***
- [x] initialize all neccesary tools
- [x] import and clean data with pandas
- [x] save dataset with dvc
- [ ] extract features with sklearn
- [ ] save extracted features using feast
- [ ] perform some statistical analysis and plots with pandas and plotly
- [ ] train model using shallow algorithm
- [ ] track and register model with mlflow 
- [ ] create dvc pipeline for running workflow
- [ ] build docker file for reproducability

![shoe plan](imgs/shoe_plan.png)


tools
***

1. pandas and plotly:
    - cleaning and converting dirty data into clean data
    - export the data as csv and parquet to the respective folders 
    - **create plots where you need to

1. lazypredict:
    - getting the best model for training in the modelling.ipynb script

1. scikit-learn:
    - extracting features from the data set and storing it as features in the feature_repo/data
    - model training from listed models in lazypredict section of the modelling.ipynb
    - model hyperparameter tunning to ascertain best metrics for the model

1. dvc:
    - storing the clean data and the feature data
    - staging the pipeline[whatever that means]

1. mlflow:
    - logging model metrics, scores, artifacts and other necessary information
    - registering the useful or well-performing models for future references
    

terminal commands
***
