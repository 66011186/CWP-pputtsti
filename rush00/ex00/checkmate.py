#!/usr/bin/env python3

def checkmate(board: str):
    if not board or not isinstance(board, str):
        return

    lines = [line for line in board.strip('\n').split('\n') if line]
    if not lines:
        return

    size = len(lines)
    # Verify the board is square
    for line in lines:
        if len(line) != size:
            return

    # Find the King ('K')
    king_positions = []
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_positions.append((r, c))

    if len(king_positions) != 1:
        return

    kr, kc = king_positions[0]

    # Check Pawn attack positions (Pawns attack diagonally up-left and up-right)
    pawn_attacks = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for pr, pc in pawn_attacks:
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                print("Success")
                return

    # Straight & Diagonal direction vectors: (row_delta, col_delta)
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Check straight lines (Rook 'R' and Queen 'Q')
    for dr, dc in straight_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('R', 'Q'):
                print("Success")
                return
            if piece in ('P', 'B', 'K'):
                break  
            r += dr
            c += dc

    # Check diagonal lines (Bishop 'B' and Queen 'Q')
    for dr, dc in diag_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('B', 'Q'):
                print("Success")
                return
            if piece in ('P', 'R', 'K'):
                break  
            r += dr
            c += dc

    print("Fail")