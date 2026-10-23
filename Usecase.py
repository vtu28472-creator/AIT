import numpy as np
import tensorflow as tf

# Input values for AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output values
y = np.array([0, 0, 0, 1])

# Create a simple neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(
        4, activation='relu', input_shape=(2,)
    ),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X, y, verbose=0)

# Predict outputs
predictions = model.predict(X, verbose=0)

print("AND Gate Results:")
for i in range(len(X)):
    output = 1 if predictions[i][0] >= 0.5 else 0
    print(X[i], "->", output)

print("Accuracy:", accuracy * 100, "%")
