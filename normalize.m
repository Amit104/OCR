function I = normalize(I)
    max=0;
    min=256;
    r=size(I,1);
    c=size(I,2);
    for i=1:r
        for j=1:c
            for k=1:3
                if max<I(i,j,k)
                    max=I(i,j,k);
                end
                if min>I(i,j,k)
                    min=I(i,j,k);
                end
            end
        end
    end
    
    low=double(min)/255
    high=double(max)/255
    
    I=imadjust(I,[low high],[0.1 1],0.9);
end