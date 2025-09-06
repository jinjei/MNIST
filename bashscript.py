import os
import pathlib

from torchvision.datasets import MNIST

# 用 MNIST 的默认下载路径
root = os.path.expanduser("~/.torch")
mnist_dir = os.path.join(root, "datasets", "MNIST")

def get_dir_size(path):
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total

if __name__ == "__main__":
    print("MNIST should be stored in:", mnist_dir)
    if os.path.exists(mnist_dir):
        size = get_dir_size(mnist_dir) / (1024 * 1024)
        print(f"Total size: {size:.2f} MB")
    else:
        print("MNIST dataset not found locally yet.")
