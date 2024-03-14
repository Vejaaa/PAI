MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    best = MIN if maximizingPlayer else MAX

    for i in range(2):
        val = minimax(depth + 1, nodeIndex * 2 + i, not maximizingPlayer, values, alpha, beta)
        best = max(best, val) if maximizingPlayer else min(best, val)
        alpha = max(alpha, best) if maximizingPlayer else alpha
        beta = min(beta, best) if not maximizingPlayer else beta

        if beta <= alpha:
            break

    return best

if __name__ == "__main__":
    values = [10, 9, 14, 18, 5, 4, 50, 3]
    print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))
