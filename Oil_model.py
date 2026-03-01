import numpy as np
import matplotlib.pyplot as plt

def main(phi = 90):
    # length (m), weight per meter (N/m)
    L, w = 3000, 200

    #Angle
    # phi = phi  #in degrees
    phi_r = np.deg2rad(phi)
    # phi is inclination from the horizontal
    # so phi = 0 means horizontal and phi = 90 means drill is vertical

    # Friction
    mu = 400 # Pa

    # outer and inner diameter (m)
    Do, Di = 0.127, 0.10

    #Young and Shear Modulus (Pa)
    E, G = 200e9, 80e9
    # Torque (Nm)
    T_bit = 5000
    # print(f"{L = }\n{w = }\n{Di = }\n{Do = }\n{E = }\n{G = }\n{T_bit = }")

    #Area
    A = (np.pi * (Do**2 - Di**2) )/4
    #Polar moment of inertia
    J = (np.pi * (Do**4 - Di**4) )/32

    # Depth intervals
    z = np.linspace(start=0, stop=L, num=201)

    #Friction
    N = w * np.cos(phi_r)
    Ff = mu * N

    #Axial Force and Stress
    F = (w*z * np.sin(phi_r)) - (Ff*z)
    sigma = F / A

    # Total Elongation i.e. delta L
    delta_l = (w * L**2) *(np.sin(phi_r) - mu * np.cos(phi_r)) / (2*A*E)

    #Addind torque produced by friction
    T_f = Ff * (Do/2) * L

    #Shear stress
    T_total = T_bit + T_f
    tau = ( T_total * Do )/ (2 * J)

    #Twist Angle
    theta = (T_total * L) / (G * J)

    # print("Surface Hook Load:", w * L, "N")
    # print("Total Elongation:", delta_l, "m")
    # print("Max Axial Stress:", sigma[-1], "Pa")
    # print("Max Shear Stress:", tau, "Pa")
    # print("Twist Angle (rad):", theta)

    return z, sigma

    plt.plot(z, sigma)
    plt.xlabel("Depth (m)")
    plt.ylabel("Axial Stress (Pa)")
    plt.show()

if __name__ == "__main__":
    z = []
    sigma = []
    z1, sigma1 = main()
    z.append(z1)
    sigma.append(sigma1)

    z1, sigma1 = main(60)
    z.append(z1)
    sigma.append(sigma1)

    z1, sigma1 = main(30)
    z.append(z1)
    sigma.append(sigma1)

    z1, sigma1 = main(10)
    z.append(z1)
    sigma.append(sigma1)

    plt.gca().invert_yaxis()
    for i in range(len(z)):
        plt.plot(z[i], sigma[-i-1])
    plt.xlabel("Depth (m)")
    plt.ylabel("Axial Stress (Pa)")
    plt.show()