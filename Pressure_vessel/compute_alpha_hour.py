# Define a function to compute heat transfer coefficient
import numpy as np
def compute_alpha_hour(num_rows, num_cols, D, v_wind, time_steps, hours):
    #See example 7.4 solution analysis 2 of Dunfamentals of heat and mass transfer 
    
    alpha_hour = np.zeros((num_rows, num_cols, len(time_steps)))
    #Constants for heat transfer coefficient 
    knu = 15.89e-6 #[m^2/s]
    k_air = 26.3e-3 #W/(m*K)
    Pr = 0.707 #dimensionless 
    C = 0.26 #Constants from book
    m_air_alpha = 0.6

    for ii in range(num_rows):
        for jj in range(num_cols):
            h = []
            
            #Calculate reynolds number and determine constants for nusselts 
            Re = v_wind*3.6*D[ii,jj]/knu            

            #Calculate nusselts
            #C and m_air_alpha are from table 7.4 of the aformentoined book. 
            # Pr is from table A4. 
            Nu = C*Re**m_air_alpha*Pr**(1/3)

            for aa in range(len(v_wind)): 
                #Calculate heat transfer coeeficient per timestep               
                h.append(Nu[aa]*k_air/D[ii,jj])           

            
            alpha_hour[ii, jj, :] = h #np.interp(time_steps, hours, h[:len(hours)])
    return alpha_hour
