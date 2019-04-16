import time
import numpy as np
import pandas as pd
from scipy.optimize import least_squares

def nonlinear_fit(data_array, model, p0, dim_fit='echo', p_bound=(0, np.inf), p_names=None):
    """ Perform nonlinear least squares along a selected axis of an xr.DataArray 

    The array is transformed to pandas DataFrame and grouped by all but ``dim_fit`` axis for
    ``scipy.optimize.least_squares`` to apply with non-negativity bounds
    
    Parameters
    ----------
    data_array : xr.DataArray
        N-D array to perform fit on
    model : callable 
        Function representing the fitted model, with the signature ``model(p, x)``, 
        with ``p`` being an array of parameters to fit, and ``x`` being an ndarray of shape (n,) 
    p0 : array_like with shape (n,) or float
        Initial guess on the model parameters
    dim_fit : str, optional
        Name of the dimension to perform the fit. Must be present in ``data_array.dims``
    p_bound: 2-tuple of array_like, optional
        Lower and upper bounds on independent variables. Each array must match the size of p0 
        or be a scalar, in the latter case a bound will be the same for all variables. 
        Use np.inf with an appropriate sign to disable bounds on all or some variables.
        Defaults to 0 as the lower and ``np.inf`` as the upper bound. 
    p_names : array_like of str, optional
        Names of the parameters to fit. Used as array names in the returned xr.Dataset. 
        Must match the size of p0. Defaults to 'p0', 'p1', etc.
    
    Returns
    ----------
    ds_fit : xr.Dataset
        Dataset with fitted parameters as variables
    dtime : float
        Time needed to perform the fitting. Captured and returned for illustrative purposes
    """  
    def resid(p, x, y):
        return model(p, x) - y
    if p_names is None:
        p_names = [f'p{idx}' for idx in range(len(p0))]
    else:
        assert len(p0) == len(p_names), 'len(p_names) must match len(p0)'

    df = data_array.to_dataframe().dropna()
    dim_intact = [d for d in data_array.dims if d!=dim_fit]
    df_grouped = df.groupby(dim_intact)
    
    # Prepare a function closure performing fitting
    x = data_array.coords[dim_fit].data
    def fun(y):
        return least_squares(resid, p0, loss='soft_l1', f_scale=0.1,
                             args=(x, y), bounds=p_bound)
    # The fit itself
    start = time.process_time()
    df_fit = df_grouped[data_array.name].apply(fun)
    end = time.process_time()
    df_fit = df_fit.to_frame()
    
    df_fit.index.set_names(level=-1, names='fit', inplace=True)
    df_fit = df_fit.xs('x', level=-1)
    df_fit = pd.DataFrame(np.stack(df_fit.values.tolist()).squeeze(), columns=p_names, index=df_fit.index)
    return df_fit.to_xarray(), end - start