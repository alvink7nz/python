import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

# Step 1: Define the neural network architecture
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# Step 2: Prepare the data
# Replace this with your own data loading and preprocessing
# Example with random data:
input_size = 10
output_size = 2
data_size = 1000

X = torch.randn(data_size, input_size)
y = torch.randint(0, output_size, (data_size,))

dataset = TensorDataset(X, y)
train_loader = DataLoader(dataset, batch_size=64, shuffle=True)

# Step 3: Initialize the model, optimizer, and loss function
model = SimpleNN(input_size, hidden_size=64, output_size=output_size)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.NLLLoss()

# Step 4: Train the model
epochs = 10

for epoch in range(epochs):
    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        output = model(batch_X)
        loss = criterion(output, batch_y)
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}')

# Step 5: Make predictions
# Replace this with your own input data for prediction
input_data = torch.randn(1, input_size)
predictions = model(input_data)
predicted_class = torch.argmax(predictions, dim=1).item()

print(f'Predicted Class: {predicted_class}')