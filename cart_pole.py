import gym
from statistics import mean

env = gym.make("CartPole-v1")


def basic_policy(obs):
	angle = obs[2]
	return 0 if angle < 0 else 1


totals = []

for _ in range(1000):
  episode_rewards = 0

  obs = env.reset()

  for step in range(200):
  	action = basic_policy(obs)
  	obs, reward, done, info = env.step(action)
  	episode_rewards += reward

  	if done:
  		break

  totals.append(episode_rewards)

print(mean(totals))

env.close()