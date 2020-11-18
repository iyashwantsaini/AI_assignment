"""
Q2

Yashwant
101803318
COE15

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

"""

import copy

# finding heuristic value for current_state
# heuristic - no of mismatched tiles in the current state as compared to goal state
def heuristic(curr_state,goal_state):
    val=0
    for i in range(0,3):
        for j in range(0,3):
            if curr_state[i][j]!=goal_state[i][j]:
                val+=1
    return val

# generate all the next possible states from current state
def generate_states(current_state,i_zero,j_zero):
    next_states=[]

    # find possible moves
    # check if left possible
    if (j_zero)>0:
        left=copy.deepcopy(current_state)
        left[i_zero][j_zero],left[i_zero][j_zero-1]=left[i_zero][j_zero-1],left[i_zero][j_zero]
        next_states.append(left)

    # check if right possible
    if (j_zero)<2:
        right=copy.deepcopy(current_state)
        right[i_zero][j_zero],right[i_zero][j_zero+1]=right[i_zero][j_zero+1],right[i_zero][j_zero]
        next_states.append(right)
    
    # check if down possible
    if (i_zero)<2:
        down=copy.deepcopy(current_state)
        down[i_zero][j_zero],down[i_zero+1][j_zero]=down[i_zero+1][j_zero],down[i_zero][j_zero]
        next_states.append(down)
    
    # check if up possible
    if (i_zero)>0:
        up=copy.deepcopy(current_state)
        up[i_zero][j_zero],up[i_zero-1][j_zero]=up[i_zero-1][j_zero],up[i_zero][j_zero]
        next_states.append(up)
    
    return next_states

# find where is the blank/0 in current state
def findzero(curr_state):
    for i in range(3):
        for j in range(3):
            if curr_state[i][j]==0:
                return [i,j]

def solver():
    
    # input 
    init_state=[
        [2,8,3],
        [1,5,4],
        [7,6,0]
    ]
    
    goal_state=[
        [1,2,3],
        [8,0,4],
        [7,6,5]
    ]

    current_state=copy.deepcopy(init_state)

    # 
    prev_heuristic=heuristic(current_state,goal_state)
    
    # save all visited states siwth their heuristic, to avoid repetitions and going in infinite loop
    visited_states=[]
    visited_states.append((prev_heuristic,current_state))

    while(1):

        print(current_state)

        # if goal state found
        if(current_state==goal_state):
            print(current_state)
            print("solution found")
            return
            
        # find indices of the 0 containing place in the current state
        zero_index=findzero(current_state)
        i_=zero_index[0]
        j_=zero_index[1]

        # generate all possible states from current state
        states=generate_states(current_state,i_,j_)
        
        # set min heuristic to inf
        min_heu=10
        # set min index to inf
        min_index=10

        # find the best possible next state out of all states possible
        for i in range(len(states)):
            curr_heu=heuristic(states[i],goal_state)
            # checking if the state is already visited or not
            if (curr_heu,states[i]) not in visited_states:
                if curr_heu<min_heu:
                    min_heu=curr_heu
                    min_index=i

        # current state is better than next states
        if min_heu>=prev_heuristic:
            print("no solution")
            print("final state - ",current_state)
            return

        # all next states are visited already or are not good enough
        elif min_heu==10:
            print("no more paths possible")
            print("last state - ",current_state)

        # move to next state
        else:
            
            if states[min_index]==goal_state:
                print(states[min_index])
                print("solution found")
                return
            
            # moving ot new state
            current_state=copy.deepcopy(states[min_index])
            
            # saving the current state to visited states
            new_state=copy.deepcopy(states[min_index])
            visited_states.append((min_heu,new_state))

solver()