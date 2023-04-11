import random
import gym

env = gym.make("CartPole-v1")
episodes = 10

for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0
    
    while not done:
        action = random.choice([0, 1])
        step_result = env.step(action)
        next_state, reward, done, info = step_result[:4]  # Ignore the last two values
        score += reward
        env.render()
    
    print(f"Episode {episode}, Score: {score}")
    
env.close()
