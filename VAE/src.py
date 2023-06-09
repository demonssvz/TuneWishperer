

# Normalize and reshape the musical sequences
normalized_sequences = (music_sequences - np.min(music_sequences)) / (np.max(music_sequences) - np.min(music_sequences))
reshaped_sequences = normalized_sequences.reshape(len(normalized_sequences), -1)

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam

latent_dim = 16

# Define the VAE architecture
input_shape = reshaped_sequences.shape[1]
inputs = Input(shape=(input_shape,))
encoded = Dense(64, activation='relu')(inputs)
z = Dense(latent_dim, activation='relu')(encoded)
decoded = Dense(64, activation='relu')(z)
outputs = Dense(input_shape, activation='sigmoid')(decoded)

# Build the VAE model
vae = Model(inputs, outputs)

# Define the loss function and optimizer
loss = MeanSquaredError()
optimizer = Adam()

# Compile the model
vae.compile(optimizer=optimizer, loss=loss)

# Train the VAE
vae.fit(reshaped_sequences, reshaped_sequences, epochs=10, batch_size=32)
# Generate original music sequences from random latent vectors
num_sequences = 5
random_latent_vectors = np.random.normal(size=(num_sequences, latent_dim))
generated_sequences = vae.decoder.predict(random_latent_vectors)

# Reshape and denormalize the generated sequences
generated_sequences = generated_sequences.reshape(num_sequences, *normalized_sequences.shape[1:])
generated_sequences = generated_sequences * (np.max(music_sequences) - np.min(music_sequences)) + np.min(music_sequences)
