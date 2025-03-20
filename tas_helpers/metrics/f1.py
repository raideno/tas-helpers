from sklearn.metrics import f1_score as sk_f1_score

def f1_score(y_true, y_pred):
    return sk_f1_score(y_true, y_pred, average='weighted')