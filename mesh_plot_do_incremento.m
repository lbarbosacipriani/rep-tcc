clear all;close all;clc
[x,y] = meshgrid(0.1:.1:5);
th=60;
K=20;
xinc=(x+K);%./sqrt(x.^2 + y.^2);
yinc=(y+K);%./sqrt(x.^2 + y.^2);
z=sqrt(xinc^2 +yinc^2);
surf(x,y,z)
%s.FaceColor = 'flat';