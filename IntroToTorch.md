# My Walkthrough

First I entered the imports:

```
import torch
import torch.nn as nn
```

Not too surprisingly it came up as unfound, need to install likely with pip. The PyTorch website has a great link:

https://pytorch.org/get-started/locally/

I just need to run this in my terminal:

```
pip3 install torch torchvision

Installing collected packages: mpmath, sympy, pillow, numpy, networkx, fsspec, filelock, torch, torchvision
Successfully installed filelock-3.16.1 fsspec-2025.3.0 mpmath-1.3.0 networkx-3.1 numpy-1.24.4 pillow-10.4.0 sympy-1.13.3 torch-2.2.2 torchvision-0.17.2
```

We are set to keep going. But, of course, new problem occurs. :D

```
ModuleNotFoundError: No module named 'torch'
```

Very annoying and I barely understand what exactly fixed, but either my python setup is extremely cooked. Or it just needed a moment to properly start working (two things can be true at once). Somehow, doing the install in a notebook caused both to start working...but we'll explore the exact reason when I factory reset this computer and never see OS X or windows ever again.

Now we can move forward.

## List of important functions and data types in Pytorch:

#### Tensor
```
a = torch.ones(5,5)
```