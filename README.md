# simple-rands
a very simple tool to generate random string with digits and numbers.

## Install

```bash
pip install simple-rands
```

## Usage

```python
import simple_rands

# optional: set seed for generator
simple_rands.seed(12345)

length = 10
print(simple_rands.gen(length))
```
