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

This data suggests a few things:
- We are predicting higher for both active cases and new cases.
 - The first correction is that we need to reduce the probability of spread in the ORANGE zone, which is currently set to 10%. This could suggest that as restrictions are right now, for every active case we currently have we are <10% likely to develop a new case the next day. Of course this assumes the virus has no incubation period, which we of course know to be false. This will be our next correction.  We reduce the probability of spread in the ORANGE zone to 7.5%
 - The next correction is to assume that it takes 10 days for restrictions to take place. This means now today's zone doesn't affect new cases, but the zone 10 days ago does. This was adjusted by changes to the implementation of the setTransmission method for the Day class
 - I also know that there is an issue with how we remove active cases and the active cases count doesn't make sense for some predictions, this took a while to fix but now the code is bug free (as far as I know)
 
