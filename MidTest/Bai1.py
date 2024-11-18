def next_state(current_state, input_signal):
    state_transition = {
        ('S0', 1): 'S0',
        ('S0', 0): 'S1',
        ('S1', 1): 'S1',
        ('S1', 0): 'S2',
        ('S2', 1): 'S2',
        ('S2', 0): 'S0'
    }
    return state_transition.get((current_state, input_signal), None)
print("Next state from S0 with input 1:", next_state('S0', 1))  
print("Next state from S0 with input 0:", next_state('S0', 0))  
print("Next state from S1 with input 1:", next_state('S1', 1))  
print("Next state from S1 with input 0:", next_state('S1', 0))  
print("Next state from S2 with input 1:", next_state('S2', 1)) 
print("Next state from S2 with input 0:", next_state('S2', 0))