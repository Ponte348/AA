clear all
close all
clc

coord = [[10, 19], [5, 17], [17, 20], [11, 10], [14, 15], [18, 1]];

x0 = 10;
y0 = 19;

x1 = 5;
y1 = 17;

x2 = 17;
y2 = 20;

x3 = 11;
y3 = 10;

x4 = 14;
y4 = 15;

x5 = 18;
y5 = 1;

% D_set = {0, 1, 2};

%Edges = [(0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

e02_x = [x0,x2];
e02_y = [y0, y2];

e03_x = [x0,x3];
e03_y = [y0, y3];

e04_x = [x0,x4];
e04_y = [y0, y4];

e05_x = [x0,x5];
e05_y = [y0, y5];

e12_x = [x1,x2];
e12_y = [y1, y2];

e23_x = [x2,x3];
e23_y = [y2, y3];

e24_x = [x0,x2];
e24_y = [y0, y2];

e25_x = [x2,x5];
e25_y = [y2, y5];

e34_x = [x3,x4];
e34_y = [y3, y4];

e35_x = [x3,x5];
e35_y = [y3, y5];

e45_x = [x4,x5];
e45_y = [y4, y5];



figure(1)
hold on
plot(e02_x,e02_y,'k.-')
plot(e03_x,e03_y,'k.-')
plot(e04_x,e04_y,'k.-')
plot(e05_x,e05_y,'k.-')
plot(e12_x,e12_y,'k.-')
plot(e23_x,e23_y,'k.-')
plot(e24_x,e24_y,'k.-')
plot(e25_x,e25_y,'k.-')
plot(e34_x,e34_y,'k.-')
plot(e35_x,e35_y,'k.-')
plot(e45_x,e45_y,'k.-')
plot(x0,y0,'g.', 'MarkerSize',20)
plot(x1,y1,'g.', 'MarkerSize',20)
plot(x2,y2,'g.', 'MarkerSize',20)
plot(x3,y3,'k.', 'MarkerSize',20)
plot(x4,y4,'k.', 'MarkerSize',20)
plot(x5,y5,'k.', 'MarkerSize',20)
axis([2 20 0 25])
xlabel('x')
ylabel('y')
title('V = 6 - K = 0.5 - P = 0.75')