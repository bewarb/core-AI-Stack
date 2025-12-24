import torch
import torch.nn as nn

#This is a tensor

a = torch.ones(5,5)
print(a)

# Sum() and Mean() functions

#Sum of the matrix
sum1 = torch.sum(a)
#Sum of each column
sum2 = torch.sum(a, axis=1)
#sum of each row
sum3 = torch.sum(a, axis=0)

print(sum3)

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.first_layer = nn.Linear(4,6) # Linear layer with 4 inputs and 6 outputs
        self.second_layer = nn.Linear(6,6) # Linear layer with 6 inputs and 6 output
        self.final_layer = nn.Linear(6,2) # Linear layer with 6 inputs and 2 output

    def forward(self, x):
        return self.final_layer(self.second_layer(self.first_layer(x)))
    
model = MyModel()

input_data = torch.randn(1,4) # Random input tensor with batch size 3 and 4 features

model_output = model(input_data)

print(model_output)

# This does not matter as this model is not trained yet.
