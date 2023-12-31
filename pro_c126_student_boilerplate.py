# -*- coding: utf-8 -*-
"""PRO-C126-Student-Boilerplate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IpkuDMnfWWxcdBjC1_emHF7DJYJiz2Tf

## RL Problem to Solve:

The **machine/bot** needs to find a way out to reach the **Goal**(Room Number 5).The machine will start from any room randomly.

<img src="https://s3-whjr-curriculum-uploads.whjr.online/f39c3b14-04c8-4171-8bd4-7693efcdb792.jpg" width= 400>

## RL Components:

* Environment

<img src="https://s3-whjr-curriculum-uploads.whjr.online/af5a1d77-041a-4bba-be4e-ca26aea97771.png" width= 300>

* Agent

<img src="https://s3-whjr-curriculum-uploads.whjr.online/fda2e793-0302-420c-981b-dbf32ecb1d12.png" width= 200>

* States

> The agent/machine can be in any of the 6 rooms( 5 rooms + 1 goal room) of the
lobby. Hence there **6 possible states**.

> <img src="https://s3-whjr-curriculum-uploads.whjr.online/e0f568a6-77af-4b52-873e-8949f388cbb6.jpg" width= 50>


* Actions

> The agent/machine can choose to move to any of the 6 rooms( 5 rooms + 1 goal room) of the lobby. Hence there also **6 possible actions**.


> <img src="https://s3-whjr-curriculum-uploads.whjr.online/0e684ce5-6454-47bd-bb2d-d3668f7a0370.jpg" width= 300>


* Rewards

> **Possible Rewards: -1, 0, 100**


> <img src="https://s3-whjr-curriculum-uploads.whjr.online/7f9acae9-73be-41ab-8686-0cd74f4840ad.jpg" width= 300>


* **Can’t Move**:If there no direct way from one room
to another, then the reward is -1.

* **Move**: If the machine can move from the current
room(state) to the next room(action)
then the reward is 0.

* **Goal**: If the machine is at/reached the goal,
then the reward is 100

## Import Modules
"""

import numpy as np
import random

"""## Reward Martix

> <img src="https://s3-whjr-curriculum-uploads.whjr.online/46dc27ea-cc8c-4b7b-959f-88406531a3c3.jpg" width= 400>

* **Can’t Move**:If there no direct way from one room
to another, then the reward is -1.

* **Move**: If the machine can move from the current
room(state) to the next room(action)
then the reward is 0.

* **Goal**: If the machine is at/reached the goal,
then the reward is 100.

> <img src="https://s3-whjr-curriculum-uploads.whjr.online/3183f05b-f22f-46b6-96b4-00043c942250.jpg" width= 400>

"""

rewards = np.array([
    [-1, -1, -1, -1,  0,  -1],
    [-1, -1, -1,  0, -1, 100],
    [-1, -1, -1 , 0 ,-1 , -1],
    [-1,  0,  0 ,-1  ,-1 , -1],
    [0, -1, -1 , -1 ,-1 ,100],
    [-1, -1, -1, -1,  0, 100]
])

"""## Initial State"""

def set_initial_state():
    return np.random.randint(0, 6)

"""## Get Action"""

def get_action(current_state, reward_matrix):
    available_action = []
    print("reward_matrix","\n",reward_matrix)
    for action in enumerate(reward_matrix[current_state]):
        if action[1]!= -1:
            available_action.append(action[0])
    choose_action = random.choice(available_action)
    print("Current State",current_state)
    print("Random choice of Action from",available_action,"is", choose_action)
    return choose_action

"""##Q matrix
**Q-learning** is a reinforcement learning algorithm. Given the current state, it helps to find the best action to be taken by the agent.
Q stands for Quality in Q-learning. Quality represents how useful action is in gaining a reward.
To perform Q-learning, we use **Q-matrix**. It is also in the form of states as rows and actions as columns. Initially, all the elements of the Q- matrix are zeroes.
"""

q_matrix = np.zeros([6,6])
print(q_matrix)

"""## Take Action"""

def take_action(current_state, reward_matrix, gamma):

    action = get_action(current_state, reward_matrix)

    #Current State, Action Reward
    current_sa_reward = reward_matrix[current_state, action]

    # New State, Action Reward
    q_sa_value = max(q_matrix[action,])

    # Current Q state
    q_current_state = current_sa_reward + (gamma * q_sa_value)

    # Update Q matrix
    q_matrix[current_state,action] = q_current_state

    print("q_matrix ","\n", q_matrix)

    new_state = action

    print("********************************************************************")

    if new_state == 5:
        print("Reached Goal!")
    else:
        print(f"Old State:{current_state} New State: {new_state}")

    return new_state

"""## Train RL Model

Aim is to make the agent explore different states and reach the goal, the rewards are updated after each trial.

Agent completes an **episode** when it starts from initial state and reaches the goal.

For each action, Q-matrix is updated. This will act as the trained environment for the agent. Using the updated Q-matrix the agent can look for maximum reward and finds optimal path for any state.

Refer the link below to check how the episodes are run and Q-matrix is updated.
[Run Multiple Episodes](https://whitehatjrcontent.s3.ap-south-1.amazonaws.com/Teacher-Resources/COCOS_Applets/POC/Coding/SimpleQ-RL/final/index.html)
"""

def run_episode(initial_state,reward_matrix, gamma):

    new_state =  take_action(initial_state, reward_matrix, gamma)

     # ADD CODE HERE ##

def train(episodes, reward_matrix, gamma):
    print("Training...")

    # ADD CODE HERE ##

gamma = 0.8

# Get Q table
q_table = train(2, rewards, gamma)

print("Final Q Table: ", q_table)

"""## Best Path to Goal

By looking at the q_table we find that the rewards are calculated for different states and actions. For a particular state the maximum rewards are given to the action which should be taken to find the optimal path to reach the goal.
"""

def optimal_path(q_table):
    path=[]
     # ADD CODE HERE ##

Q_optimal_path, max_reward  = optimal_path(q_table)
print(Q_optimal_path, max_reward)