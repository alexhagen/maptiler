function []=mapedgecheck(I)
    %check left edge
    s=I(:,1,:);
    s=s>0.5010 & s<0.5030;
    s=s(:,1)+s(:,2)+s(:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        left = 1;
        fprintf('Would go best on left edge\n');
    end
    %check right edge
    s=I(:,end,:);
    s=s>0.5010 & s<0.5030;
    s=s(:,1)+s(:,2)+s(:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        right = 1;
        fprintf('Would go best on right edge\n');
    end
    %check top edge
    s=I(1,:,:);
    s=s>0.5010 & s<0.5030;
    s=s(1,:,1)+s(1,:,2)+s(1,:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        top = 1;
        fprintf('Would go best on top edge\n');
    end
    %check bottom edge
    s=I(end,:,:);
    s=s>0.5010 & s<0.5030;
    s=s(1,:,1)+s(1,:,2)+s(1,:,3);
    if (sum(s)>2.4*numel(s) && ...
            sum(s)<3.2*numel(s))
        bottom = 1;
        fprintf('Would go best on bottom edge\n');
    end
end