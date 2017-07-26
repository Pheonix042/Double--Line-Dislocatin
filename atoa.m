clear all;
clf;
x=[6:64];
y=[5:34];
load atoa.txt
surf(x,y,atoa);
title('Angle to angle energy ','Color','r','FontSize',24)
xlabel('Position in X direction','FontSize',18,'Color','b')
ylabel('Position in Y direction','FontSize',18,'Color','b')
zlabel('Angle to angle bend Energy(kcal/mole)','FontSize',18,'Color','b')
hold on
colorbar