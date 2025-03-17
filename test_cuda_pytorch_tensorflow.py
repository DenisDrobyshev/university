import tensorflow as tf
from tensorflow.config.experimental import get_device_details
from tensorflow.python.client import device_lib
import torch
from torch import cuda

if __name__ == "__main__":
    gpu_devices = tf.config.list_physical_devices("GPU")
    gpu_details = [get_device_details(gpu) for gpu in gpu_devices]

    print(f"\nTensorFlow build supports GPU: {tf.test.is_built_with_gpu_support()}")
    print(f"TensorFlow build supports XLA: {tf.test.is_built_with_xla()}")
    is_built_with_cuda = tf.test.is_built_with_cuda()
    print(f"TensorFlow build supports CUDA: {is_built_with_cuda}")

    if is_built_with_cuda:
        build_info = tf.sysconfig.get_build_info()
        print(f"TensorFlow build CUDA version: {build_info['cuda_version']}")
        print(f"TensorFlow build cuDNN version: {build_info['cudnn_version']}")

    print(f"\nNumber of GPUs found on system: {len(gpu_devices)}")
    for device, details in zip(gpu_devices, gpu_details):
        print(f"\nGPU: {device.name}")
        print(f"GPU index: {device.name.split(':')[-1]}")
        print(f"GPU name: {details['device_name']}")

    if torch.backends.cuda.is_built():
        print(f"PyTorch build CUDA version: {torch.version.cuda}")
        print(f"PyTorch build cuDNN version: {torch.backends.cudnn.version()}")
        print(f"PyTorch build NCCL version: {torch.cuda.nccl.version()}")

        print(f"\nNumber of GPUs found on system: {cuda.device_count()}")

    if cuda.is_available():
        print(f"\nActive GPU index: {cuda.current_device()}")
        print(f"Active GPU name: {cuda.get_device_name(cuda.current_device())}")
    elif torch.backends.mps.is_available():
        mps_device = torch.device("mps")
        print(f"PyTorch has active GPU: {mps_device}")
    else:
        print(f"PyTorch has no active GPU")