import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

# This mu needs to be changed for changing the parameter
mu = 5

''' For changing the initial conditions please change init_cond
    init_cond[0]=x(t),
    init_cond[1]=dx(t)/dt
'''
init_cond = [0, -1]


def function(init_cond, t):

    '''
    This function returns the differential equations using two states
    the state x(t) and its derivative
    '''
    x1 = init_cond[1]
    x2 = mu*(1-(init_cond[0]**2))*init_cond[1]-init_cond[0]
    f = [x1, x2]
    return f


def state_plot(sol, t):

    '''
    This function creates the plot of the two states-x(t) and dx(t)/dt vs time.
    Different options for customizing the plot features are also provided in
    this function.
    '''
    line1, = plt.plot(t, sol[:, 0], '.-', label='x', linewidth=1,
                      markersize=1, markeredgewidth=1, color='r')
    line2, = plt.plot(t, sol[:, 1], 'D-', label='dx/dt', linewidth=2,
                      markersize=1, markeredgewidth=1, color='b')
    plt.grid()
    plt.title("Plot of x(t) and dx(t)/dt vs Time with mu= "+str(mu) +
              "roll 15307r001", fontname='serif', fontsize=14)
    plt.xlabel("Time", fontname='serif', fontsize=12)
    plt.xticks(range(0, 50)[::2], family='serif', fontsize=8)
    plt.ylabel("States", fontname='serif', fontsize=12)
    plt.yticks(family='serif', fontsize=12)
    plt.legend(prop={'family': 'serif', 'size': 12})
    plt.savefig('Plot_of_states.png')


def phase_plot(sol):

    '''
    This function creates the phase plot of the oscillator for a particular
    value of mu
    '''
    plt.grid()
    plt.plot(sol[:, 0], sol[:, 1], linewidth=2, label='Phase Plot')
    plt.title('Phase Plot with mu= '+str(mu) +
              "roll 15307r001", fontname='serif', fontsize=14)
    plt.xlabel('x', fontname='serif', fontsize=12)
    plt.ylabel('dx/dt', fontname='serif', fontsize=12)
    plt.savefig('Phase_plot.png')


def main():

    '''
    solves the differential equation and creates the two required plots
    '''
    t = np.linspace(0, 50, 10000)
    sol = odeint(function, init_cond, t)
    state_plot(sol, t)
    phase_plot(sol)

if __name__ == '__main__':
    main()
