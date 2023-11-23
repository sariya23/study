% task 1
str_cell = {
    '123', 'abcd';
    '5678', 'efg'
};
disp(str_cell);

% task 2
A = 32:52;
char_array = char(A);
disp(char_array);

% task 3
disp('It is life'(5))

% task 4
str1 = '     East          ';

len = length(str1);

center_aligned = (sprintf('%*s', len, str1));
left_aligned = (sprintf('%-*s', len, str1));
right_aligned = (sprintf('%*s', len, str1));

disp(['Исходная строка: ', str1]);
disp(['Длина строки: ', num2str(len)]);
disp(['Выровнено по центру: ', center_aligned]);
disp(['Выровнено по левой стороне: ', left_aligned]);
disp(['Выровнено по правой стороне: ', right_aligned]);

% task 5
str1 = '     East          ';
str1_trimmed = strtrim(str1);
len = length(str1_trimmed);
disp(['Исходная строка: ', str1]);
disp(['Длина строки без концевых пробелов: ', num2str(len)]);
disp(['Строка без концевых пробелов: ', str1_trimmed]);

% task 6
array = repmat('+', 3, 4);
disp(array);

% task 7
% Задайте строки
s1 = 'Happy';
s2 = 'New';
s3 = 'Year';
vertical_concatenation = {s1; s2; s3};
horizontal_concatenation = [s1, ' ', s2, ' ', s3];
disp('Объединение вертикально:');
disp(vertical_concatenation);

disp('Объединение горизонтально:');
disp(horizontal_concatenation);

% task 8
st1 = 'example';
st2 = 'EXAMple';

compare_case_sensitive = strcmp(st1, st2);
disp(['Сравнение с учетом регистра: ', num2str(compare_case_sensitive)]);

compare_case_insensitive = strcmpi(st1, st2);
disp(['Сравнение без учета регистра: ', num2str(compare_case_insensitive)]);

n = 6; % Сравниваем первые 6 символов
compare_n_characters = strncmp(st1, st2, n);
disp(['Сравнение первых ', num2str(n), ' символов: ', num2str(compare_n_characters)]);

% task 9
st2 = 'EXAMple';
upper_case_st2 = upper(st2);
disp(['Строка в верхнем регистре: ', upper_case_st2]);
lower_case_st2 = lower(st2);
disp(['Строка в нижнем регистре: ', lower_case_st2]);

% task 10
s = 'oo';
str = 'boom';
index = strfind(str, s);
contains_strfind = ~isempty(index);

disp(['Используя strfind: ', num2str(contains_strfind)]);

% task 11
str = 'London is the capital of Great Britain';
modified_str = strrep(str, 'o', '*');
disp(['Исходная строка: ', str]);
disp(['Модифицированная строка: ', modified_str]);

% taks 12
str = 'London is the capital of Great Britain';
tokens = strsplit(str);
disp('Лексемы:');
disp(tokens);

% task 13
A = randn(3);
formatted_str = sprintf('%.5f ', A);
disp('Преобразованная строка:');
disp(formatted_str);