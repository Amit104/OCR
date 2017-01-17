function a = wordsegment(I)
    a = [];
    b = binimg(I);
    r = size(b,1);
    c = size(b,2);
    thresh = 0;
    
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
            if i - colnum > 3
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
    a=uint8(a);
    subi=[];
    
    if size(a,1) ~= 0
        subi(1:r,1:a(1),1:3)=I(1:r,1:a(1),1:3);
        subi=uint8(subi);
        charactersegment(subi);
   
        for i=2:C-1
            subi = [];
            subi(1:r,1:a(i)-a(i-1)+1,1:3)=I(1:r,a(i-1):a(i),1:3);
            subi=uint8(subi);
            charactersegment(subi);
        end
    end
    
end