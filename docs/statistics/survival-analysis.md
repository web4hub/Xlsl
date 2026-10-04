# Kaplan-Meier and Log-Log Confidence Intervals

At event time t:

S(t) = product over event times <= t of (1 - d_t / n_t)

where n_t is the risk set immediately before t and d_t is the event count.

Greenwood variance:

Var[S(t)] = S(t)^2 * sum d_t / (n_t (n_t - d_t))

For 0 < S < 1 and positive standard error, a log-log confidence interval can be represented by:

W = exp(z * se / (S * log(S)))
lower = S^(1/W)
upper = S^W

Boundary cases should be handled explicitly rather than producing invalid floating-point values.
