function [fuzzyf,f]=mapfuzzymaker(f)
    I=imread(f);
    I=imresize(I, 0.6);
    %Create White Strips around the border
    I(:,1:15,:)=255;
    I(1:15,:,:)=255;
    I(:,end-15:end,:)=255;
    I(end-15:end,:,:)=255;
    %Create Fuzzy Center
    randblock=255*rand(size(I(15:end-15,15:end-15,1)));
    I(15:end-15,15:end-15,1)=randblock;
    I(15:end-15,15:end-15,2)=randblock;
    I(15:end-15,15:end-15,3)=randblock;
    %%Add black lines for crosshair roads
    I(floor(size(I,1)/2)-2:ceil(size(I,1)/2)+2,1:15,:)=0;
    I(1:15,floor(size(I,1)/2)-2:ceil(size(I,1)/2)+2,:)=0;
    I(floor(size(I,1)/2)-2:ceil(size(I,1)/2)+2,end-15:end,:)=0;
    I(end-15:end,floor(size(I,1)/2)-2:ceil(size(I,1)/2)+2,:)=0;
    imshow(I);
    fuzzyf=[f(1:end-4) 'fuzzy.png'];
    imwrite(I,fuzzyf);
end