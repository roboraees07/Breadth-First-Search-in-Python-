# Breadth-First-Search-in-Python-
Implementation of Breadth First Search (BFS) in Python for traversing or searching tree or graph data structures.

# Breadth First Search in Python

This repository contains an implementation of the Breadth First Search (BFS) algorithm in Python. BFS is a fundamental algorithm used for traversing or searching tree or graph data structures. It explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

## Overview

The BFS algorithm starts at the root node and explores all its neighboring nodes at the present depth prior to moving on to nodes at the next depth level. It uses a queue to keep track of the nodes that need to be explored.

## Features

- Simple and clear implementation of BFS
- Traverses graphs level by level
- Can be adapted to solve shortest path problems in unweighted graphs

## Usage

To use the BFS implementation, simply run the `bfs.py` script. It uses a predefined graph structure for demonstration purposes.

### Example

Here's a simple example demonstrating how the BFS algorithm works:

```python
# Define the graph as a dictionary
graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': {},
    'E': {},
    'F': {},
    'G': {}
}

# Define the start and goal nodes
start = 'A'
goal = 'D'

# Execute the BFS algorithm
print(bfs(start))  # Output: ['A', 'B', 'D']
