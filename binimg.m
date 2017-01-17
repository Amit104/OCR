function I = binimg(I)
    r=size(I,1);
    c=size(I,2);
    for i=1:r
        for j=1:c
            C=0;
            for k=1:3
                if I(i,j,k) < 160
                    C=C+1;
                end
            end
            if C==3
                for k=1:3
                    I(i,j,k)=0;
                end
            else
                for k=1:3
                    I(i,j,k)=255;
                end
            end
        end
    end
end