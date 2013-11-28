function [f,l,r,t,b]=mapcrop(f)
    [X,map] = imread(f);
    I = ind2rgb(X,map);
    I2 = imcrop(I,[1 1 size(I,1) size(I,2)-50]);
    [l,r,t,b]=mapedgecheck(I2);
    f=[f(1:end-4) 'cropped.png'];
    imwrite(I2,f);
end