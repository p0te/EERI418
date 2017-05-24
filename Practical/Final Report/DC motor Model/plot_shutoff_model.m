Array=dlmread('Motor_shut_off_rpm_smoothed.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
x = linspace(0,1.8,36001);
plot(col1-1.702, col2-0.36)
hold on;
plot(x,1.2*exp(-x/0.769))
xlabel({'Time (s)'},'FontSize',11);

% Create title
title({'Motor Step Response'},'FontSize',11);

% Create ylabel
ylabel({'RPM(/1000)'},'FontSize',11);
hold off;