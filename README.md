# ns-covid-model
A Control Systems overview of the COVID-19 Response of the Nova Scotian Government
 
## Abstract
I am amazed by the response of the Nova Scotian government in handling the COVID-19 pandemic. Earlier this month we had a peak of 31 cases to which the government quickly responded and tightened restrictions. This response was like an effective control system, so I decided to try and model it like one.

The data scope for this project is from Nova Scotia's second wave, which is a period I've defined as from November 19th onward. Attached is a graph over this period, from CBC.


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
 - I now have 2 data points to test the active case prediction on, on Day #20 we had 71 active cases and on Day #21 we had 64
  - On first run, the algorithm predicts 81 and 68, respectively, which are both too high, so we lower the parameters
  - On 2nd iteration: Prediction = (68, 61), Both too low
  - On 3rd iteration: Prediction = (72, 64), About perfect
  
- We got as close as possible, now let's find the error range.
- We run the experiment 10 times and get data in the form (ActiveCases on day #20, ActiveCases on day #21): [(70, 61), (69, 65), (65, 61), (72, 63), (74, 64), (68, 57), (67, 60), (68, 60), (71, 63), (67, 59)]
 - Getting the error for these values = [(-1, -3), (-2, +1), (-6, -3), (+1, -1), (+3, 0), (-3, -7), (-4, -4), (-3, -4), (0, -1), (-4, -5)]
- We have a mean error of ( -1.9 , -2.8 ), we should repeat this process to reiterate on the algorithm
- The above steps were redone on paper to acheive an algorithm with a mean error of = ( -0.2 , -0.6 )

Running the algorithm one final time, we get:

|        |       New Cases        |       Active Cases            |
| ------ |:----------------------:| -----------------------------:|
|Day #19 |       7 reported       |       Active Cases: 77        |
|Day #20 |       6 reported       |       Active Cases: 72        |
|Day #21 |       4 reported       |       Active Cases: 64        |
|Day #22 |       2 reported       |       Active Cases: 56        |
|Day #23 |       3 reported       |       Active Cases: 50        |
|Day #24 |       2 reported       |       Active Cases: 40        |
|Day #25 |       4 reported       |       Active Cases: 35        |
|Day #26 |       1 reported       |       Active Cases: 34        |
|Day #27 |       7 reported       |       Active Cases: 36        | 
|Day #28 |       1 reported       |       Active Cases: 33        |
|Day #29 |       6 reported       |       Active Cases: 29        |
|Day #30 |       5 reported       |       Active Cases: 30        |
|Day #31 |       3 reported       |       Active Cases: 27        | 

Here, our algoritm predicts the cases for Day #20 within 1 correct value of the actual result and predicts Day #21 perfectly. 

- Given our mean error, we make the following predictions
### Predictions
|             |        New Cases             |             Active Cases         |
| ----------- | ---------------------------- | -------------------------------- |
| Day #22     |  Likely 3, in range(1,6)     |  Likely 56, in range(49, 62)     |

 
