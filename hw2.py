from scipy.stats import norm, t
import numpy as np
import math
import matplotlib.pyplot as plt

#Problem 3

def prob3():
    
    mean = 50
    std = 2
    n = 100

    gamma_95 = 0.95
    rhobar_95 = norm.ppf( (1-gamma_95)/2 )
    rho_95 = rhobar_95*std/np.sqrt(n)    
    ans_95 = [mean+rho_95,mean-rho_95]
    
    gamma_99 = 0.99
    rhobar_99 = norm.ppf( (1-gamma_99)/2 )
    rho_99 = rhobar_99*std/np.sqrt(n)    
    ans_99 = [mean+rho_99,mean-rho_99]
    
    print("Part(a)& Part(B)")
    print("95%: ",ans_95)
    print("99%: ",ans_99)

    # compute gamma = ? Given rho
    # rho = rhobar*std/sart(n)
    # rhobar = rho/(std/sqrt(n))
    # (1-gamma)/2 = cdf(rhobar)
    # gamma = 1-2*cdf(rhobar)
    rho = 0.3
    rhobar = rho/(std/np.sqrt(n))
    gamma = abs(float(1-2*norm.cdf(rhobar)))*100

    print("Part(C)")
    print("rhobar", rhobar)
    print("Gamma" , gamma, '%')
    
    gamma_95 = 0.95
    gamma_99 = 0.99    
    sig_hat = 2
    rho = 0.3    
        
    rho_hat_95 = norm.ppf( (1-gamma_95)/2)
    rho_hat_99 = norm.ppf( (1-gamma_99)/2) 
      
    N_95 = (rho_hat_95*sig_hat/rho)**2
    N_99 = (rho_hat_99*sig_hat/rho)**2
    
    print("Part(D) & Part (E)")
    print("Sample Needed for 95%: ",N_95)
    print("Sample Needed for 99%: ", N_99)
    
def prob4():
    N = 8
    sigma_hat2 = 1.018
    mu_hat = 3410.14    
    gamma_95 = 0.95
    gamma_99 = 0.99
        
    rhobar_95 = t.ppf( (1-gamma_95)/2, N-1)
    rho_95 = rhobar_95*(sigma_hat2/np.sqrt(8))
    ans_95 = [mu_hat+rho_95, mu_hat-rho_95]
    
    rhobar_99 = t.ppf( (1-gamma_99)/2, 7)
    rho_99 = rhobar_99*(sigma_hat2/np.sqrt(8))
    ans_99 = [mu_hat+rho_99, mu_hat-rho_99]
    
    print("Part(C)")
    print("95%: " , ans_95)
    print("99%: " , ans_99)   
    
def prob5():
    N = 45
    mu_hat = 0.165
    sigma_hat = 0.022
    
    gamma = 0.95
    rho_bar = norm.ppf( (1-gamma)/2 )
    rho = rho_bar*(sigma_hat/np.sqrt(N))
    ans = [mu_hat-rho, mu_hat+rho]
    print("Part a: ", ans)
    
    x = np.linspace(0,1, N)
    mu = 0.165
    sigma = 0.022
    
    s = np.random.normal( loc = 0, scale = 1 , size = 45)
    plt.hist(s, 30, density=True)
    #plt.show()
    
    ## Want gamma given interval [0.157,0.167], 
    # mu = 0.165, sigma_hat = 0.022, n = 45
    # since N >40 & sigma_hat is given
    # We can use Z
    # Interval [mu-rho,mu+rhou]
    # rho = 0.167-mu
    # rho = rho_hat*(sigma_hat/sqrt(n))
    # rho_hat = rho/(sigma_hat/sqrt(n))
    # rho_hat = ppf( (1-gamma)/2)
    # (1-gamma)/2 = cdf(rho_hat)
    # gamma = 1-2*cdf(rho_hat)
    
    rho =  0.167-mu
    rho_hat = rho/(sigma_hat/np.sqrt(N))
    gamma = 1-2*norm.cdf(rho_hat)
    ans = abs(gamma)*100
    
    print("The condidence level for the interval is: ", ans)
    
    
    
prob5()


