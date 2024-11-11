clear all
close all
clc


P = 0.25;

Size =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; %K =0.125; %P =0.25;
Op_Exaustive1 =[20, 30, 42, 56, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 28800, 36992, 46818, 58482, 72200, 88200, 106722, 128018, 1068672, 1322500, 1622400, 1974375, 2384928, 2861082, 3410400];
Op_Heuristic1 =[0, 0, 0, 0, 64, 81, 100, 121, 144, 169, 196, 225, 3600, 4352, 5202, 6156, 7220, 8400, 9702, 11132, 133584, 158700, 187200, 219375, 255528, 295974, 341040];
Times_Exaustive1 =[0.0001419000000169035, 0.00019009999959962443, 0.00019659999998111743, 0.00017250000018975697, 0.0005011999992348137, 0.0006691999997201492, 0.0008218000002671033, 0.0014283000000432367, 0.00156299999980547, 0.0023032000008242903, 0.003922500000044238, 0.005098100000395789, 0.02304089999961434, 0.03219050000006973, 0.04652850000002218, 0.06936399999995047, 0.1065705999999409, 0.16955529999995633, 0.30442579999999, 0.5461805999993885, 1.6580495999996856, 2.740549799999826, 4.831897099999878, 8.872982000000775, 16.79474520000076, 32.67550990000018, 64.61074949999966];
Times_Heuristic1 =[0.0001483999994889018, 0.00013530000069295056, 0.00015840000014577527, 0.0001277999999729218, 0.0002173000002585468, 0.00030750000041734893, 0.0003243000001020846, 0.000522399999681511, 0.0008493000004818896, 0.001323200000115321, 0.0013314999996509869, 0.0029954999999972642, 0.0074388000002727495, 0.012134900000091875, 0.022411900000406604, 0.042591299999912735, 0.08292830000027607, 0.16327369999999064, 0.32677760000024136, 0.6449376999999004, 1.3915426999992633, 2.7625034000002415, 5.740886900000078, 11.106585200000154, 22.479216100000485, 46.76812659999996, 93.29933119999987];
N_Solutions_Exaustive1 =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
N_Solutions_Heuristic1 =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
N_Configurations_Exaustive1 =[5, 6, 7, 8, 64, 81, 100, 121, 144, 169, 196, 225, 1800, 2176, 2601, 3078, 3610, 4200, 4851, 5566, 44528, 52900, 62400, 73125, 85176, 98658, 113680];
N_Configurations_Heuristic1 =[0, 0, 0, 0, 8, 9, 10, 11, 12, 13, 14, 15, 225, 256, 289, 324, 361, 400, 441, 484, 5566, 6348, 7200, 8125, 9126, 10206, 11368];

%Size =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; %K =0.25; %P =0.25;
Op_Exaustive2 =[64, 125, 216, 343, 1568, 2592, 4050, 6050, 26400, 40898, 61152, 88725, 6432, 8143, 10134, 12426, 9960, 12012, 103862, 14704613, 673872, 867100, 1102348, 1386126, 16492, 18531, 20730];
Op_Heuristic2 =[16, 25, 36, 49, 392, 576, 810, 1100, 6600, 9438, 13104, 17745, 6432, 8143, 10134, 12426, 9960, 12012, 103862, 3196655, 673872, 867100, 1102348, 1386126, 16492, 18531, 20730];
Times_Exaustive2 =[0.00024089999988063937, 0.0002455000003465102, 0.00028649999967456097, 0.0004741000002468354, 0.0013263000000733882, 0.0025282000005972805, 0.003365499999745225, 0.005365900000469992, 0.020550899999761896, 0.02690199999960896, 0.04294339999978547, 0.06140469999991183, 0.004930499999318272, 0.006296000000475033, 0.007808899999872665, 0.00964300000032381, 0.009374500000376429, 0.01112340000054246, 0.07934449999993376, 10.877408299999843, 0.4882563000001028, 0.6716249999999491, 0.8349051000004692, 1.0702826999995523, 0.18320660000063071, 0.2418398999998317, 0.30998600000020815];
Times_Heuristic2 =[0.00015919999987090705, 0.00023860000055719865, 0.00018479999926057644, 0.00021019999985583127, 0.00043420000019978033, 0.0005827000004501315, 0.0009592000005795853, 0.001718800000162446, 0.004968599999301659, 0.007411900000079186, 0.010170700000344368, 0.013911700000790006, 0.004816700000446872, 0.005767000000560074, 0.007379799999398529, 0.009428200000002107, 0.00856629999998404, 0.010305300000254647, 0.07906689999981609, 2.891855800000485, 0.4873945999997886, 0.6547331000001577, 0.8182604000003266, 1.0345477999999275, 0.13828240000020742, 0.17637749999994412, 0.22645969999939553];
N_Solutions_Exaustive2 =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1];
N_Solutions_Heuristic2 =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1];
N_Configurations_Exaustive2 =[16, 25, 36, 49, 196, 288, 405, 550, 2200, 3146, 4368, 5915, 402, 479, 563, 654, 498, 572, 4721, 639331, 28078, 34684, 42398, 51338, 589, 639, 691];
N_Configurations_Heuristic2 =[4, 5, 6, 7, 49, 64, 81, 100, 550, 726, 936, 1183, 402, 479, 563, 654, 498, 572, 4721, 138985, 28078, 34684, 42398, 51338, 589, 639, 691];

