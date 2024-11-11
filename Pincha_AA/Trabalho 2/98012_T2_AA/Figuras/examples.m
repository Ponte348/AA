clear all
close all
clc

%%% Heuristico e Randomized retornaram falsos conjuntos mínimos

% [[13, 3], [3, 19], [5, 0], [13, 12], [14, 3], [4, 18], [9, 4], [4, 4], [2, 14], [13, 2], [3, 0], [20, 20], [8, 13], [15, 7]]
% [(0, 6), (1, 9), (1, 11), (1, 13), (2, 9), (3, 7), (4, 5), (4, 13), (6, 11), (6, 12), (7, 10)]
% Exaustive
% K = 5 ; Result Exaustive: {4, 6, 7, 8, 9}
% Heuristico
% K = 6 ; Result Heuristic: {0, 4, 6, 7, 8, 9}
% Randomized
% K = 6 ; Result Randomized: {5, 6, 7, 8, 9, 13}
%%%

x0 = 13; y0 = 5;
x1 = 3; y1 = 19;
x2 = 5; y2 = 1;
x3 = 13; y3 = 12;
x4 = 14; y4 = 3;
x5 = 4; y5 = 18;
x6 = 9; y6 = 4;
x7 = 4; y7 = 4;
x8 = 2; y8 = 14;
x9 = 13; y9 = 2;
x10 = 3; y10 = 1;
x11 = 19; y11 = 19;
x12 = 18; y12 = 13;
x13 = 15; y13 = 17;

% [(0, 6), (1, 9), (1, 11), (1, 13), (2, 9), (3, 7), (4, 5), (4, 13), (6, 11), (6, 12), (7, 10)]
e1x = [x0,x6]; e1y = [y0,y6];
e2x = [x1,x9]; e2y = [y1,y9];
e3x = [x1,x11]; e3y = [y1,y11];
e4x = [x1,x13]; e4y = [y1,y13];
e5x = [x2,x9]; e5y = [y2,y9];
e6x = [x3,x7]; e6y = [y3,y7];
e7x = [x4,x5]; e7y = [y4,y5];
e8x = [x4,x13]; e8y = [y4,y13];
e9x = [x6,x11]; e9y = [y6,y11];
e10x = [x6,x12]; e10y = [y6,y12];
e11x = [x7,x10]; e11y = [y7,y10];



figure(1)
hold on
% Vértices
plot(x0,y0,'k.', 'MarkerSize',20)
plot(x1,y1,'k.', 'MarkerSize',20)
plot(x2,y2,'k.', 'MarkerSize',20)
plot(x3,y3,'k.', 'MarkerSize',20)
plot(x4,y4,'k.', 'MarkerSize',20)
plot(x5,y5,'k.', 'MarkerSize',20)
plot(x6,y6,'k.', 'MarkerSize',20)
plot(x7,y7,'k.', 'MarkerSize',20)
plot(x8,y8,'k.', 'MarkerSize',20)
plot(x9,y9,'k.', 'MarkerSize',20)
plot(x10,y10,'k.', 'MarkerSize',20)
plot(x11,y11,'k.', 'MarkerSize',20)
plot(x12,y12,'k.', 'MarkerSize',20)
plot(x13,y13,'k.', 'MarkerSize',20)
% Edges
plot(e1x,e1y,'k.-')
plot(e2x,e2y,'k.-')
plot(e3x,e3y,'k.-')
plot(e4x,e4y,'k.-')
plot(e5x,e5y,'k.-')
plot(e6x,e6y,'k.-')
plot(e7x,e7y,'k.-')
plot(e8x,e8y,'k.-')
plot(e9x,e9y,'k.-')
plot(e10x,e10y,'k.-')
plot(e11x,e11y,'k.-')
% K = 5 ; Result Exaustive: {4, 6, 7, 8, 9}
plot(x4,y4,'g.', 'MarkerSize',20)
plot(x6,y6,'g.', 'MarkerSize',20)
plot(x7,y7,'g.', 'MarkerSize',20)
plot(x8,y8,'g.', 'MarkerSize',20)
plot(x9,y9,'g.', 'MarkerSize',20)
% K = 6 ; Result Heuristic: {0, 4, 6, 7, 8, 9}
plot(x0,y0,'ro', 'MarkerSize',15)
plot(x4,y4,'ro', 'MarkerSize',15)
plot(x6,y6,'ro', 'MarkerSize',15)
plot(x7,y7,'ro', 'MarkerSize',15)
plot(x8,y8,'ro', 'MarkerSize',15)
plot(x9,y9,'ro', 'MarkerSize',15)
% K = 6 ; Result Randomized: {5, 6, 7, 8, 9, 13}
plot(x5,y5,'bo', 'MarkerSize',20)
plot(x6,y6,'bo', 'MarkerSize',20)
plot(x7,y7,'bo', 'MarkerSize',20)
plot(x8,y8,'bo', 'MarkerSize',20)
plot(x9,y9,'bo', 'MarkerSize',20)
plot(x13,y13,'bo', 'MarkerSize',20)

