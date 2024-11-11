clear all
close all
clc

% E -> Exaustivo
% H -> Heuristico
% C -> Randomized

% N combinações = min(N_comb, 1000)
% P = 0.125
Size          =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
Ks_solution_E =[0, 0, 5, 5, 5, 6, 5, 5, 5, 5, 5, 6, 6, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8];
Ks_solution_H =[0, 0, 5, 5, 5, 6, 5, 5, 6, 6, 6, 6, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8];
Ks_solution_C =[0, 0, 5, 5, 5, 6, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 7, 8, 8, 9, 8, 9, 9, 9, 10, 11];


count_C = 0;
count_H = 0;
idx = 1;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;


% P = 0.25
Ks_solution_E =[0, 3, 4, 3, 3, 4, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 5, 5, 5, 5, 5, 5, 5];
Ks_solution_H =[0, 4, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5];
Ks_solution_C =[0, 3, 4, 3, 3, 4, 3, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 7, 6, 7, 7, 6, 5, 6];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;


% P = 0.50
Ks_solution_E =[2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3];
Ks_solution_H =[2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3];
Ks_solution_C =[2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 3, 3, 3, 3, 3];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;

% P = 0.75
Ks_solution_E =[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
Ks_solution_H =[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
Ks_solution_C =[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;

%%
clear all
close all
clc
% N combinações min(N_comb, 100)
% P = 0.125
Size          =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
Ks_solution_E =[0, 0, 5, 5, 5, 6, 5, 5, 5, 5, 5, 6, 6, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8];
Ks_solution_H =[0, 0, 5, 5, 5, 6, 5, 5, 6, 6, 6, 6, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8];
Ks_solution_C =[0, 0, 5, 5, 5, 6, 5, 5, 6, 6, 7, 7, 7, 8, 7, 8, 8, 8, 8, 8, 9, 11, 8, 11, 11, 10, 11];


count_C = 0;
count_H = 0;
idx = 1;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;


% P = 0.25
Ks_solution_E = [0, 3, 4, 3, 3, 4, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 5, 5, 5, 5, 5, 5, 5];
Ks_solution_H = [0, 4, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5];
Ks_solution_C =[0, 4, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5, 4, 6, 6, 8, 7, 8, 6, 7, 8, 7, 7];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;


% P = 0.50
Ks_solution_E = [2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3];
Ks_solution_H = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3];
Ks_solution_C =[2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 4];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;

% P = 0.75
Ks_solution_E = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
Ks_solution_H = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
Ks_solution_C =[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;



%%
% N combinações min(N_comb, 10)
% P = 0.125
Size          =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
Ks_solution_E =[0, 0, 5, 5, 5, 6, 5, 5, 5, 5, 5, 6, 6, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8];
Ks_solution_H =[0, 0, 5, 5, 5, 6, 5, 5, 6, 6, 6, 6, 7, 8, 8, 7, 8, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8];
Ks_solution_C =[0, 0, 5, 6, 5, 6, 6, 7, 6, 7, 7, 8, 8, 9, 9, 8, 11, 10, 10, 11, 12, 11, 11, 13, 12, 11, 13];


count_C = 0;
count_H = 0;
idx = 1;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;


% P = 0.25
Ks_solution_E = [0, 3, 4, 3, 3, 4, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 5, 5, 5, 5, 5, 5, 5];
Ks_solution_H = [0, 4, 4, 3, 3, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5];
Ks_solution_C =[0, 4, 4, 3, 3, 4, 3, 5, 7, 4, 5, 6, 5, 6, 5, 7, 7, 6, 7, 10, 8, 11, 8, 10, 8, 10, 8];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;


% P = 0.50
Ks_solution_E = [2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3];
Ks_solution_H = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3];
Ks_solution_C =[2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 2, 3, 4, 4, 3, 2, 3, 3, 5, 4, 4, 4, 4, 4, 5, 3, 3];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;

% P = 0.75
Ks_solution_E = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
Ks_solution_H = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
Ks_solution_C =[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3];


count_C = 0;
count_H = 0;
for i =1:length(Ks_solution_E)
    if Ks_solution_E(i) < Ks_solution_C(i)
        count_C = count_C + 1;
    end
    if Ks_solution_E(i) < Ks_solution_H(i)
        count_H = count_H + 1;
    end
end

nC(idx) = count_C;
nH(idx) = count_H;
idx = idx + 1;














