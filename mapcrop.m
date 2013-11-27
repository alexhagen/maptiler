function [f]=mapcrop(f)
    [X,map] = imread(f);
    I = ind2rgb(X,map);
    I2 = imcrop(I,[1 1 1280 1230]);
    imwrite(I2,[f(1:end-4) 'cropped.png']);
end