legend('','','','','','','','','','','','','','','','','','','','','','','','','','','','Resultado Exaustivo','','','','','Resultado Heurístico','','','','','','','Resultado Randomized','Location','northwest')

axis([0 20 0 25])
xlabel('x')
ylabel('y')
title('V = 14 - P = 0.125')


%% Heuristico e Randomized retornaram verdadeiros conjuntos mínimos


clear all
close all
clc

% [[13, 3], [3, 19], [5, 0], [13, 12], [14, 3], [4, 18], [9, 4], [4, 4], [2, 14], [13, 2]]
% [(0, 6), (1, 9), (2, 9), (3, 7), (4, 5)]
% Exaustive
% K = 5 ; Result Exaustive: {0, 3, 4, 8, 9}
% Heuristico
% K = 5 ; Result Heuristic: {0, 3, 4, 8, 9}
% Randomized
% K = 5 ; Result Randomized: {0, 5, 7, 8, 9}


x0 = 11; y0 = 3;
x1 = 3; y1 = 19;
x2 = 5; y2 = 1;
x3 = 13; y3 = 12;
x4 = 14; y4 = 3;
x5 = 4; y5 = 18;
x6 = 9; y6 = 4;
x7 = 4; y7 = 4;
x8 = 3; y8 = 14;
x9 = 13; y9 = 12;

% [(0, 6), (1, 9), (2, 9), (3, 7), (4, 5)]
e1x = [x0,x6]; e1y = [y0,y6];
e2x = [x1,x9]; e2y = [y1,y9];
e3x = [x2,x9]; e3y = [y2,y9];
e4x = [x3,x7]; e4y = [y3,y7];
e5x = [x4,x5]; e5y = [y4,y5];



figure(1)
hold on
% Vértices
plot(x0,y0,'k.', 'MarkerSize',20)
plot(x1,y1,'k.', 'MarkerSize',20)
plot(x2,y2,'k.', 'MarkerSize',20)
plot(x3,y3,'k.', 'MarkerSize',20)
plot(x4,y4,'k.', 'MarkerSize',20)
plot(x5,y5,'k.', 'MarkerSize',20)
plot(x6,y6,'k.', 'MarkerSize',20)
plot(x7,y7,'k.', 'MarkerSize',20)
plot(x8,y8,'k.', 'MarkerSize',20)
plot(x9,y9,'k.', 'MarkerSize',20)
% Edges
plot(e1x,e1y,'k.-')
plot(e2x,e2y,'k.-')
plot(e3x,e3y,'k.-')
plot(e4x,e4y,'k.-')
plot(e5x,e5y,'k.-')
% K = 5 ; Result Exaustive: {0, 3, 4, 8, 9}
plot(x0,y0,'g.', 'MarkerSize',20)
plot(x3,y3,'g.', 'MarkerSize',20)
plot(x4,y4,'g.', 'MarkerSize',20)
plot(x8,y8,'g.', 'MarkerSize',20)
plot(x9,y9,'g.', 'MarkerSize',20)
% K = 5 ; Result Heuristic: {0, 3, 4, 8, 9}
plot(x0,y0,'ro', 'MarkerSize',15)
plot(x3,y3,'ro', 'MarkerSize',15)
plot(x4,y4,'ro', 'MarkerSize',15)
plot(x8,y8,'ro', 'MarkerSize',15)
plot(x9,y9,'ro', 'MarkerSize',15)
%K = 5 ; Result Randomized: {0, 5, 7, 8, 9}
plot(x0,y0,'bo', 'MarkerSize',20)
plot(x5,y5,'bo', 'MarkerSize',20)
plot(x7,y7,'bo', 'MarkerSize',20)
plot(x8,y8,'bo', 'MarkerSize',20)
plot(x9,y9,'bo', 'MarkerSize',20)

