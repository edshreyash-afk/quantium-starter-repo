#!/bin/bash

# 1. Activate the project virtual environment
# Note: In Bash/Git Bash on Windows, use the forward slash
source venv/Scripts/activate

# 2. Execute the test suite
# This runs all tests found in your /tests directory
pytest tests/

# 3. Capture the exit code of the pytest command
# If pytest succeeds, it returns 0. If it fails, it returns 1+.
if [ $? -eq 0 ]; then
    echo "CI Step: Tests Passed!"
    exit 0
else
    echo "CI Step: Tests Failed!"
    exit 1
fi