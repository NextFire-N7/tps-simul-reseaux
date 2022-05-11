#plot [0:20] "avr_response.out" using 1:3 title "instantaneous" w l, "avr_response.out" using 1:4 title "average" w l, "avr_response.out" using 1:4:5 w yerrorbars 
plot [0:1000] "loss.out" using 1:3 title "drop probability" w l, "loss.out" using 1:4 title "average drop" w l, "loss.out" using 1:6 title "collision probability" w l, "loss.out" using 1:7 title "average collision" w l 

#time #drop %loss avr_%drop #coll %col avr_%coll thpt_a thpt_o thpt_s rho_a rho_o rho_s
