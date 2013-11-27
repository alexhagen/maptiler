function []=maptilemaker(gpscoords,style,tilecoord)
    %check edges
    %Download 1280x1280 picture of zoom levels 5-13
    for zoom=5:13
        %Remove bottom strip of picture
        %Generate Fuzzy Picture to Compare to
        %Calculate 2d cross correlation
        %Calculate the total difference at that 2dxcorr, save to array
    end
    %find the minimum difference to find the best fit
    %determine the center of this picture in gps coords and zoom
    %Style the map
    %Download the tiled picture
end