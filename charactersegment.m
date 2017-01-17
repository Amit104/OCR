function a = charactersegment(I)
    a = [];
    b = binimg(I);
    r = size(b,1);
    c = size(b,2);
    avg = 0;
    for i = 1:c
        colsum = 0;
        for j = 1:r
            if b(j,i,1) == 0
                colsum = colsum + 1;
            end
        end
        avg = avg + colsum;
    end
    avg = avg/r;
    thresh = avg/2;
    
    flag = 0; C = 1;colnum = 0;
    for i = 1:c
        colsum = 0;
        for j = 1:r
            if b(j,i,1) == 0
                colsum = colsum + 1;
            end
        end
        
        if colsum <= thresh && flag == 0
            flag = 1;
            colnum = i;
            
        elseif colsum > thresh && flag == 1
            flag = 0;
            mid = (colnum + i)/2;
            if i - colnum > 1
                a(C) = mid;
                C = C + 1;
            end
        end
    end
    %figure,imshow(I), hold on;
    figure,imshow(b), hold on;
    for i=1:C-1
        plot([a(i),a(i)],[1,r],'Color','r','LineWidth',2);
    end
    
    hold on;
end