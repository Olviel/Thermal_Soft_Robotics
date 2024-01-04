import numpy as np

def calc_mu(T):
    #source: 
    # Calculates dynamic viscosity of air
    # T: Temperature of the fluid [K]
    # Output: dynamic viscosity

    # Constants
    mu0 = 1.716e-5
    T0 = 273.15
    S_mu   = 111

    # Calculate dynamic viscosity
    mu = mu0*((T0+S_mu)/(T+S_mu))*(T/T0)**(3/2)
    return mu 

def calc_nu(T,rho):
    # Calculates kinematic viscosity of air
    # T: Temperature of the fluid [K]
    # Output: kinematic viscosity

    # Calculate kinematic viscosity
    nu = calc_mu(T)/rho
    return nu

# For all fomrula,s see table 3.3 in # https://link.springer.com/content/pdf/10.1007/978-981-10-0807-8.pdf
def h_cap(di,do):
    # Calculates heat transfer coeefficient for two concentric cylinders
    # System: two concentric cylinders 
    # Assumptions laminar flow 
    # Input: inner diameter, outer diameter
    # Output: heat transfer coefficient

    X = 0.5*(do-di)
    h = (X**3*(1/(di**(3/5))+1/(do**(3/5))**5))**(-1/4)
    return h

def h_cpn(A, peri ,L, K, Cp,T_f, T_s, rho_air):
    # Calculates heat transfer coeefficient for free convection in closed cilinder 
    #System: horizontal cilinder

    # Inputs:
    # A: Area of cylinder
    # peri: perimeter of cylinder
    # mu: dynamic viscosity
    # K: thermal conductivity
    # Cp: specific heat capacity at constant pressure
    # T_f : temperature of fluid
    # T_s: temperature of surface
    # nu: kinematic viscosity
    # L: length of cylinder
    # beta: thermal expansion coefficient of the medium 

    #Retun: heat transfer coefficient
    C = 0.47
    n = 0.25
    K = 1

    X = A/peri
    delta_T = abs(T_f-T_s)
    beta = 1/(np.average([T_f,T_s])) # Formula 3.23 c
    Gr = (9.81*beta*delta_T*X**3)/(calc_nu(T_f,rho_air)**2) # Formula 3.22d
    #print("beta:", beta, "Gr:", Gr, "n:", n, "X:", X, "delta_T:", delta_T, "nu:", calc_nu(T_f,rho_air))

    Pr = calc_mu(T_f)*Cp/K #formula 3.22c
    h = (K/L)*C*((Gr*Pr)**n)*K
    
    return abs(h)

def h_cac(v,D):
    # Convetion from container to ambient air 
    #See example 7.4 solution analysis 2 of Fundamentals of heat and mass transfer 
    
    #Inputs
    # v_wind: wind speed [m/s]
    # D: diameter of container [m]
    
    #Outputs
    # h_cac: heat transfer coefficient [W/(m^2*K)]
    
    #Constants for heat transfer coefficient 
    knu = 15.89e-6 #[m^2/s]
    k_air = 26.3e-3 #W/(m*K)
    Pr = 0.707 #dimensionless 
    C = 0.26 #Constants from book
    m_air_alpha = 0.6

    #Calculate reynolds number and determine constants for nusselts 
    Re = v*3.6*D/knu            

    #Calculate nusselts
    #C and m_air_alpha are from table 7.4 of the aformentoined book. 
    # Pr is from table A4. 
    Nu = C*Re**m_air_alpha*Pr**(1/3)

    h_cac = Nu*k_air/D
    return h_cac
   
def machine_precision(num, den):
    # Adjust num and den directly based on the condition
    if not 1e-16 < abs(num) < -1e-16:
        num = 0
    if not 1e-16 < abs(den) < -1e-16:
        den = 0

    # Handle division by zero
    if den == 0:
        return 0  # or some other value or error handling

    # Calculate and return the fraction
    frac = num / den
    return frac 

def mu_novec(T): 
    # Calculates dynamic viscosity of novec
    # T: Temperature of the fluid [K]
    # Output: dynamic viscosity

    Z = 10**(10**(10.151-4.606*np.log(T)))-0.7
    mu = Z - np.exp(-0.7-3.295*Z+0.6119*Z**2-0.3193*Z**3)
    return mu

def c_novec(T):
    # Calculates specific heat capacity of novec
    # T: Temperature of the fluid [K]
    # Output: specific heat ca
    c = 1223.2+3.0203*(T-273.15)
    return c

