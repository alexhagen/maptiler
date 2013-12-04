function []=maptilemaker(gpscoords,style)
    zoom = [5:13];
    s=struct('gpscoords',[],'zoom',[],...
            'f',[],'croppedf',[],'fuzzyf',[],...
            'cc',[],'max_cc',[],'disable',[],...
            'left',[],'right',[],'top',[],'bottom',[]);
    for i=1:3%numel(zoom)
        s(i).gpscoords=gpscoords;
        s(i).zoom=zoom(i);
        %Download 1280x1280 picture of zoom levels 5-13
        f=mapdownload(zoom(i),gpscoords,[1280 1280]/4);
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
            s(i).cc=cc
            s(i).max_cc=max_cc;
        end
    end
    %find the max performance value to find the best fit
    max_cc_arr=arrayfun(@(x)(x.max_cc),s);
    max_cc_ind=find(max(max_cc_arr)==max_cc_arr);
    offset=s(i).cc
    %determine the center of this picture in gps coords and zoom
    %Style the map
    %Download the tiled picture
end