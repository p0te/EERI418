function [omega,zeta] = po_and_ts(po,ts) %po in percent, ts in seconds
syms x
syms y
[omega,zeta] = vpasolve([exp((-pi*x)/(sqrt(1-x^2))) == po,ts == (4)/(y*x)],[x,y]);
eqn1 = exp((-pi*x)/(sqrt(1-x^2))) == po;
ezplot(eqn1,x);


end