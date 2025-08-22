import numpy as np

def calculate(list):
    matrix=np.array(list)
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix=matrix.reshape(3,3)
        calculations={}
        #mean
        mean_columns=np.mean(matrix, axis=0).tolist()
        mean_rows=np.mean(matrix, axis=1).tolist()
        mean_flat=np.mean(matrix).tolist()
        calculations["mean"] = [mean_columns, mean_rows,  mean_flat]
        #variance
        variance_columns=np.var(matrix, axis=0).tolist()
        variance_rows=np.var(matrix, axis=1).tolist()
        variance_flat=np.var(matrix).tolist()
        calculations["variance"] = [variance_columns, variance_rows,  variance_flat]

        #standard deviation
        standarddeviation_columns=np.std(matrix, axis=0).tolist()
        standarddeviation_rows=np.std(matrix, axis=1).tolist()
        standarddeviation_flat=np.std(matrix).tolist()
        calculations["standard deviation"] = [standarddeviation_columns, standarddeviation_rows,  standarddeviation_flat]
        #max
        max_columns=np.max(matrix, axis=0).tolist()
        max_rows=np.max(matrix, axis=1).tolist()
        max_flat=np.max(matrix).tolist()
        calculations["max"]= [max_columns, max_rows, max_flat]
        #min
        min_columns=np.min(matrix, axis=0).tolist()
        min_rows=np.min(matrix, axis=1).tolist()
        min_flat=np.min(matrix).tolist()
        calculations["min"]= [min_columns, min_rows, min_flat]
        #sum
        sum_columns=np.sum(matrix, axis=0).tolist()
        sum_rows=np.sum(matrix, axis=1).tolist()
        sum_flat=np.sum(matrix).tolist()
        calculations["sum"]=[sum_columns, sum_rows, sum_flat]
        return calculations