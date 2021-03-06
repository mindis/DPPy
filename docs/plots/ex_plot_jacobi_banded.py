from dppy.beta_ensembles import JacobiEnsemble

jacobi = JacobiEnsemble(beta=3.14) # beta can be >0, default beta=2
# Reference measure is Beta(a,b)
jacobi.sample_banded_model(a=500, b=300, size_N=400)
# jacobi.plot(normalization=True)
jacobi.hist(normalization=True)