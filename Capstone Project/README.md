
The goal of the project was to build a machine learning model to predict the parameters of the depth and width of the welded joint.

Before building the machine learning model, the data was pre-processed and duplicates were removed.

Then, an exploratory analysis of the data was carried out, in which non-linear correlations between features and targets were revealed, as well as correlations between features. Based on the results of the stage, it was concluded that the targets lend themselves well to forecasting, and also that not all features can be used for successful forecasting.

After that, a machine learning pipeline was built:
- normalization of incoming features;
- reducing the number of input features using the method of principal components;
- feeding prepared features into a machine learning model.

Then, the optimal parameters for the selected models were selected using grid search and cross-validation:
- linear regression;
- SVR;
- KNeighbors;
- Random Forest;
- Gradient Boosting;
- CatBoost.

Also, two neural networks were used for evaluation: a multilayer perceptron and a fully connected neural network with 3 hidden layers.

After that, the models were trained and the quality of their predictions was checked by cross-validation. As a result of the evaluation, a GradientBoosting Regressor model with a MultiOutputRegressor was chosen for subsequent deployment as a Flask application. The values of the coefficient of determination for the selected model: 0.94 for the depth of the joint and 0.95 for the width of the joint. The average quality score for the two metrics on cross-validation was 0.96 on the training dataset and 0.92 on the test dataset.

Link to the Flask APP: https://welding-joint-prediction.onrender.com

Link to the Colab Notebook (in English): https://colab.research.google.com/drive/156264nKYHCpdWsj1zLWJ1OTRZnlNOlrz

