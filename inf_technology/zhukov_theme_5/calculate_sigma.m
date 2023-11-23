function sigma = calculate_sigma(n)
    sigma = 0;

    for k = 0:n
        term = ((-1)^k * (k + 1)) / factorial(k);
        sigma = sigma + term;
    end
end