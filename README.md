# AI Assignment

```md
Q1

Question -
Blocks World problem using Simple Hill Climbing.

Heuristic Function -
H(n) : Number of misplaced blocks in the current state as compared to the goal state.

Steps -
1. Evaluate initial state. If its equal to goal state - (found) return.
2. Loop until a solution is found or next states cause no change in the heuristic value.
   (a). Try going to next states one by one, if any better state found, move to next better state without considering other possiblities.
   (b). If no better next state found, stop and return

```

```md
Q2

Question -
8 puzzle problem using Steepest Hill Climbing.

Heuristic Function -
H(n) : Number of misplaced tiles in the current state as compared to the goal state. 

Steps -
1. Evaluate initial state. If its equal to goal state - (found) return.
2. Loop until a solution is found or next states cause no change in the heuristic value.
   (a). Generate all new state possible states from current state.
   (b). Evaluate new states, if any one is equal to goal state, (found) return.
        if any of the next state is better than current state, move to best possible new state.
        else, (not found) return.

```