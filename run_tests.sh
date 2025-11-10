#!/bin/bash
# Simple test script for the repository

echo "Running tests for public-test repository..."
echo ""

# Test 1: Verify README exists
echo "Test 1: Checking if README.md exists..."
if [ -f "README.md" ]; then
    echo "✓ PASS: README.md exists"
else
    echo "✗ FAIL: README.md not found"
    exit 1
fi

# Test 2: Verify test.sh exists and is executable
echo "Test 2: Checking if test.sh exists and is executable..."
if [ -f "test.sh" ] && [ -x "test.sh" ]; then
    echo "✓ PASS: test.sh exists and is executable"
else
    echo "✗ FAIL: test.sh not found or not executable"
    exit 1
fi

# Test 3: Verify we're in a git repository
echo "Test 3: Checking if this is a git repository..."
if git rev-parse --git-dir > /dev/null 2>&1; then
    echo "✓ PASS: This is a git repository"
else
    echo "✗ FAIL: Not a git repository"
    exit 1
fi

# Test 4: Verify GitHub Actions workflow exists
echo "Test 4: Checking if GitHub Actions workflow exists..."
if [ -f ".github/workflows/main.yml" ]; then
    echo "✓ PASS: GitHub Actions workflow exists"
else
    echo "✗ FAIL: GitHub Actions workflow not found"
    exit 1
fi

echo ""
echo "All tests passed! ✓"
exit 0
