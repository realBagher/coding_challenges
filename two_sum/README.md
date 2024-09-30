
# Two Sum Problem Solution

This project contains a Python implementation of the **Two Sum** problem and corresponding unit tests.



## Solution Approach

The solution uses a **hash map** (Python dictionary) to store the elements of the array as keys and their indices as values. As we iterate through the list of numbers, we compute the **complement** (target - current number). If the complement is already in the dictionary, it means we have found the pair of numbers that add up to the target, and we return their indices.

### Time and Space Complexity
- **Time Complexity:** O(n), where `n` is the number of elements in the list `nums`. We only iterate through the list once.
- **Space Complexity:** O(n), as we store up to `n` elements in the hash map.

## File Structure

- **solution.py**: Contains the `Solution` class and the `twoSum` method.
- **test.py**: Contains the unit tests for the `twoSum` method using Python's `unittest` framework.
- **README.md**: This documentation file.

## Installation

To set up and run this project locally, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/realBagher/coding_challenges/tree/main/two_sum
   cd two-sum
   ```

2. **Ensure you have Python installed**:
   Make sure you have Python 3.x installed on your system.



## Running the Code

### Example Usage
To run the solution and get the result for specific input, you can use the following code in a Python file or interactive shell:

```python
from solution import Solution

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))  # Output: [0, 1]
```

### Running Unit Tests

The project includes unit tests to verify the correctness of the solution. You can run these tests using Python’s `unittest` framework:

1. Run the following command in the terminal to execute the tests:
   ```bash
   python -m unittest test_solution.py
   ```

2. If all tests pass, you will see output like this:
   ```
   ..
   ----------------------------------------------------------------------
   Ran 2 tests in 0.000s

   OK
   ```

### Writing Custom Tests

To write your own tests, you can add additional test cases in the `test_solution.py` file using the following format:

```python
import unittest
from solution import Solution

class TestTwoSum(unittest.TestCase):
    def test_custom_case(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([1, 5, 3, 8], 9), [0, 3])  # Example custom case

if __name__ == "__main__":
    unittest.main()

```
