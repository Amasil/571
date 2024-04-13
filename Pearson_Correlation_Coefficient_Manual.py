import numpy as np

# Data for 2019
dci_scores_2019 = [56.044, 90.836, 84.292, 56.126, 95.225, 82.775, 86.026, 60.865, 96.070, 94.648, 100.000]
sdi_scores_2019 = [72.4, 77.9, 73.2, 69.6, 85.2, 78.9, 79.5, 61.5, 85.0, 78.8, 74.5]

# Data for 2020
dci_scores_2020 = [48.784, 90.482, 84.105, 46.450, 96.013, 75.099, 77.690, 48.353, 95.146, 93.693, 100.000]
sdi_scores_2020 = [73.2, 78.2, 73.9, 70.9, 84.6, 79.2, 79.2, 63.4, 84.7, 84.7, 76.4]

# Calculate means
dci_scores_mean_2019 = np.mean(dci_scores_2019) # Mean of DCI scores for 2019
sdi_scores_mean_2019 = np.mean(sdi_scores_2019) # Mean of SDI scores for 2019
dci_scores_mean_2020 = np.mean(dci_scores_2020) # Mean of DCI scores for 2020
sdi_scores_mean_2020 = np.mean(sdi_scores_2020) # Mean of SDI scores for 2020

# Calculate Pearson correlation coefficient for 2019
# The numerator calculates the sum of the products of the differences between each data point and the mean for each dataset
# The denominator calculates the product of the square roots of the sums of the squared differences between each data point and its mean for each dataset
numerator_2019 = np.sum((np.array(dci_scores_2019) - dci_scores_mean_2019) * (np.array(sdi_scores_2019) - sdi_scores_mean_2019))
denominator_2019 = np.sqrt(np.sum((np.array(dci_scores_2019) - dci_scores_mean_2019)**2) * np.sum((np.array(sdi_scores_2019) - sdi_scores_mean_2019)**2))
r_2019 = numerator_2019 / denominator_2019

# Calculate Pearson correlation coefficient for 2020
numerator_2020 = np.sum((np.array(dci_scores_2020) - dci_scores_mean_2020) * (np.array(sdi_scores_2020) - sdi_scores_mean_2020))
denominator_2020 = np.sqrt(np.sum((np.array(dci_scores_2020) - dci_scores_mean_2020)**2) * np.sum((np.array(sdi_scores_2020) - sdi_scores_mean_2020)**2))
r_2020 = numerator_2020 / denominator_2020

# Print results
print("Pearson correlation coefficient 2019:", r_2019)
print("Pearson correlation coefficient 2020:", r_2020)