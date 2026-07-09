import torch

# This checks if your graphics card (GPU) is detected by PyTorch
is_cuda = torch.cuda.is_available()
print(f"CUDA Available: {is_cuda}")

if is_cuda:
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
else:
    print("WARNING: CUDA not found. Training will use your CPU (this will be very slow).")