%Size =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; %K =0.5; %P =0.25;
Op_Exaustive3 =[72, 200, 480, 35, 32, 36, 10, 11, 84, 91, 84, 90, 80, 102, 90, 95, 80, 84, 528, 5635, 4296, 5150, 2990, 3510, 280, 290, 270];
Op_Heuristic3 =[36, 80, 240, 35, 32, 36, 10, 11, 84, 91, 84, 90, 80, 102, 90, 95, 80, 84, 528, 5635, 4296, 5150, 2990, 3510, 280, 290, 270];
Times_Exaustive3 =[0.00020089999998162966, 0.00026699999943957664, 0.00042690000009315554, 0.00017290000050707022, 0.00017019999995682156, 0.00019220000012865057, 0.0001968000005945214, 0.0002238000006400398, 0.00037460000021383166, 0.0005543999996007187, 0.0009119999995164108, 0.0019366000005902606, 0.0029261999998198007, 0.005106000000523636, 0.010965899999973772, 0.01978560000043217, 0.04634020000048622, 0.08258800000021438, 0.1891963999996733, 0.3437273000008645, 0.7665370000004259, 1.357742700000017, 3.02405010000075, 5.358700699999645, 12.46317209999961, 23.130915699999605, 51.979989399999795];
Times_Heuristic3 =[0.00018759999966277974, 0.00020089999998162966, 0.0002875000000130967, 0.00019860000065818895, 0.00017109999953390798, 0.00019149999934597872, 0.00019100000008620555, 0.000224099999286409, 0.0003501999999571126, 0.00045510000018111896, 0.0009037999998326995, 0.001917200000207231, 0.0032403000004705973, 0.005020900000090478, 0.01185280000026978, 0.021917399999438203, 0.04932050000024901, 0.08606830000007903, 0.2083396999996694, 0.381089499999689, 0.8470194999999876, 1.4853102999995826, 3.5289278000000195, 6.239753399999245, 14.293625600000269, 25.62392650000038, 59.298804300000484];
N_Solutions_Exaustive3 =[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
N_Solutions_Heuristic3 =[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
N_Configurations_Exaustive3 =[18, 40, 80, 5, 4, 4, 1, 1, 7, 7, 6, 6, 5, 6, 5, 5, 4, 4, 24, 245, 179, 206, 115, 130, 10, 10, 9];
N_Configurations_Heuristic3 =[9, 16, 40, 5, 4, 4, 1, 1, 7, 7, 6, 6, 5, 6, 5, 5, 4, 4, 24, 245, 179, 206, 115, 130, 10, 10, 9];

%Size =[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; %K =0.75; %P =0.25;
Op_Exaustive4 =[32, 50, 6, 7, 8, 9, 10, 11, 48, 52, 42, 30, 16, 34, 18, 19, 20, 21, 22, 161, 144, 150, 130, 108, 84, 87, 60];
Op_Heuristic4 =[24, 90, 6, 7, 8, 9, 10, 11, 48, 52, 42, 30, 16, 34, 18, 19, 20, 21, 22, 161, 144, 150, 130, 108, 84, 87, 60];
Times_Exaustive4 =[0.00019590000010794029, 0.00019580000025598565, 0.00017289999959757552, 0.00014039999950909987, 0.00016140000025188783, 0.00018369999997958075, 0.00022980000085226493, 0.0003074999995078542, 0.0007714000003034016, 0.0008386999998037936, 0.0018472000001565902, 0.0025611000000935746, 0.004305899999963003, 0.007886000000326021, 0.014686600000459293, 0.028054300000803778, 0.055863099999442056, 0.1161960999997973, 0.23378039999988687, 0.4627247000007628, 0.9365972999994483, 1.8285904000003939, 3.682892699999684, 7.526164300000346, 15.076084199999968, 30.165129900000466, 60.925791100000424];
Times_Heuristic4 =[0.00018249999993713573, 0.00021190000006754417, 0.00018619999991642544, 0.00015170000006037299, 0.00016360000063286861, 0.00021240000023681205, 0.0002395999999862397, 0.00026309999975637766, 0.0007872999995015562, 0.0006837000000814442, 0.0012795000002370216, 0.0023235999997268664, 0.005286999999952968, 0.009302400000706257, 0.0193464000003587, 0.03796890000012354, 0.07594520000020566, 0.15450659999987693, 0.32220219999999244, 0.6401541000004727, 1.3120114000003014, 2.6365338000005067, 5.386664599999676, 11.158193799999935, 22.15459709999959, 45.40050419999989, 92.92425019999973];
N_Solutions_Exaustive4 =[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
N_Solutions_Heuristic4 =[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
N_Configurations_Exaustive4 =[8, 10, 1, 1, 1, 1, 1, 1, 4, 4, 3, 2, 1, 2, 1, 1, 1, 1, 1, 7, 6, 6, 5, 4, 3, 3, 2];
N_Configurations_Heuristic4 =[6, 18, 1, 1, 1, 1, 1, 1, 4, 4, 3, 2, 1, 2, 1, 1, 1, 1, 1, 7, 6, 6, 5, 4, 3, 3, 2];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure(1)
%subplot(1,2,2)
hold on
plot(Size,log(Times_Exaustive1),'b.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Times_Exaustive2),'r.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Times_Heuristic1),'k.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Times_Heuristic2),'m.-','LineWidth',1,'MarkerSize',10)
ylabel('Log(Time)')
xlabel('Nº vertices (V)')
legend('Exaustive K = 0.125','Exaustive K = 0.25','Heuristic K = 0.125','Heuristic K = 0.25','Location','northwest')
title(['P = ',num2str(P)])
axis([4 25 -10 6])
drawnow


figure(2)
%subplot(1,2,1)
hold on
plot(Size,log(Times_Exaustive3),'b.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Times_Exaustive4),'r.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Times_Heuristic3),'k.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Times_Heuristic4),'m.-','LineWidth',1,'MarkerSize',10)
ylabel('Log(Time)')
xlabel('Nº vertices (V)')
legend('Exaustive K = 0.50','Exaustive K = 0.75','Heuristic K = 0.50','Heuristic K = 0.75','Location','northwest')
title(['P = ',num2str(P)])
axis([4 25 -10 6])
drawnow


figure(3)
%subplot(1,2,1)
hold on
plot(Size,log(Op_Exaustive1),'b.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Op_Exaustive2),'r.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Op_Heuristic1),'k.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Op_Heuristic2),'m.-','LineWidth',1,'MarkerSize',10)
ylabel('log(Operações)')
xlabel('Nº vertices (V)')
legend('Exaustive K = 0.125','Exaustive K = 0.25','Heuristic K = 0.125','Heuristic K = 0.25','Location','northwest')
title(['P = ',num2str(P)])
axis([4 25 2 20])
drawnow

figure(4)
%subplot(1,2,2)
hold on
plot(Size,log(Op_Exaustive3),'b.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Op_Exaustive4),'r.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Op_Heuristic3),'k.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(Op_Heuristic4),'m.-','LineWidth',1,'MarkerSize',10)
ylabel('log(Operações)')
xlabel('Nº vertices (V)')
legend('Exaustive K = 0.50','Exaustive K = 0.75','Heuristic K = 0.50','Heuristic K = 0.75','Location','northwest')
title(['P = ',num2str(P)])
axis([4 25 0 18])
drawnow

figure(5)
%subplot(1,2,2)
hold on
plot(Size,log(N_Configurations_Exaustive1),'b.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(N_Configurations_Exaustive2),'r.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(N_Configurations_Heuristic1),'k.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(N_Configurations_Heuristic2),'m.-','LineWidth',1,'MarkerSize',10)
ylabel('log(Configurações)')
xlabel('Nº vertices (V)')
legend('Exaustive K = 0.125','Exaustive K = 0.25','Heuristic K = 0.125','Heuristic K = 0.25','Location','northwest')
title(['P = ',num2str(P)])
axis([4 25 0 18])
drawnow

figure(6)
%subplot(1,2,2)
hold on
plot(Size,log(N_Configurations_Exaustive3),'b.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(N_Configurations_Exaustive4),'r.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(N_Configurations_Heuristic3),'k.-','LineWidth',1,'MarkerSize',10)
plot(Size,log(N_Configurations_Heuristic4),'m.-','LineWidth',1,'MarkerSize',10)
ylabel('log(Configurações)')
xlabel('Nº vertices (V)')
legend('Exaustive K = 0.50','Exaustive K = 0.75','Heuristic K = 0.50','Heuristic K = 0.75','Location','northwest')
title(['P = ',num2str(P)])
axis([4 25 0 18])



