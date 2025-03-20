import numpy as np

# SOURCE: https://arxiv.org/pdf/2210.10352
def mof_score(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("The lengths of y_true and y_pred must be the same.")
    
    if len(y_true) == 0:
        return 0.0

    return np.mean(np.array(y_true) == np.array(y_pred))