function [f]=mapcrop(f)
    [X,map] = imread(f);
    I = ind2rgb(X,map);
    I2 = imcrop(I,[1 1 1280 1230]);
    mapedgecheck(I2);
    f=[f(1:end-4) 'cropped.png'];
    imwrite(I2,f);
end