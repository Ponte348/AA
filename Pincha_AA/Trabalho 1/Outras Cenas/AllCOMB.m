clear all
close all
clc


P = 0.125;
K =0.75;

Size =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]; %K =0.75; %P =0.125;
Op_Exaustive =[32, 150, 270, 7, 8, 36, 30, 55, 12, 13, 14, 15, 16, 68, 54, 38, 20, 21, 22, 23, 24, 25];
Op_Heuristic =[24, 90, 180, 7, 8, 36, 30, 55, 12, 13, 14, 15, 16, 68, 54, 38, 20, 21, 22, 23, 24, 25];
Op_ALLExaustive =[192, 560, 1122, 2107, 3736, 10899, 11170, 17908, 32844, 50284, 74774, 212520, 326528, 1123241, 1688526, 1066907, 3614460, 5135466, 7181812, 11061367, 15139416, 22613600];

Op_ALLExaustive(6) = nan;
Op_ALLExaustive(15:19) = nan;

c = 1;
for j=1:length(Op_ALLExaustive)
    if  isnan(Op_ALLExaustive(j)) == false
        Op(c) = Op_ALLExaustive(j);
        x2(c) = Size(j);
        c = c + 1;
    end
end

Op = Op(1:12);
x2 = x2(1:12);


% General model:
%      f(x) = (a*x^2)*b*2^x+c
% Coefficients (with 95% confidence bounds):
%        a =     0.01912  (-8.35e+05, 8.35e+05)
%        b =       1.464  (-6.392e+07, 6.392e+07)
%        c =      0.9609  (-3.824e+04, 3.824e+04)

a =     0.01912;
b =       1.464;
c =      0.9609;
fit = (a.*x2.^2).*b.*2.^x2+c;

str = 'a = 0.01912';
text(6,4*10E5,str)
text(6,5*10E5,str)

figure(1)
hold on
plot(x2,Op,'r.-','LineWidth',1,'MarkerSize',10)
plot(x2,fit,'.-','Color',[0.9290 0.6940 0.1250],'LineWidth',1.5,'MarkerSize',10)
ylabel('Operações')
xlabel('Nº vertices (V)')
legend('Exaustive All Combinations','(a*V^2) * b*2^V + c','Location','northwest')
%axis([4 17 2 20])
title(['P = ',num2str(P), ', K = ',num2str(K)])
subtitle('a = 0.01912, b = 1.464, c = 0.9609')

figure(2)
hold on
plot(Size,log(Op_Heuristic),'b.-','LineWidth',1,'MarkerSize',10)
plot(x2,log(Op),'r.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Op_Exaustive),'k.-','LineWidth',1,'MarkerSize',10)
ylabel('log(Operações)')
xlabel('Nº vertices (V)')
legend('Heuristic','Exaustive All Combinations','Exaustive','Location','northwest')
axis([4 16 2 20])
title(['P = ',num2str(P), ', K = ',num2str(K)])




