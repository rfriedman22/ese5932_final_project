clear all
close all
load('C:\Users\Kaushik Dutta\Downloads\project_data.mat')  % Location of the file

% Defining for 270 views
a = 1;
for i=1:2:540
    sinogram270(:,a) = sinogram(:,i);
    a = a + 1;
end

% Defining for 90 views
a = 1;
for i=1:6:540
    sinogram90(:,a) = sinogram(:,i);
    a = a + 1;
end

filename1 = 'C:\Users\Kaushik Dutta\Desktop\Sinogram270.mat';
save( filename1, 'sinogram270' );

filename2 = 'C:\Users\Kaushik Dutta\Desktop\Sinogram90.mat';
save( filename2, 'sinogram90' );


