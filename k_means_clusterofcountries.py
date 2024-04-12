#This code is used to cluster the countires based on the Lockdown methods and the case data sets

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Attributes
    # Country : Name of the specific Country
    # Government Response : Inlcudes how the government responded to the situation
    # Lockdown Severity : Level of Lockdown
    # Cases per 1000 people: Provides a fair comparison as per the population for each country
    # Recovery Percentage : Patient recovered from number of cases as a percentage
    # Death Percentage : Death of patiend from number of cases as a percentage
    # Puclic Compilance : Response from the public and Co-operation
    # Policy Change over Time : Different lockdown methods of each country
data = {
    'Country': ['China', 'New Zealand', 'Japan', 'USA', 'Argentina', 'South Africa', 'Denmark', 'Colombia', 'Switzerland', 'Sweden', 'Canada'],
    'Government_Response': ['Strict', 'Elimination Strategy', 'Mitigation', 'Mitigation', 'Elimination Strategy', 'Flatten the Curve', 'Mitigation', 'Mitigation', 'Soft Lockdown', 'Voluntary Measures', 'Mitigation'],
    'Lockdown_Severity': ['High', 'Severe', 'Moderate', 'Moderate', 'Severe', 'Severe', 'High', 'Moderate', 'Low', 'Low', 'Moderate'],
    'Cases per 1000 people' : ['0', '0', '1', '29', '26.65', '13', '9', '23', '22', '13', '7'],
    'Recovery Percentage' : ['94', '95', '90', '39', '84', '90', '73', '90', '45', '54', '83'],
    'Death Percentage' : ['5', '1', '2', '2', '3', '3', '1', '3', '1', '4', '4'],
    'Public_Compliance': ['High compliance', 'High compliance', 'High compliance', 'Variable compliance', 'High compliance', 'Variable compliance', 'High compliance', 'Variable compliance', 'High compliance', 'High compliance', 'Variable compliance'],
    'Policy_Changes_Over_Time': ['Implemented vaccine research, quick containment', 'Severe lockdown initially, digital technology for contact tracing', 'Mild lockdown, 3C Plus approach', 'Varied lockdown measures, significant economic impact', 'Extended strict lockdown, penalties for violations', 'Gradual relaxation of lockdown measures, balancing lives and livelihoods', 'Early and decisive action, balance between health measures and economic activity', 'Strict lockdown initially, targeted interventions', 'Gradual easing of restrictions, "soft" lockdown measures', 'Reliance on voluntary behavioral changes, no strict lockdown measures', 'Varied lockdown measures, significant economic impact']
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical variables
df_encoded = pd.get_dummies(df.drop(columns=['Country']))

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_encoded)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# View the clustered data
print(df[['Country', 'Cluster']])

