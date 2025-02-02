from keras import backend as K
def mean_squared_error(y_true,y_pred):
    return K.mean(K.square(y_pred-y_true))
def root_mean_square_error(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)**0.5
def rmse(y_true,y_pred):
    return mean_squared_error(y_true, y_pred)**0.5
mse = MSE = mean_squared_error
def masked_mean_squared_error(y_true, y_pred):
    idx = (y_true>1e-6).nonzero()
    return K.mean(K.square((y_pred[idx]-y_true[idx])))
def masked_rmse(y_true,y_pred):
    return masked_mean_squared_error(y_true, y_pred)**0.5