legend('','','','','','','','','','','','','','','','','','','','Resultado Exaustivo','','','','','Resultado Heurístico','','','','Resultado Randomized')


axis([2 15 0 20])
xlabel('x')
ylabel('y')
title('V = 10 - P = 0.125')

%% SWtinyG

clear all
close all
clc


x0 = 13; y0 = 3;
x1 = 3; y1 = 19;
x2 = 6; y2 = 5;
x3 = 15; y3 = 12;
x4 = 16; y4 = 3;
x5 = 6; y5 = 18;
x6 = 9; y6 = 1;
x7 = 4; y7 = 4;
x8 = 2; y8 = 14;
x9 = 15; y9 = 7;
x10 = 3; y10 = 1;
x11 = 19; y11 = 19;
x12 = 11; y12 = 13;


e1x = [x0,x5]; e1y = [y0,y5];
e2x = [x4,x3]; e2y = [y4,y3];
e3x = [x1,x0]; e3y = [y1,y0];
e4x = [x9,x12]; e4y = [y9,y12];
e5x = [x6,x4]; e5y = [y6,y4];
e6x = [x5,x4]; e6y = [y5,y4];
e7x = [x0,x2]; e7y = [y0,y2];
e8x = [x11,x12]; e8y = [y11,y12];
e9x = [x9,x10]; e9y = [y9,y10];
e10x = [x0,x6]; e10y = [y0,y6];
e11x = [x7,x8]; e11y = [y7,y8];
e12x = [x9,x11]; e12y = [y9,y11];
e13x = [x5,x3]; e13y = [y5,y3];



figure(1)
hold on
% Vértices
plot(x0,y0,'k.', 'MarkerSize',20)
plot(x1,y1,'k.', 'MarkerSize',20)
plot(x2,y2,'k.', 'MarkerSize',20)
plot(x3,y3,'k.', 'MarkerSize',20)
plot(x4,y4,'k.', 'MarkerSize',20)
plot(x5,y5,'k.', 'MarkerSize',20)
plot(x6,y6,'k.', 'MarkerSize',20)
plot(x7,y7,'k.', 'MarkerSize',20)
plot(x8,y8,'k.', 'MarkerSize',20)
plot(x9,y9,'k.', 'MarkerSize',20)
plot(x10,y10,'k.', 'MarkerSize',20)
plot(x11,y11,'k.', 'MarkerSize',20)
plot(x12,y12,'k.', 'MarkerSize',20)
% Edges
plot(e1x,e1y,'k.-')
plot(e2x,e2y,'k.-')
plot(e3x,e3y,'k.-')
plot(e4x,e4y,'k.-')
plot(e5x,e5y,'k.-')
plot(e6x,e6y,'k.-')
plot(e7x,e7y,'k.-')
plot(e8x,e8y,'k.-')
plot(e9x,e9y,'k.-')
plot(e10x,e10y,'k.-')
plot(e11x,e11y,'k.-')
% K = 4 ; Result Heuristic: {0, 9, 3, 7}
plot(x0,y0,'g.', 'MarkerSize',20)
plot(x9,y9,'g.', 'MarkerSize',20)
plot(x3,y3,'g.', 'MarkerSize',20)
plot(x7,y7,'g.', 'MarkerSize',20)
% K = 4 ; Result Randomized: {0, 9, 3, 7}}
plot(x0,y0,'bo', 'MarkerSize',15)
plot(x9,y9,'bo', 'MarkerSize',15)
plot(x3,y3,'bo', 'MarkerSize',15)
plot(x7,y7,'bo', 'MarkerSize',15)

legend('','','','','','','','','','','','','','','','','','','','','','','','','','','','Resultado Exaustivo','','','','Resultado Randomized','Location','northwest')

axis([0 20 0 25])
xlabel('x')
ylabel('y')
title('SW tiny Graph')
