function [f]=mapdownload(zoom,center,size)
    url=['http://maps.googleapis.com/maps/api/staticmap' ...
        '?center=' center '&zoom=' sprintf('%d',zoom) ...
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
    f=urlwrite(url,'map.png');
end

%http://maps.googleapis.com/maps/api/staticmap?center=41.744164,-87.665405&zoom=10&format=png&sensor=false&size=640x480&maptype=roadmap&visual_refresh=true&style=visibility:off&style=feature:landscape.natural|visibility:on|color:0xffffff&style=feature:water|visibility:on|color:0x808080&style=feature:road|color:0x000000|visibility:on&style=feature:road.highway|element:labels|visibility:off&style=feature:road.arterial|element:labels|visibility:off&style=feature:road.local|element:labels|visibility:off