function n = find_first_y(a)
    y_prev = 0;
    n = 1;

    while true
        y_current = (y_prev + 1) / (y_prev + 2);

        if y_current - y_prev < a
            break;
        end

        y_prev = y_current;
        n = n + 1;
    end
end