import matplotlib.pyplot as plt  # Python script that models a Mobius strip using parametric equations and computes key geometric properties
import numpy as np
# a,b are the radius and width 
# defining the strip
def mobius_strip(a,b,num_points):
    # u is the  array created by divide circle(0 to 2 )accordingto num points 
    u = np.linspace(0, 2 * np.pi,num_points)  # v will be the array is created by dividing -b to b with no of points
    v = np.linspace(-b,b,num_points)  # forming meshgrid combination of U, V
    U,V = np.meshgrid(u,v) 
    # equations of Mobius Strip
    x = (a + V/2 * np.cos(U/2) ) * np.cos(U) # a is radius , V will be width parameter and np.cos is the x-coordinate for parametric eqn
    # y will be the sin component
    y = (a + V/2 * np.cos(U/2) ) * np.sin(U)
    # for vertical coordinates we need radius
    z = V/2 * np.sin(U/2)
    return x,y,z
    # return mobius strip vector eqn
#plotting the strip
def plot(x,y,z):
    fig =plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot_surface(x,y,z,cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Mobius Strip')
    plt.show()
if __name__=="__main__":
    plot(*mobius_strip(2,0.3,100))
    # radius 2 ,width 0.3 and dividing by 100