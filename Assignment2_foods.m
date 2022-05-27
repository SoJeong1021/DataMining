clc
clear
close all


x1 = csvread('housing.csv');

x1 = x1(1:end,2:5);

plot(x1, 'b+')

grid on

xlabel('floor')
ylabel('price')

x_floor = x1(1:end,1);
x_price = x1(1:end,4);

cov_ap = ((x_floor-mean(x_floor))'*(x_price-mean(x_price)))/length(x_price)
var_a = ((x_floor-mean(x_floor))'*(x_floor-mean(x_floor)))/length(x_floor)
var_p = ((x_price-mean(x_price))'*(x_price-mean(x_price)))/length(x_price)

corr_c = cov_ap/sqrt(var_a*var_p)
