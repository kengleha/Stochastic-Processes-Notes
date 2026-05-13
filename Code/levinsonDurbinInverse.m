function inverseMatrix = levinsonDurbinInverse(acf)
    % ACF: Autocorrelation function (column vector)
    
    order = length(acf) - 1;  % Model order
    
    % Initialization
    a = zeros(order + 1, 1);
    E = acf(1);  % Prediction error for k = 0
    
    % Initialization for the inverse Toeplitz matrix
    inverseMatrix = toeplitz(1 ./ acf);
    
    for k = 1:order
        % Levinson recursion
        alpha = -acf(k + 1:-1:2).' * a(1:k);
        alpha = alpha / E;
        
        a(1:k) = a(1:k) + alpha * flip(a(1:k));
        a(k + 1) = alpha;
        
        % Update prediction error
        E = (1 - alpha^2) * E;
        
        % Update the inverse Toeplitz matrix
        col = [1; flip(alpha * a(1:k))];
        row = [1, alpha * a(1:k).'];
        inverseMatrix = inverseMatrix - (inverseMatrix * col) * row / (1 + alpha * a(1:k).' * col);
    end
end