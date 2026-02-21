#!/bin/bash

# 1. Activate the project virtual environment
# Using forward slashes for Linux compatibility
source venv/Scripts/activate

# 2. Execute the test suite
# Using 'python -m pytest' ensures the root directory is in the path
python -m pytest tests/

# 3. Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $? -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed. Check the logs above."
    exit 1
fi