import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('data.csv', delimiter=',', names=True)


head_x = data['head_x']
head_y = data['head_y']
tail_x = data['tail_x']
tail_y = data['tail_y']
frames = data['frame']

theta = np.arctan2(head_y - tail_y, head_x - tail_x)


fig, axs = plt.subplots(1, 2, figsize=(14, 6))


axs[0].plot(head_x, head_y, 'ro-', label='head')
axs[0].plot(tail_x, tail_y, 'bo-', label='tail')
axs[0].set_title('Trajectory of the Robot')
axs[0].set_xlabel('x-loc (unit)')
axs[0].set_ylabel('y-loc (unit)')
axs[0].legend()
axs[0].grid(True)


axs[1].plot(frames, theta, 'g^-')
axs[1].set_title('Orientation of the Robot')
axs[1].set_xlabel('frame #')
axs[1].set_ylabel('theta (rad)')
axs[1].grid(True)


plt.tight_layout()
plt.show() 
