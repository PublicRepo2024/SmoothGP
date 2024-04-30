import numpy as np

def ldp_lap_vec(arr_x, func, epsL, mreps, sens):
    y_tilde = [func(x)+np.random.laplace(0,1,size=mreps)*sens/epsL for x in arr_x]
    return y_tilde