function []=maptilemaker(gpscoords,style,filename)
    zoom = [13:16];
    picsize = [700 560];
    s=struct('gpscoords',[],'zoom',[],...
            'f',[],'croppedf',[],'fuzzyf',[],...
            'cc',[],'max_cc',[],'disable',[],...
            'left',[],'right',[],'top',[],'bottom',[]);
    for i=1:numel(zoom)
        s(i).gpscoords=gpscoords;
        s(i).zoom=zoom(i);
        %Download correctly sized picture of zoom levels 5-13
        f=mapdownload(zoom(i),gpscoords,[picsize(1) picsize(2)+50]);
        s(i).f=f;
        %Remove bottom strip of picture and check edges
        [croppedf,l,r,t,b]=mapcrop(f);
        s(i).l=l;
        s(i).r=r;
        s(i).t=t;
        s(i).b=b;
        if l+r+t+b > 2
            s(i).disable=1;
        else
            s(i).croppedf=croppedf;
            %Generate Fuzzy Picture to Compare to
            [fuzzyf,croppedf]=mapfuzzymaker(croppedf);
            s(i).fuzzyf=fuzzyf;
            %Calculate 2d cross correlation and save performance number
            [cc,max_cc]=mapxcorr(croppedf,fuzzyf);
            s(i).cc=cc;
            s(i).max_cc=max_cc;
        end
    end
    %find the max performance value to find the best fit
    max_cc_arr=arrayfun(@(x)(x.max_cc),s);
    max_cc_ind=find(max(max_cc_arr)==max_cc_arr);
    offset=s(max_cc_ind).cc;
    %determine the center of this picture in gps coords and zoom
    move_sets= [offset(1)-picsize(1)/2 offset(2)-picsize(2)/2]./picsize;
    [bounds]=mapmove(s(max_cc_ind).gpscoords,s(max_cc_ind).zoom,move_sets);
    %Download the tiled picture
    mapmake(bounds,style,['C:\Users\ahagen\Desktop\' filename]);
end