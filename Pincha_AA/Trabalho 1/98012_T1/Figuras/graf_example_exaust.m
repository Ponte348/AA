clear all
close all
clc

coord = [[20, 20], [13, 4], [20, 1], [11, 7], [1, 9], [6, 2], [19, 1], [4, 1], [20, 9], [4, 18]];

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

x7 = coord(15);
y7 = coord(16);

x8 = coord(17);
y8 = coord(18);

x9 = coord(19);
y9 = coord(20);

% D_set = {9, 4};

%Edges =[(0, 3), (0, 9), (1, 2), (1, 7), (1, 9), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), 
% (3, 9), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 9), (6, 8), (7, 9)]

e03_x = [x0,x3];
e03_y = [y0, y3];

e09_x = [x0,x9];
e09_y = [y0, y9];

e12_x = [x1,x2];
e12_y = [y1, y2];

e17_x = [x1,x7];
e17_y = [y1, y7];

e19_x = [x1,x9];
e19_y = [y1, y9];

e23_x = [x2,x3];
e23_y = [y2, y3];

e24_x = [x2,x4];
e24_y = [y2, y4];

e25_x = [x2,x5];
e25_y = [y2, y5];

e26_x = [x2,x6];
e26_y = [y2, y6];

e27_x = [x2,x7];
e27_y = [y2, y7];

e34_x = [x3,x4];
e34_y = [y3, y4];

e35_x = [x3,x5];
e35_y = [y3, y5];

e39_x = [x3,x9];
e39_y = [y3, y9];

e45_x = [x4,x5];
e45_y = [y4, y5];

e46_x = [x4,x6];
e46_y = [y4, y6];


e47_x = [x4,x7];
e47_y = [y4, y7];

e48_x = [x4,x8];
e48_y = [y4, y8];

e49_x = [x4,x9];
e49_y = [y4, y9];

e56_x = [x5,x6];
e56_y = [y5, y6];

e57_x = [x5,x7];
e57_y = [y5, y7];

e59_x = [x5,x9];
e59_y = [y5, y9];

e68_x = [x6,x8];
e68_y = [y6, y8];

e79_x = [x7,x9];
e79_y = [y7, y7];


%Edges =[(0, 3), (0, 9), (1, 2), (1, 7), (1, 9), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), 
% (3, 9), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 9), (6, 8), (7, 9)]

figure(1)
hold on
plot(e03_x,e03_y,'k.-','MarkerSize',20)
plot(e09_x,e09_y,'k.-','MarkerSize',20)
plot(e12_x,e12_y,'k.-','MarkerSize',20)
plot(e17_x,e17_y,'k.-','MarkerSize',20)
plot(e23_x,e23_y,'k.-','MarkerSize',20)
plot(e24_x,e24_y,'k.-','MarkerSize',20)
plot(e25_x,e25_y,'k.-','MarkerSize',20)
plot(e26_x,e26_y,'k.-','MarkerSize',20)
plot(e27_x,e27_y,'k.-','MarkerSize',20)
plot(e34_x,e34_y,'k.-','MarkerSize',20)
plot(e35_x,e35_y,'k.-','MarkerSize',20)
plot(e39_x,e39_y,'k.-','MarkerSize',20)
plot(e45_x,e45_y,'k.-','MarkerSize',20)
plot(e46_x,e46_y,'k.-','MarkerSize',20)
plot(e47_x,e47_y,'k.-','MarkerSize',20)
plot(e48_x,e48_y,'k.-','MarkerSize',20)
plot(e49_x,e49_y,'k.-','MarkerSize',20)
plot(e56_x,e56_y,'k.-','MarkerSize',20)
plot(e57_x,e57_y,'k.-','MarkerSize',20)
plot(e59_x,e59_y,'k.-','MarkerSize',20)
plot(e68_x,e68_y,'k.-','MarkerSize',20)
plot(e79_x,e79_y,'k.-','MarkerSize',20)
plot(x4,y4,'g.', 'MarkerSize',20)
plot(x9,y9,'g.', 'MarkerSize',20)
axis([0 20 0 20])
xlabel('x')
ylabel('y')
title('V = 10 - K = 0.25 - P = 0.5')