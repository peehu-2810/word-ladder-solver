# Word Ladder Solver using BFS

## Overview
This project implements a solution to the Word Ladder problem using the Breadth-First Search (BFS) algorithm. The objective is to transform a given start word into a target word by changing one letter at a time, ensuring that each intermediate word is valid.

The algorithm guarantees the shortest transformation sequence by exploring all possible word combinations level by level.

---

## Features
- Implementation of BFS search algorithm
- Finds shortest transformation path
- Validates words using a predefined dictionary
- Command-line interface (CLI) based execution
- Displays step-by-step transformation
- Shows total number of steps

---

## Project Structure

word-ladder-solver/
│
├── main.py            # Handles user input and execution
├── solver.py          # Contains BFS implementation
├── words.txt          # Dictionary of valid words
├── README.md          # Project documentation
└── requirements.txt   # Dependencies (none required)

---

## Installation

1. Clone the repository:

git clone https://github.com/your-username/word-ladder-solver

2. Navigate to the project directory:

cd word-ladder-solver

3. Ensure Python 3.x is installed.

No external libraries are required.

---

## Usage

Run the program using:

python main.py

### Input Format
Enter two words of the same length:
- Start word
- Target word

Example:

Start: cat  
End: dog  

---

## Output

The program displays:
- Step-by-step transformation sequence
- Total number of steps required

Example:

cat  
bat  
bot  
dot  
dog  

Total Steps: 4

---

## Algorithms Used

### Breadth-First Search (BFS)

BFS is an uninformed search algorithm used to explore nodes level by level.

In this project:
- Each word is treated as a node  
- A connection exists if two words differ by one letter  
- BFS explores all possible transformations  
- The first time the target word is reached ensures the shortest path  

---

## Problem Representation

- Words → Nodes  
- One-letter change → Edge  
- Dictionary → Valid state space  

---

## Conclusion
Through this project, I explored how BFS can be applied to solve transformation-based problems efficiently. The approach ensures that the shortest sequence of valid word changes is found.

---

## Learning Outcomes

Through this project, I gained a better understanding of:

- How BFS works in practical scenarios  
- Graph-based problem representation  
- Shortest path finding techniques  
- Importance of visited states in search algorithms  
- Writing modular Python programs  

---

## Challenges Faced

Some challenges encountered during development:

- Generating valid word transformations efficiently  
- Avoiding repeated exploration of states  
- Handling cases where no valid path exists  
- Maintaining clear and readable code structure  

---

## Future Improvements

This project can be improved by:

- Using a larger dictionary for better results  
- Implementing bidirectional BFS for optimization  
- Adding visualization of transformations  
- Supporting different word lengths dynamically  

---

## Author Note

This project was developed as part of AI/ML coursework to demonstrate the application of search algorithms in solving real-world problems.
