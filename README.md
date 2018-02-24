#Image Processing Algorithms

## Introduction

A collection of image processing algorithms in _Python_. 


## Prerequisites

- Python 3+
- OpenCV


## Installation

Simply clone/download this repository.


## Run

1. Choose the algorithm you want to run.
2. Modify the parameters 
3. Simply run and get the result (in Python array)

### Example

Let's say you want to run a template matching algorithm. Simply navigate to [template_matching.py](template_matching.py), create array for image and template:

```python
image = [
    [4, 4, 4],
    [1, 2, 1]
]

template = [
    [1, 2, 1]
]
```

Then choose which type of matching you want:

```python
print('non_normalized_correlation')
print(non_normalized_correlation(template, image))
print()
print('normalized_correlation')
print(normalized_correlation(template, image))
```

And get the results:

```python
non_normalized_correlation
[[ 4 12 16 12  4]
 [ 1  4  6  4  1]]

normalized_correlation
[[1.         2.12132034 2.30940108 2.12132034 1.        ]
 [1.         1.78885438 2.44948974 1.78885438 1.        ]]
```


There are a lot of algorithms and more are still being added. Experiment with them however you like.