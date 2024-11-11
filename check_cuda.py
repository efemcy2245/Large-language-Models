import torch

print("PyTorch Version:", torch.__version__)            # Check the version of PyTorch
print("CUDA Available:", torch.cuda.is_available())      # Should return True if CUDA is available
print("CUDA Version:", torch.version.cuda)               # Check the version of CUDA PyTorch is using
