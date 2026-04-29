# simple-rands
a very simple tool to generate random string with digits and numbers.

## Install

```bash
pip install simple-rands
```

## Usage

```python
import simple_rands
import string

# optional: set seed for generator
simple_rands.seed(12345)

# generate a random string with uppercase letter, lowercase letter, and number
length = 16
print(simple_rands.gen(length))

# generate base32 data
print(simple_rands.gen(length, char_pool=string.ascii_uppercase + "234567"))

```
