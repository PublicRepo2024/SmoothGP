import numpy as np
from scipy.special import lambertw

def polar_to_spherical(r, thetas, d):
    assert (d>2 and len(thetas)==d-1)
    if d == 3:
        sin_prods = [r*np.sin(thetas[0])*np.cos(thetas[1]),r*np.sin(thetas[0])*np.sin(thetas[1]),r*np.cos(thetas[0])]
    else:
        sin_thetas = np.sin(thetas)
        sin_prods = [np.cos(thetas[0])*r]
        sin_prods.extend([np.prod(sin_thetas[:j+1])*np.cos(thetas[j+1])*r for j in range(d-2)])
        sin_prods.append(np.prod(sin_thetas)*r)
    return sin_prods

def polar_to_spherical_vec(r, thetas, d):
    assert (d>2)
    if d == 3:
        sin_prods = [r*np.sin(thetas[0])*np.cos(thetas[1]),r*np.sin(thetas[0])*np.sin(thetas[1]),r*np.cos(thetas[0])]
    else:
        sin_thetas = np.sin(thetas)
        sin_prods = [np.cos(thetas[0])*r]
        sin_prods.extend([np.prod(sin_thetas[:j+1])*np.cos(thetas[j+1])*r for j in range(d-2)])
        sin_prods.append(np.prod(sin_thetas)*r)
    return sin_prods
    
def get_laplacian(eps, d):
    thetas = [np.random.uniform(0,np.pi) for i in range(d-2)]
    thetas.append(np.random.uniform(0,2*np.pi))
    r = np.random.gamma(d,scale=1.0/eps)
    return (r, thetas)

def get_laplacian_vec(eps, d, mreps):
    thetas = [np.random.uniform(0, np.pi, size=mreps) for i in range(d-2)]
    thetas.append(np.random.uniform(0, 2*np.pi, size=mreps))
    r = np.random.gamma(d,scale=1.0/eps, size=mreps)
    return (r, thetas)

def get_laplacian_2d(eps):
    theta = np.random.uniform(0,2*np.pi)
    u = np.random.uniform(0,1)
    w = lambertw((u-1)*np.exp(-1),k=-1)
    assert(w.imag==0)
    r = -(w.real+1)/eps
    return (r, theta)

def get_laplacian_2d_vec(eps, mreps):
    theta = np.random.uniform(0, 2*np.pi, mreps)
    u = np.random.uniform(0, 1, mreps)
    w = lambertw((u-1)*np.exp(-1),k=-1)
    assert(w.imag.all()==0)
    r = -(w.real+1)/eps
    return (r, theta)
