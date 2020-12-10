# ns-covid-model
 A Control Systems overview of the COVID-19 Response of the Nova Scotian Government

# Prediction Results
## Iteration 0 - 2020-12-09
- We want to predict the number of active cases and the number of new cases expected
- We only have 2 data points for the number of active cases, which is at day 0 (=0) and at today (=71)
- To find the correct weights, I made simple guesses to correct my average to approach closer to 71.
 - For example, with my first set of prediction models for recovery, the simulations consistently ended with a predicted number of active cases closer to 50, so I tweaked the values to weight the predictions more heavier in the 7-12 day range, like the CDC recommends, which corrected the error.

- With this iteration, we predict 6 new cases tomorrow and 70 active cases in total

## Iteration 1 - 2020-12-10
- Yesterday we predicted 6 new cases for a total of 70 active cases. The actual value was 4 new cases for a total of 64 active cases

|               | New Cases     | Active Cases  |
| ------------- |:-------------:| -------------:|
| Predicted     |          6    |       70      |
| Actual        |          4    |       64      |
| Error         |         -2    |       -6      |
| Relative Error|         33%   |        8%     |
