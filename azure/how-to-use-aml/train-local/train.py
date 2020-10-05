from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from azureml.core.run import Run
import joblib
import os
import numpy as np
import numpy as np

os.makedirs('./outputs', exist_ok=True)

X, y = load_diabetes(return_X_y = True)

run = Run.get_context()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=.2, 
    random_state=0
)

data ={
    'train': {
        'X': X_train,
        'y': y_train
    },
    'test': {
        'X': X_test,
        'y': y_test
    }
}

# list of numbers from 0 to 1 with 0.05 intervals
alphas = np.arange(0.0, 1.0, 0.05)

# for each alpha value
for alpha in alphas:
    # instantiate model
    reg = Ridge(alpha=alpha)
    # fit our data
    reg.fit(data['train']['X'], data['train']['y'])
    # create predictions
    predictions = reg.predict(data['test']['X'])
    
    # work out error
    mse = mean_squared_error(predictions, data['test']['y'])
    # log alpha used & error
    run.log('alpha', alpha)
    run.log('mse', mse)

    os.makedirs('outputs', exist_ok=True)
    model_file_name = 'ridge_{0:.2f}.pkl'.format(alpha)
    joblib.dump(value=reg, filename=os.path.join('outputs/',model_file_name))

    print('alpha is {0:.2f}, and mse is {1:0.2f}'.format(alpha, mse))