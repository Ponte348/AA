clear all
close all
clc

% Nº of letters: 1000
% Exact counter time: 0.010391500080004334 (s)
% Probabilistic counter time: 0.08799570007249713 (s)
% Lossy counter time: 0.0014136999379843473 (s)
% 
% Nº of letters: 10000
% Exact counter time: 0.02097980002872646 (s)
% Probabilistic counter time: 0.7766457000980154 (s)
% Lossy counter time: 0.004415000090375543 (s)
% 
% Nº of letters: 100000
% Exact counter time: 0.04281929996795952 (s)
% Probabilistic counter time: 6.720932199968956 (s)
% Lossy counter time: 0.060293099959380925 (s)
% 
% Nº of letters: 1000000
% Exact counter time: 0.297984900069423 (s)
% Probabilistic counter time: 71.85790770000312 (s)
% Lossy counter time: 0.59488769993186 (s)
% 
% Nº of letters: 10000000
% Exact counter time: 2.6432206999743357 (s)
% Probabilistic counter time: 667.4582836999325 (s)
% Lossy counter time: 4.5411697999807075 (s)
% 
% Nº of letters: 100000000
% Exact counter time: 24.851058100000955 (s)
% Probabilistic counter time: 6506.611075599911 (s)
% Lossy counter time: 41.674260600004345 (s)

N_letters = [10^3, 10^4, 10^5, 10^6, 10^7, 10^8];

exact_time = [0.010391500080004334, 0.02097980002872646, 0.04281929996795952, 0.297984900069423, 2.6432206999743357, 24.851058100000955];

% Linear model Poly1:
%      f(x) = p1*x + p2
% Coefficients (with 95% confidence bounds):
%        p1 =   2.481e-07  (2.462e-07, 2.501e-07)
%        p2 =     0.04944  (-0.03157, 0.1305)
% 
% Goodness of fit:
%   SSE: 0.01627
%   R-square: 1
%   Adjusted R-square: 1
%   RMSE: 0.06378



p1 = 2.481e-07;
p2 = 0.04944;

f = p1*N_letters + p2;

figure(1)
hold on
plot(N_letters, exact_time,'r.-','LineWidth',1,'MarkerSize',10)
plot(N_letters,f,'b.-','LineWidth',1,'MarkerSize',10)
ylabel('Tempo (s)')
xlabel('Nº letras')
legend('Exact Counter','Exact Counter Linear Fit (R^2:1.0)','Location','northwest','FontSize',10)
title('Exact Counter')



prob_time = [0.08799570007249713, 0.7766457000980154, 6.720932199968956, 71.85790770000312, 667.4582836999325, 6506.611075599911];

% Linear model Poly1:
%      f(x) = p1*x + p2
% Coefficients (with 95% confidence bounds):
%        p1 =   6.503e-05  (6.48e-05, 6.526e-05)
%        p2 =       4.611  (-4.889, 14.11)
% 
% Goodness of fit:
%   SSE: 223.7
%   R-square: 1
%   Adjusted R-square: 1
%   RMSE: 7.479

p12 = 6.503e-05;
p22 = 4.611;

f2 = p12*N_letters + p22;

figure(2)
hold on
plot(N_letters, prob_time,'r.-','LineWidth',1,'MarkerSize',10)
plot(N_letters,f2,'b.-','LineWidth',1,'MarkerSize',10)
ylabel('Tempo (s)')
xlabel('Nº letras')
legend('Probabilistic Counter','Probabilistic Counter Linear Fit (R^2:1.0)','Location','northwest','FontSize',10)
title('Probabilistic Counter (1000)')


lossy_time = [0.0014136999379843473, 0.004415000090375543, 0.060293099959380925, 0.59488769993186, 4.5411697999807075, 41.674260600004345];


% Linear model Poly1:
%      f(x) = p1*x + p2
% Coefficients (with 95% confidence bounds):
%        p1 =   4.159e-07  (4.107e-07, 4.211e-07)
%        p2 =      0.1106  (-0.1017, 0.323)
% 
% Goodness of fit:
%   SSE: 0.1118
%   R-square: 0.9999
%   Adjusted R-square: 0.9999
%   RMSE: 0.1671


p13 = 4.159e-07;
p23 = 0.1106;

f3 = p13*N_letters + p23;

figure(3)
hold on
plot(N_letters, lossy_time,'r.-','LineWidth',1,'MarkerSize',10)
plot(N_letters,f3,'b.-','LineWidth',1,'MarkerSize',10)
ylabel('Tempo (s)')
xlabel('Nº letras')
legend('Lossy Counter','Lossy Counter Linear Fit (R^2:0.99)','Location','northwest','FontSize',10)
title('Lossy Counter (0.01)')

