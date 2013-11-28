function [corr_offset,max_cc]=mapxcorr(f,fuzzyf)
    I=imread(f);
    If=imread(fuzzyf);
    I2=double(I(:,:,1));
    If2=double(If(:,:,1));
    cc=xcorr2(I2,If2);
    [max_cc, imax] = max(abs(cc(:)));
    [ypeak, xpeak] = ind2sub(size(cc),imax(1));
    corr_offset = [ (ypeak-size(I2,1)) (xpeak-size(I2,2)) ];
    corr_offset = -corr_offset;
    Iandf=I2;
    Iandf(corr_offset(1)+1:corr_offset(1)+size(If2,1),...
        corr_offset(2)+1:corr_offset(2)+size(If2,2))=If2;
    %figure(1);
    %subplot(1,2,1);
    %imagesc(I2); 
    %colormap gray; 
    %subplot(1,2,2);
    %imagesc(Iandf); 
    %colormap gray;
end