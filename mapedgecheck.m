function [l,r,t,b]=mapedgecheck(I)
    l=0;
    r=0;
    t=0;
    b=0;
    %check left edge
    s=I(:,1,:);
    s=s>0.5010 & s<0.5030;
    s=s(:,1)+s(:,2)+s(:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        l = 1;
    end
    %check right edge
    s=I(:,end,:);
    s=s>0.5010 & s<0.5030;
    s=s(:,1)+s(:,2)+s(:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        r = 1;
    end
    %check top edge
    s=I(1,:,:);
    s=s>0.5010 & s<0.5030;
    s=s(1,:,1)+s(1,:,2)+s(1,:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        t = 1;
    end
    %check bottom edge
    s=I(end,:,:);
    s=s>0.5010 & s<0.5030;
    s=s(1,:,1)+s(1,:,2)+s(1,:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        b = 1;
    end
end