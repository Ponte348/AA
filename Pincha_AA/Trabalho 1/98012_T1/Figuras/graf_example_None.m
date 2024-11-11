clear all
close all
clc

coord = [[11, 13], [12, 8], [10, 12], [1, 10], [16, 0], [4, 5], [19, 4]];

x0 = coord(1);
y0 = coord(2);

x1 = coord(3);
y1 = coord(4);

x2 = coord(5);
y2 = coord(6);

x3 = coord(7);
y3 = coord(8);

x4 = coord(9);
y4 = coord(10);

x5 = coord(11);
y5 = coord(12);

x6 = coord(13);
y6 = coord(14);

% D_set = {9, 4};

%Edges =[(0, 3), (1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)]

e03_x = [x0,x3];
e03_y = [y0, y3];

e12_x = [x1,x2];
e12_y = [y1, y2];

e23_x = [x2,x3];
e23_y = [y2, y3];

e24_x = [x2,x4];
e24_y = [y2, y4];

e25_x = [x2,x5];
e25_y = [y2, y5];

e26_x = [x2,x6];
e26_y = [y2, y6];

e34_x = [x3,x4];
e34_y = [y3, y4];

e35_x = [x3,x5];
e35_y = [y3, y5];

e45_x = [x4,x5];
e45_y = [y4, y5];

e46_x = [x4,x6];
e46_y = [y4, y6];

e56_x = [x5,x6];
e56_y = [y5, y6];


figure(1)
hold on
plot(e03_x,e03_y,'k.-','MarkerSize',20)
plot(e12_x,e12_y,'k.-','MarkerSize',20)
plot(e23_x,e23_y,'k.-','MarkerSize',20)
plot(e24_x,e24_y,'k.-','MarkerSize',20)
plot(e25_x,e25_y,'k.-','MarkerSize',20)
plot(e26_x,e26_y,'k.-','MarkerSize',20)
plot(e34_x,e34_y,'k.-','MarkerSize',20)
plot(e35_x,e35_y,'k.-','MarkerSize',20)
plot(e45_x,e45_y,'k.-','MarkerSize',20)
plot(e46_x,e46_y,'k.-','MarkerSize',20)
plot(e56_x,e56_y,'k.-','MarkerSize',20)
axis([0 20 0 20])
xlabel('x')
ylabel('y')
title('V = 7 - K = 0.25 - P = 0.5')