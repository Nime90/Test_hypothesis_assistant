#OrderedLogisticRegression
def OrderedLogisticRegression (data, dep_var, ind_var):
        import pandas as pd
        from statsmodels.miscmodels.ordinal_model import OrderedModel

        mod_prob = OrderedModel(data[str(dep_var)], data[ind_var], distr='logit')
        res_log = mod_prob.fit(method='bfgs')
        results = res_log.summary()
        
        return results.to_string()