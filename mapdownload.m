function [f]=mapdownload(zoom,center,size)
    if numel(center)==2
        centerstring=sprintf('%.6f,%.6f',center(1),center(2));
    else
        centerstring=center;
    end
    url=['http://maps.googleapis.com/maps/api/staticmap' ...
        '?center=' centerstring '&zoom=' sprintf('%d',zoom) ...
        '&size=' sprintf('%d',size(1)) 'x' sprintf('%d',size(2)) ...
        '&maptype=roadmap&scale=2' ...
        '&sensor=false' ...
        '&visual_refresh=true&style=visibility:off' ...
        '&style=feature:landscape.natural|visibility:on|color:0xffffff' ...
        '&style=feature:water|visibility:on|color:0x808080' ...
        '&style=feature:road|color:0x000000|visibility:on' ...
        '&style=feature:road.highway|element:labels|visibility:off' ...
        '&style=feature:road.arterial|element:labels|visibility:off' ...
        '&style=feature:road.local|element:labels|visibility:off'];
    f=urlwrite(url,...
        sprintf('zoom%d_gps%.0f_%.0f.png',...
        zoom,1000*center(1),1000*center(2)));
end

%http://maps.googleapis.com/maps/api/staticmap?center=41.744164,-87.665405&
%zoom=10&format=png&sensor=false&size=640x480&maptype=roadmap&visual_refres
%h=true&style=visibility:off&style=feature:landscape.natural|visibility:on|
%color:0xffffff&style=feature:water|visibility:on|color:0x808080&style=feat
%ure:road|color:0x000000|visibility:on&style=feature:road.highway|element:l
%abels|visibility:off&style=feature:road.arterial|element:labels|visibility
%:off&style=feature:road.local|element:labels|visibility:off
