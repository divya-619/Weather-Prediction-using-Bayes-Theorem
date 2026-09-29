# Weather Prediction using Bayes' Theorem

This program predicts the weather when the sky is **Cloudy** using Bayes' Theorem.

The dataset contains 20 days:

* Rain = 8 days 
* Not Rain = 12 days

Among the rainy days, 7 were cloudy. Among the non-rainy days, 3 were cloudy.

The program first calculates the prior and conditional probabilities. Then, Bayes' Theorem is used to find **P(Rain | Cloudy)** and **P(Not Rain | Cloudy)**.

Finally, the two probabilities are compared. The weather condition with the higher probability is selected as the prediction.

For this dataset:

* P(Rain | Cloudy) = 0.70
* P(Not Rain | Cloudy) = 0.30
* **Predicted Weather = Rain**
