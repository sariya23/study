function sign = determine_polynomial_sign(a, b, c, d, x)
    % Determines the sign of the polynomial ax^3 - bx^2 - cx + d at the point x.

    polynomial_value = a * x^3 - b * x^2 - c * x + d;

    if polynomial_value > 0
        sign = 1;
    elseif polynomial_value < 0
        sign = -1; 
    else
        sign = 0;
    end
end
