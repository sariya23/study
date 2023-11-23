function isMember = checkMembership(number, array)
    isMember = ismember(number, array);

    if isMember
        disp(['The number ', num2str(number), ' belongs to the array.']);
    else
        disp(['The number ', num2str(number), ' does not belong to the array.']);
    end
end