# Word Ladder Solver using BFS

## Overview
This project implements a solution to the Word Ladder problem using the Breadth-First Search (BFS) algorithm. The goal is to transform a starting word into a target word by changing one letter at a time, while ensuring that each intermediate word is valid.

The algorithm guarantees the shortest transformation sequence by exploring all possible paths level by level.

---

## Features
- Implementation of BFS for shortest path finding
- Valid word transformation using a predefined dictionary
- Command-line based execution
- Displays transformation steps clearly
- Calculates total number of steps

---

## Project Structure
word-ladder-solver/
├── main.py  
├── solver.py  
├── words.txt  
├── README.md  
├── requirements.txt  
└── .gitignore  

---

## Installation
1. Clone the repository  
2. Navigate to the project directory  
3. Ensure Python 3.x is installed  

No external libraries are required.

---

## Usage
Run the following command:

python main.py

Enter the start and end words when prompted.  
Both words must be of the same length.

---

## Algorithm Used

### Breadth-First Search (BFS)
- Each word is treated as a node  
- A connection exists if two words differ by one letter  
- BFS explores all possible transformations level by level  
- The first time the target word is reached ensures the shortest path  

---

## Example

Input:
cat → dog  

Output:
cat  
bat  
bot  
dot  
dog  

Total Steps: 4

---

## Conclusion
This project demonstrates how BFS can be applied to solve transformation-based problems efficiently. By representing words as nodes in a graph, the algorithm is able to determine the shortest sequence of valid transitions.
