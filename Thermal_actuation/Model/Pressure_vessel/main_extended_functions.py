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

def h_cpn(A, peri ,L, K, Cp,delta_T, mu, nu, beta ):
    # Calculates heat transfer coeefficient for free convection in closed cilinder 
    #System: horizontal cilinder

    # Inputs:
    # A: Area of cylinder
    # peri: perimeter of cylinder
    # mu: dynamic viscosity
    # K: thermal conductivity
    # Cp: specific heat capacity at constant pressure
    # delta_T: temperature difference between cylinder and air
    # nu: kinematic viscosity
    # L: length of cylinder
    # beta: thermal expansion coefficient of the medium 

    #Retun: heat transfer coefficient
    C = 0.47
    n = 0.25
    K = 1

    X = A/peri
    Gr = (9.81*beta*delta_T*X**3)/(nu**2)

    Pr = mu*Cp/K

    h = (K/L)*C*((Gr*Pr)**n)*K
    return h

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