# Two-Sample Log-Rank Reference

For each distinct event time j:

N_j = subjects at risk immediately before the time.
N_1j = group-1 subjects at risk.
O_j = total observed events.
O_1j = group-1 observed events.

Expected group-1 events:

E_1j = N_1j O_j / N_j

Two-group hypergeometric variance:

V_j = N_1j N_2j O_j (N_j - O_j) / (N_j^2 (N_j - 1))

The test statistic is:

chi-square = (O_1 - E_1)^2 / V

The signed statistic is:

Z = (O_1 - E_1) / sqrt(V)

For one degree of freedom:

p = erfc(|Z| / sqrt(2))

The implementation groups exact equal event times and uses risk sets before removing current-time observations.
