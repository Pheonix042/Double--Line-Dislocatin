clear all;
clf;
x=[6:64];
y=[5:34];
load van.txt
surf(x,y,van);
title('VanDar energy ','Color','r','FontSize',24)
xlabel('Position in X direction','FontSize',18,'Color','b')
ylabel('Position in Y direction','FontSize',18,'Color','b')
zlabel('VanDar wahl Energy(kcal/mole)','FontSize',18,'Color','b')
hold on
colorbar