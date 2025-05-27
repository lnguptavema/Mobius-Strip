import matplotlib.pyplot as plt
import numpy as np
def mobius_strip(a,b,num_points):
    u=np.linspace(0,2*np.pi,num_points)
    v=np.linspace(-b,b,num_points)
    U,V=np.meshgrid(u,v)
    x=(a+V/2*np.cos(U/2))*np.cos(U)
    y=(a+V/2*np.cos(U/2))*np.sin(U)
    z=V/2*np.sin(U/2)
    return x,y,z
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