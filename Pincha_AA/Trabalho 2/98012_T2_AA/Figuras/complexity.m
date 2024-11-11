clear all
close all
clc

Size =[10, 13, 15, 16, 18, 20, 23, 25, 26, 28, 30];
Total_operacoes =[423, 706, 828, 1049, 1064, 1558, 1665, 2017, 2265, 2401, 2622];


% Linear model Poly1:
%      f(x) = p1*x + p2
% Coefficients (with 95% confidence bounds):
%        p1 =       113.5  (102.6, 124.5)
%        p2 =        -803  (-1037, -569.2)
% 
% Goodness of fit:
%   SSE: 9.044e+04
%   R-square: 0.9838
%   Adjusted R-square: 0.982
%   RMSE: 100.2


p1 = 113.5;
p2 = -803;
f = p1*Size+p2;

figure(1)
hold on

plot(Size,Total_operacoes,'b.-','LineWidth',1,'MarkerSize',10)
plot(Size,f,'r.-','LineWidth',1,'MarkerSize',10)
ylabel('Operações')
xlabel('Nº vertices (V)')
legend('Randomized','y = 113.5 x V - 803, (R^2 = 0.98)','Location','northwest','FontSize',12)
title('Complexidade Computacional')
axis([10 30 300 2700])