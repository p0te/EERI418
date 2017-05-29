syms x
syms y
syms s
syms kc
syms z


po = 0.1;
ts = 300;
zeta = vpasolve(exp((-pi*x)/(sqrt(1-x^2))) == po,x)
omega = vpasolve(ts == 4/(zeta*y),y)
syms kc
syms z
%syms omega
%syms zeta
% kc = 0.075
% ki = 0.0015
% z = ki/kc
 %k = vpasolve([2*zeta*omega==(0.0073507 + 0.63230*kc),omega^2==(0.63230*kc*z)],[kc,z])
s0= solve(s^2 + 2*zeta*omega*s + omega^2 , s )






%k = solve([((0.63230/(s0(1)+ (7.3507)*10^-3))*((kc*(s0(1) + z))/(s0(1)))) + 1 == 0,((0.63230/(s0(2)+ (7.3507)*10^-3))*((kc*(s0(2) + z))/(s0(2)))) +1  == 0],[kc z])

subs(k.kc)
subs(k.z)


