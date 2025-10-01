import pandas as pd
import numpy as np

# Set the desired number of data points
N = 1000
np.random.seed(42) # For reproducibility

# 1. Generate the three distinct clusters (Categorical Data)
cluster_ids = np.random.choice([1, 2, 3], size=N, p=[0.4, 0.35, 0.25])

# 2. Assign properties based on Cluster_ID for visual separation
data = {
    'Index': np.arange(N),
    'Cluster_ID': cluster_ids,
}

df = pd.DataFrame(data)

# Create distinct base radii for the clusters to separate them visually
cluster_base_radius = {1: 80, 2: 40, 3: 120}

# Generate radii with noise
df['Orbital_Radius'] = df['Cluster_ID'].apply(lambda c: cluster_base_radius[c]) + np.random.randn(N) * 5

# Generate the angle for orbital position (0 to 2*pi)
df['Theta'] = np.random.rand(N) * 2 * np.pi

# 3. Calculate 3D Coordinates (The Pretty Orbital Shape)
df['X_Orbit'] = df['Orbital_Radius'] * np.cos(df['Theta'])
df['Y_Orbit'] = df['Orbital_Radius'] * np.sin(df['Theta'])

# Z-Height: Add a small, cluster-dependent Z-dimension for 3D scatter
df['Z_Height'] = (df['Cluster_ID'] * 3) + np.random.randn(N) * 2

# 4. Generate Energy and Noise (Continuous/Size Data)
# Energy will be inversely related to radius (closer to center = higher energy)
df['Energy_Level'] = 100 / df['Orbital_Radius'] + np.random.rand(N) * 0.5
df['Energy_Level'] = df['Energy_Level'].clip(0.1, 5.0) # Clip to a reasonable range

# 5. Finalize the DataFrame and save it
# Drop the temporary 'Theta' column
df = df.drop(columns=['Theta'])

# Save to a CSV file
df.to_csv('orbital_swarm_1000.csv', index=False)

print(f"Successfully generated {N} data points and saved to 'orbital_swarm_1000.csv'")
print("\nFirst 5 rows:")
print(df.head())