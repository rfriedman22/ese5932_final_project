clear all;
close all;

% Size of the region of interest
L = 0.06144

% No of pixels in each direction
npixels = 256;
% Pixel size
pixel_size = L/npixels;

% Number of Views
nviews = 90;
% Angle increment between views (unit:degree)
dtheta = 5/12;

%Views
views = [0:nviews-1]*dtheta;

% Number of rays for each views
nrays= 512;

% Distance between first and last ray (unit pixels)
d = npixels*(nrays-1)/nrays;

% Construct imaging operator (unit:pixels)
A = paralleltomo(npixels, views, nrays, d);

% Rescale A to physical units ( unit : mm)
A = A*pixel_size;

%filename = 'C:\Users\Kaushik Dutta\Desktop\A90.mat';
%save( filename, 'A' );
