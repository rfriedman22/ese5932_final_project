clear all;
close all;
load data/project_data.mat;

% Size of the region of interest
L = 0.06144;

% No of pixels in each direction
npixels = 256;
% Pixel size
pixel_size = L/npixels;

% Number of Views
nviews = 540;
% Angle increment between views (unit:degree)
dtheta = 5/12;

% Number of rays for each views
nrays= 512;

% Distance between first and last ray (unit pixels)
d = npixels*(nrays-1)/nrays;

% Set how much to subset the data
subviews = [90 270 540];
for i = [1:length(subviews)]
    nsubviews = subviews(i);
    step_size = nviews / nsubviews;
    theta = dtheta * step_size;
    views = [0:nsubviews-1]*theta;
    
    % Construct imaging operator (unit:pixels)
    A = paralleltomo(npixels, views, nrays, d);

    % Rescale A to physical units ( unit : mm)
    A = A*pixel_size; 
    
    filename = append('./data/A', int2str(nsubviews), '.mat');
    save(filename, 'A');
    
    % Generate the subsetted sinogram
    a = 1;
    for i=1:step_size:nviews
        sino(:, a) = sinogram(:, i);
        a = a + 1;
    end
    
    filename = append('./data/sinogram', int2str(nsubviews), '.mat');
    save(filename, 'sino');
end
