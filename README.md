# ns-covid-model
A Control Systems overview of the COVID-19 Response of the Nova Scotian Government
 
## Abstract
I am amazed by the response of the Nova Scotian government in handling the COVID-19 pandemic. Earlier this month we had a peak of 31 cases to which the government quickly responded and tightened restrictions. This response was like an effective control system, so I decided to try and model it like one.

The data scope for this project is from Nova Scotia's second wave, which is a period I've defined as from November 19th onward. Attached is a graph over this period, from CBC.
![alt text](https://github.com/RohitKochhar/ns-covid-model/blob/main/imgs/cbcGraph.png?raw=true)

This graph contains all the datapoints used in this experiment:

`a_InputData         = [1, 5, 8, 11, 11, 37, 16, 14, 9, 14, 10, 15, 10, 17, 11, 15, 6, 4, 8, 7,  6,  4]`

a_Input data is an array where each entry is the amount of cases that day. So on the first day we have 1, on the second we have 5, and so on.

**Using this data, my model is able to predict how COVID will spread in the community up to a week in advance.**

I get the number of active cases from my MLA's Official Government FaceBook page. I use these values to validate my own model to make sure I can successfully predict days which I have the data for. By doing this, every day my model becomes better at predicting the number of active cases.

`a_ActualActiveCases = [0, 0, 0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  0,  0,  0,  0, 0, 0, 0, 0, 71, 64]`

## Model Design
The idea to program this as a control system came to me when I considered how restrictions are the input to a control system that determines how we spread the coronavirus. I defined 3 zones of restrictions:

`Restriction zones = RED, ORANGE, YELLOW`

Here, I made my own estimate for what should be the deciding factor in what zone we are in. I decided that we could choose the zone based on the number of active cases we currently have. 
- If we have over 100 active cases, we are in the RED zone.
 - In the RED zone, let's say restaurants are closed, essential travel only, small gathering limits.
- If we have between 100 and 50 cases, we are in the ORANGE zone.
 - In the ORANGE zone, restaurants are open, but gyms and other high risk areas are closed, medium gathering limits.
- If we have between than 50 and 0 cases, we are in the YELLOW zone.

Then, depending on the zone we are in, I made some guesses on how the virus would spread.
- If we are in the RED zone, for each active case, we have a 5% chance of a new infection **ten days later** to accomodate for the incubation period of the virus.
- If we are in the ORANGE zone, for each active case, we have a 7.5% chance of a new infection **ten days later** to accomodate for the incubation period of the virus
- If we are in the YELLOW zone, for each active case, we have a 15% chance of a new infection **ten days later** to accomodate for the incubation period of the virus

This is how we make new cases, but we also have to remove people who have recovered from the virus. For this, I created my own-piecewise function to take a random function and return how long it will take for an infection to recover. It is distributed as follows

| Infection will recover in : |  2 days  |  3 days  | 4 days | 5 days | 6 days | 7 days | 8 days | 9 days | 10 days | 11 days |
| --------------------------- | -------- | -------- | ------ | ------ | ------ | ------ | ------ | ------ | ------- | --------|
|                             |    1%    |    3%    |   4%   |   4%   |   10%  |   13%  |   15%  |  20%   |    20%  |    10%  | 


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

 
