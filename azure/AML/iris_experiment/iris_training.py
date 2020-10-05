from azureml.core import Run
import pandas as pd
import os

# Get run context
run = Run.get_context()


# load data
boston_df = pd.DataFrame(load_boston().data, columns = load_boston().feature_names)

# count rows 
boston_df_rowcount = (len(boston_df))
print(f'Analysing {boston_df_rowcount} rows.')

# log results
run.log('Observations', boston_df_rowcount)

# log average age of homeowners
avg_age = boston_df['AGE'].mean()
run.log('Average Age', avg_age)

# save a sample of the data in the outputs folder
# this folder gets uploaded automatically!
os.makedirs('outputs', exist_ok=True)
boston_df.sample(100).to_csv('outputs/sample.csv', index=False, header=True)

# complete run
run.complete()
