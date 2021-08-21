clear all;close all;clc
[x,y] = meshgrid(0.05:.05:2);
th=60;
K=20;
xinc=(x+K)./sqrt(x.^2 + y.^2);
yinc=(y+K)./sqrt(x.^2 + y.^2);
z=sqrt(xinc^2 +yinc^2);
mesh(x,y,z)