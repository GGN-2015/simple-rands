import random
import string
from typing import Optional

# random value generator
RNG = random.Random()

# set seed for random generator
def seed(value:int):
    RNG.seed(value)

def gen(length:int, rng:Optional[random.Random]=None, char_pool:Optional[str]=None):
    """
    Generate a random string of specified length containing lowercase letters, uppercase letters and numbers
    
    Parameters:
        length (int): The length of the string to be generated, must be a positive integer
    
    Returns:
        str: Randomly generated string
    
    Raises:
        ValueError: Raised when the length is not a positive integer
    """
    # Validate input parameter legality
    if not isinstance(length, int) or length <= 0:
        raise ValueError("String length must be a positive integer greater than 0")
    
    if rng is None: # use default
        rng = RNG

    # type of rng should be verified
    if not isinstance(rng, random.Random):
        raise TypeError()

    if char_pool is None:
        # Build character pool: lowercase letters + uppercase letters + digits
        char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Randomly select specified number of characters from the character pool and concatenate into a string
    random_chars = [rng.choice(char_pool) for _ in range(length)]
    random_string = ''.join(random_chars)
    
    return random_string

# Test examples
if __name__ == "__main__":
    # set seed for generator
    seed(42)

    # Generate random string with length 8
    print("Random string of length 8:", gen(8))
    # Generate random string with length 16
    print("Random string of length 16:", gen(16))
    # Generate random string with length 20
    print("Random string of length 20:", gen(20))