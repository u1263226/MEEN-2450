# MEEN-2450

## Lab 8
ODE Decomposition:

dx/dt = v

dv/dt = d^2x/dt^2 = (Fp - Fd - Frr)/m
    
Fp = constant

Fd = (ro*Cd*A*v**2)/2 = (ro*Cd*A*(dx/dt)**2)/2

Frr = m*g*Crr

dy/dt = {dx/dt, dv/dt}

Includes 3 files: eulers2, train_motion, and moving_train

Also a jpg of the output graph

