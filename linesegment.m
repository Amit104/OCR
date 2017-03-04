function [a] = linesegment(I)
    a = [];
    b = binimg(I);
    r = size(b,1);
    c = size(b,2);
    avg = 0;
    for i = 1:r
        rowsum = 0;
        for j = 1:c
            if b(i,j,1) == 0
                rowsum = rowsum + 1;
            end
        end
        avg = avg + rowsum;
    end
    avg = avg/r;
    thresh = 0;
    
    flag = 0; C = 1;rownum = 0;
    for i = 1:r
        rowsum = 0;
        for j = 1:c
            if b(i,j,1) == 0
                rowsum = rowsum + 1;
            end
        end
        
        if rowsum <= thresh && flag == 0
            flag = 1;
            rownum = i;
            
        elseif rowsum > thresh && flag == 1
            flag = 0;
            mid = (rownum + i)/2;
            if i - rownum > 1
                a(C) = mid;
                C = C + 1;
            end
        end
    end
    %figure,imshow(I), hold on;
    figure,imshow(b), hold on;
    for i=1:C-1
        plot([1,c],[a(i),a(i)],'Color','r','LineWidth',2);
    end
    
    hold on;
    a=uint8(a);
    subi=[];
    subi(1:a(1),1:c,1:3)=I(1:a(1),1:c,1:3);
    subi=uint8(subi);
    wordsegment(subi);
    for i=2:C-1
        subi = [];
        subi(1:a(i)-a(i-1)+1,1:c,1:3)=I(a(i-1):a(i),1:c,1:3);
        subi=uint8(subi);
        wordsegment(subi);
    end
end
    