import torch

t = torch.Tensor([[[1,2],
                  [3,4]],
                  [[5,6],
                   [7,8]]])

print(t.shape)
t.flatten()
print(t)
