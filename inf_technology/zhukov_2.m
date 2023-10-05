% Task 1 %
MATRIX = [1, 10, 1; 1, 2, 3; 1, 3, 6];
disp(MATRIX);

% Task 2 %
MATRIX(1, 2) = 1;
disp(MATRIX);

% Task 3 %
ZEROS_MATRIX = zeros(2);
ONES_MATRIX = ones(2);
EYE_MATRIX = eye(2);
RAND_MATRIX = rand(2);
RANDN_MATRIX = randn(2);
MAGIC_MATRIX = magic(2);
disp('-------------');
disp('zeros:');
disp(ZEROS_MATRIX);
disp('ones:');
disp(ONES_MATRIX);
disp('eye:');
disp(EYE_MATRIX);
disp('rand:');
disp(RAND_MATRIX);
disp('randn:');
disp(RANDN_MATRIX);
disp('magic:');
disp(MAGIC_MATRIX);

% Task 4 %
v = [65, 8, 7];
k = 3;
n = length(v); 

X = zeros(n);

for i = 1:n
    X(i, i + k - 1) = v(i);
end
disp('-----------')
disp(X)

% Task 5 %
A = [1, 10, 1; 1, 2, 3; 1, 3, 6];
B = [3, 2, 0; 8, 5, 0];

M = [A; B];
N = blkdiag(A, B);
L = cat(1, A, B);

% Task 6 %
B(:, 3) = [];
L(2, :) = [];
M = [];

% Task 7 %
fprintf('Det A: %d\n', det(A));
fprintf('Det B: %d\n', det(B));

% Task 8 %
disp('--------')
A = [5, -6, 4; 3, -3, 2; 4, -5, 2];
b = [3; 2; 1];
X = A \ b;
fprintf('x_1 = %d\n', X(1));
fprintf('x_2 = %d\n', X(2));
fprintf('x_3 = %d\n', X(3));