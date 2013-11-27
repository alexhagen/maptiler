function []=maptilemaker(gpscoords,style)
    for zoom=5%:13
        %Download 1280x1280 picture of zoom levels 5-13
        f=mapdownload(zoom,gpscoords,[640 640]);
        %Remove bottom strip of picture and check edges
        f=mapcrop(f);
        %Generate Fuzzy Picture to Compare to
        %Calculate 2d cross correlation
        %Calculate the total difference at that 2dxcorr, save to array
    end
    %find the minimum difference to find the best fit
    %determine the center of this picture in gps coords and zoom
    %Style the map
    %Download the tiled picture
end