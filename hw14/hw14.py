import gym

env = gym.make("CartPole-v1", render_mode="human")  # use render_mode="rgb_array" if no display
observation = env.reset()

total_reward = 0
done = False

while not done:
    angle = observation[2]               # pole angle
    angular_velocity = observation[3]    # pole angular velocity

    # Simple rule: combine angle and angular velocity
    action = 0 if angle + 0.5 * angular_velocity < 0 else 1

    observation, reward, done, _, _ = env.step(action)
    total_reward += reward

env.close()
print("Total reward:", total_reward)
