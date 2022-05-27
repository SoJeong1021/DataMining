clc
clear
close all

x1 = csvread('netflix.csv');
x1 = x1(2:2001,1:2);

x_dateAdded = x1(1:2000,1);
x_releaseYear = x1(1:2000,2);

cov_ap = ((x_dateAdded-mean(x_dateAdded))'*(x_releaseYear-mean(x_releaseYear)))/length(x_releaseYear)
var_a = ((x_dateAdded-mean(x_dateAdded))'*(x_dateAdded-mean(x_dateAdded)))/length(x_dateAdded)
var_p = ((x_releaseYear-mean(x_releaseYear))'*(x_releaseYear-mean(x_releaseYear)))/length(x_releaseYear)

corr_c = cov_ap/sqrt(var_a*var_p)

