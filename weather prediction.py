# Dataset
total_days = 20
rain_days = 8
not_rain_days = 12

cloudy_and_rain = 7        
cloudy_and_not_rain = 3    

# Prior probabilities
p_rain = rain_days / total_days
p_not_rain = not_rain_days / total_days

# Conditional probabilities (likelihoods)
p_cloudy_given_rain = cloudy_and_rain / rain_days
p_cloudy_given_not_rain = cloudy_and_not_rain / not_rain_days

p_cloudy = (p_cloudy_given_rain * p_rain) + (p_cloudy_given_not_rain * p_not_rain)

# Bayes' Theorem: P(A|B) = P(B|A) * P(A) / P(B)

p_rain_given_cloudy = (p_cloudy_given_rain * p_rain) / p_cloudy
p_not_rain_given_cloudy = (p_cloudy_given_not_rain * p_not_rain) / p_cloudy

# results
print("Given: Sky = Cloudy")
print("-" * 30)
print(f"P(Rain)                = {p_rain:.2f}")
print(f"P(Not Rain)            = {p_not_rain:.2f}")
print(f"P(Cloudy | Rain)       = {p_cloudy_given_rain:.3f}")
print(f"P(Cloudy | Not Rain)   = {p_cloudy_given_not_rain:.3f}")
print(f"P(Cloudy)              = {p_cloudy:.2f}")
print(f"P(Rain | Cloudy)       = {p_rain_given_cloudy:.2f}")
print(f"P(Not Rain | Cloudy)   = {p_not_rain_given_cloudy:.2f}")
print("-" * 30)

if p_rain_given_cloudy > p_not_rain_given_cloudy:
    print("Predicted Weather = Rain")
else:
    print("Predicted Weather = Not Rain")