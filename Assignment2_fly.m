clc
clear
close all
x1 = csvread('항공통계.csv');
x2 = csvread('항공통계.csv');
x1 = x1(133:141,3);
x2 = x2(283:291,3);
x1_avg = mean(x1);
x2_avg = mean(x2);

air = [mean(x1);mean(x2)];
x1_label = ["inland";"jeju"]

bar(air)
set(gca, 'XTickLabel', x1_label); 

grid on