# -*- coding: utf-8 -*-
"""
A set of utilities to process chess games
"""

# imports
import numpy as np

# a python lib for reading chess games
import chess
import chess.pgn
import chess.variant


########################################################
# methods

def coords_to_np(coords_str):
    # transform chess coordinates to numpy indexes
    # e.g. 'e4' -> 4,4
    
    # dictionaries for convertion
    letters_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    ranks_dict =   {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    
    # get letter and rank
    letter = coords_str[0]
    rank = coords_str[1]
    # convert to indexes with dicts
    i = ranks_dict[rank]
    j = letters_dict[letter]
    # return as tuple
    return (i, j)
# end func


def board2np(board):
    # transform the board object in a np array
    
    # dict of piece types
    pieces_dict = {0: '.', 1: 'P', 2: 'N', 3: 'B', 4: 'R', 5: 'Q', 6: 'K'}
    
    # def np board
    board_np = np.zeros((8, 8), str)
    
    # for all squares, get the piece and put in np board
    # this is ugly, and there is probably a much better way.. :p
    # proc square
    q = board.piece_at(chess.A1)
    i, j = coords_to_np('a1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.A2)
    i, j = coords_to_np('a2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.A3)
    i, j = coords_to_np('a3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.A4)
    i, j = coords_to_np('a4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.A5)
    i, j = coords_to_np('a5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.A6)
    i, j = coords_to_np('a6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.A7)
    i, j = coords_to_np('a7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.A8)
    i, j = coords_to_np('a8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # new row
    # proc square
    q = board.piece_at(chess.B1)
    i, j = coords_to_np('b1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.B2)
    i, j = coords_to_np('b2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.B3)
    i, j = coords_to_np('b3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.B4)
    i, j = coords_to_np('b4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.B5)
    i, j = coords_to_np('b5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.B6)
    i, j = coords_to_np('b6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.B7)
    i, j = coords_to_np('b7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.B8)
    i, j = coords_to_np('b8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # new row
    # proc square
    q = board.piece_at(chess.C1)
    i, j = coords_to_np('c1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.C2)
    i, j = coords_to_np('c2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.C3)
    i, j = coords_to_np('c3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.C4)
    i, j = coords_to_np('c4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.C5)
    i, j = coords_to_np('c5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.C6)
    i, j = coords_to_np('c6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.C7)
    i, j = coords_to_np('c7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.C8)
    i, j = coords_to_np('c8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # new row
    # proc square
    q = board.piece_at(chess.D1)
    i, j = coords_to_np('d1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.D2)
    i, j = coords_to_np('d2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.D3)
    i, j = coords_to_np('d3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.D4)
    i, j = coords_to_np('d4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.D5)
    i, j = coords_to_np('d5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.D6)
    i, j = coords_to_np('d6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.D7)
    i, j = coords_to_np('d7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.D8)
    i, j = coords_to_np('d8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # new row
    # proc square
    q = board.piece_at(chess.E1)
    i, j = coords_to_np('e1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.E2)
    i, j = coords_to_np('e2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.E3)
    i, j = coords_to_np('e3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.E4)
    i, j = coords_to_np('e4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.E5)
    i, j = coords_to_np('e5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.E6)
    i, j = coords_to_np('e6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.E7)
    i, j = coords_to_np('e7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.E8)
    i, j = coords_to_np('e8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # new row
    # proc square
    q = board.piece_at(chess.F1)
    i, j = coords_to_np('f1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.F2)
    i, j = coords_to_np('f2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.F3)
    i, j = coords_to_np('f3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.F4)
    i, j = coords_to_np('f4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.F5)
    i, j = coords_to_np('f5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.F6)
    i, j = coords_to_np('f6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.F7)
    i, j = coords_to_np('f7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.F8)
    i, j = coords_to_np('f8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # new row
    # proc square
    q = board.piece_at(chess.G1)
    i, j = coords_to_np('g1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.G2)
    i, j = coords_to_np('g2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.G3)
    i, j = coords_to_np('g3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.G4)
    i, j = coords_to_np('g4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.G5)
    i, j = coords_to_np('g5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.G6)
    i, j = coords_to_np('g6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.G7)
    i, j = coords_to_np('g7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.G8)
    i, j = coords_to_np('g8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # new row
    # proc square
    q = board.piece_at(chess.H1)
    i, j = coords_to_np('h1')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.H2)
    i, j = coords_to_np('h2')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.H3)
    i, j = coords_to_np('h3')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.H4)
    i, j = coords_to_np('h4')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.H5)
    i, j = coords_to_np('h5')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.H6)
    i, j = coords_to_np('h6')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.H7)
    i, j = coords_to_np('h7')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    # proc square
    q = board.piece_at(chess.H8)
    i, j = coords_to_np('h8')
    if q == None:
         board_np[i, j] = pieces_dict[0]
    else:
        piece = pieces_dict[ q.piece_type ]
        if q.color == False: # black
            piece = piece.lower() # e.g. Q -> q
        board_np[i, j] = piece
    # end if
    
    
    # ready
    return board_np
# end func

def get_material(np_board):
    # get material imbalance from board 
    # returns a vec, [P, N, B, R, Q, K]
    # where P is the pawn imbalance (white pawns - black pawns), 
    # and similarly for the other pieces
    
    material = np.zeros(6, int)
    
    for i in range(8):
        for j in range(8):
            piece = np_board[i, j]
            # pawn
            if piece == 'P':
                material[0] += 1
            elif piece == 'p':
                material[0] -= 1
            # knight
            elif piece == 'N':
                material[1] += 1
            elif piece == 'n':
                material[1] -= 1
            # bishop
            elif piece == 'B':
                material[2] += 1
            elif piece == 'b':
                material[2] -= 1
            # rook
            elif piece == 'R':
                material[3] += 1
            elif piece == 'r':
                material[3] -= 1
            # queen
            elif piece == 'Q':
                material[4] += 1
            elif piece == 'q':
                material[4] -= 1
            # king
            elif piece == 'K':
                material[5] += 1
            elif piece == 'k':
                material[5] -= 1
            # end if
    # end for
    return material
# end func

def read_games(png_file, skip_draws = False, max_elo_diff = 100, min_elo = 1400, 
               min_moves = 10, samples_per_game = 3, n_total = 10000, include_kings = False,
               min_material = 1):
    # a function to read chess games from a png file
    # from each game, we sample some positions and record the material differences
    # we include them in a dataset (X), along with the game outcomes (Y)
    
    X = np.zeros((0, 6), int)
    Y = np.zeros(0, int)
    
    pgn = open(png_file) 
    cntw = -1
    
    while True:
        if cntw > n_total:
            break
        
        # try to read next game
        try:
            # get next game
            game = chess.pgn.read_game(pgn)
        except:
            break
        # end try
        
        # get game elos, time, etc.
        try:
            w_elo = float(game.headers['WhiteElo'])   
            b_elo = float(game.headers['BlackElo'])   
            
            time_str = game.headers['TimeControl']
            # it will be like 10+0, get the 10 and the 0
            i = time_str.find('+')
            time_base = int(time_str[:i])
            time_inc = int(time_str[i+1:])    
            
            res_str = game.headers['Result']
            if res_str == '1-0':
                result = 1
            elif res_str == '0-1':
                result = -1
            else: # 1/2 - 1/2
                result = 0
            
            term_str =  game.headers['Termination']
            if term_str == 'Normal':
                termin = True
            else:
                termin = False
        except:
            continue
        # end try
        
        # if high rating diff, low ratings or fast time controls, skip game
        if np.abs(w_elo - b_elo) > max_elo_diff:
            continue
        
        if max(w_elo, b_elo) < min_elo:
            continue
        
        if time_base <= 1 and time_inc == 0:
            continue
        
        if skip_draws == True and result == 0:
            continue
        
        # now read game moves
        # get number of moves
        n_moves = len( list(game.mainline_moves()) )
        # an array to hold all intermediate positions in the game
        board_pos = np.zeros((n_moves, 8, 8), str)
        
        if n_moves < min_moves:
            continue
        
    
        # go through moves
        cntw += 1
        cnt = -1
        board = game.board() # init game board
        for move in game.mainline_moves():
            board.push(move)
            #print(board); print();
            
            # get board as np
            np_board = board2np(board)
            cnt += 1
            board_pos[cnt] = np_board.copy()
        # end for
        
        # get some random positions from the game
        ind = np.random.choice(np.arange(n_moves), samples_per_game, False)
        
        
        # for the selected positions, if material imbalnce, include in the dataset
        for i in ind:
            # get ith pos
            np_board = board_pos[i]
            
            # get material
            v = get_material(np_board)
            
            if np.sum(np.abs(v)) > min_material:
                #require at least 2 impalances to avoid capture - recapture
                #positions that are not informative
                
                # append v and result in dataset
                X = np.vstack((X, v))
                Y = np.hstack((Y, result))
        # end for
    # end while
    
    if include_kings == False:
        # drop king imbalance column (not needed instandard chess!)
        X = X[:, :5]
    
    # return data
    return X, Y
# end func

def npbard2num(np_board):
    # transforms a np string board into a numerical np board
    # where 'P', 'N', become 1, 2, etc.
    
    num_board = np.zeros((8, 8, 13), int)
    
    piece_dict = {'.': 0, 
                  'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
                  'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12}
    
    for i in range(8):
        for j in range(8):
            piece = np_board[i, j]
            k = piece_dict[piece]
            
            # encode pieces with vectors
            num_board[i, j, k] = 1
    # end for
    return num_board
# end func


def read_games_neural(png_file, skip_draws = False, max_elo_diff = 50, min_elo = 2000, 
               min_moves = 10, samples_per_game = 3, n_total = 20000):
    # a function to read chess games from a png file
    # from each game, we sample some positions and record the material differences
    # we include them in a dataset (X), along with the game outcomes (Y)
    
    X = np.zeros((0, 8, 8, 13), int)
    Y = np.zeros(0, int)
    
    pgn = open(png_file) 
    cntw = -1
    
    while True:
        if cntw > n_total:
            break
        
        # try to read next game
        try:
            # get next game
            game = chess.pgn.read_game(pgn)
        except:
            break
        # end try
        
        # get game elos, time, etc.
        try:
            w_elo = float(game.headers['WhiteElo'])   
            b_elo = float(game.headers['BlackElo'])   
            
            time_str = game.headers['TimeControl']
            # it will be like 10+0, get the 10 and the 0
            i = time_str.find('+')
            time_base = int(time_str[:i])
            time_inc = int(time_str[i+1:])    
            
            res_str = game.headers['Result']
            if res_str == '1-0':
                result = 1
            elif res_str == '0-1':
                result = -1
            else: # 1/2 - 1/2
                result = 0
            
            term_str =  game.headers['Termination']
            if term_str == 'Normal':
                termin = True
            else:
                termin = False
        except:
            continue
        # end try
        
        # if high rating diff, low ratings or fast time controls, skip game
        if np.abs(w_elo - b_elo) > max_elo_diff:
            continue
        
        if max(w_elo, b_elo) < min_elo:
            continue
        
        if time_base <= 1 and time_inc == 0:
            continue
        
        if skip_draws == True and result == 0:
            continue
        
        # now read game moves
        # get number of moves
        n_moves = len( list(game.mainline_moves()) )
        # an array to hold all intermediate positions in the game
        board_pos = np.zeros((n_moves, 8, 8), str)
        
        if n_moves < min_moves:
            continue
        
    
        # go through moves
        cntw += 1
        cnt = -1
        board = game.board() # init game board
        for move in game.mainline_moves():
            board.push(move)
            #print(board); print();
            
            # get board as np
            np_board = board2np(board)
            cnt += 1
            board_pos[cnt] = np_board.copy()
        # end for
        
        # get some random positions from the game
        ind = np.random.choice(np.arange(n_moves), samples_per_game, False)
        
        
        # for the selected positions, if material imbalnce, include in the dataset
        for i in ind:
            # get ith pos
            np_board = board_pos[i]
            
            # get material
            v = get_material(np_board)
            
            if np.sum(np.abs(v)) > 1:
                #require at least 2 impalances to avoid capture - recapture
                #positions that are not informative
                
                # get num board representation of pos
                num_board = npbard2num(np_board)
                # add batch dim
                num_board = np.reshape(num_board, (1, *num_board.shape))
                
                # append v and result in dataset
                X = np.vstack((X, num_board))
                Y = np.hstack((Y, result))
        # end for
    # end while
    
    # return data
    return X, Y
# end func


def read_games_variant(png_file, variant, skip_draws = False, max_elo_diff = 100, min_elo = 1400, 
               min_moves = 10, samples_per_game = 3, n_total = 5000, include_kings = False):
    # a function to read chess games from a png file
    # from each game, we sample some positions and record the material differences
    # we include them in a dataset (X), along with the game outcomes (Y)
    
    X = np.zeros((0, 6), int)
    Y = np.zeros(0, int)
    
    pgn = open(png_file) 
    cntw = -1
    
    while True:
        if cntw > n_total:
            break
        
        # try to read next game
        try:
            # get next game
            game = chess.pgn.read_game(pgn)
        except:
            break
        # end try
        
        # get game elos, time, etc.
        try:
            w_elo = float(game.headers['WhiteElo'])   
            b_elo = float(game.headers['BlackElo'])   
            
            time_str = game.headers['TimeControl']
            # it will be like 10+0, get the 10 and the 0
            i = time_str.find('+')
            time_base = int(time_str[:i])
            time_inc = int(time_str[i+1:])    
            
            res_str = game.headers['Result']
            if res_str == '1-0':
                result = 1
            elif res_str == '0-1':
                result = -1
            else: # 1/2 - 1/2
                result = 0
            
            term_str =  game.headers['Termination']
            if term_str == 'Normal':
                termin = True
            else:
                termin = False
        except:
            continue
        # end try
        
        # if high rating diff, low ratings or fast time controls, skip game
        if np.abs(w_elo - b_elo) > max_elo_diff:
            continue
        
        if max(w_elo, b_elo) < min_elo:
            continue
        
        if time_base <= 1 and time_inc == 0:
            continue
        
        if skip_draws == True and result == 0:
            continue
        
        # now read game moves
        # get number of moves
        n_moves = len( list(game.mainline_moves()) )
        # an array to hold all intermediate positions in the game
        board_pos = np.zeros((n_moves, 8, 8), str)
        
        if n_moves < min_moves:
            continue
        
    
        # go through moves
        cntw += 1
        cnt = -1
        if variant == 'standard':
            board = game.board() # init game board
        elif variant == 'antichess':
            board = chess.variant.AntichessBoard()
            include_kings = True
        elif variant == 'atomic':
            board = chess.variant.AtomicBoard()
        else:
            print('variant not supported or undestood!')
            return None, None
        # end if
            
        for move in game.mainline_moves():
            board.push(move)
            #print(board); print();
            
            # get board as np
            np_board = board2np(board)
            cnt += 1
            board_pos[cnt] = np_board.copy()
        # end for
        
        # get some random positions from the game
        ind = np.random.choice(np.arange(n_moves), samples_per_game, False)
        
        
        # for the selected positions, if material imbalnce, include in the dataset
        for i in ind:
            # get ith pos
            np_board = board_pos[i]
            
            # get material
            v = get_material(np_board)
            
            if np.sum(np.abs(v)) > 1:
                #require at least 2 impalances to avoid capture - recapture
                #positions that are not informative
                
                # append v and result in dataset
                X = np.vstack((X, v))
                Y = np.hstack((Y, result))
        # end for
    # end while
    
    if include_kings == False:
        # drop king imbalance column (not needed instandard chess!)
        X = X[:, :5]
    
    # return data
    return X, Y
# end func


def read_games_rl(png_file, max_elo_diff = 200, min_elo = 2100, 
               min_moves = 10, samples_per_game = 5, n_total = 5000, include_kings = False):
    # a function to read chess games from a png file for rl state value estimation
    # from each game, we sample some positions and record next position, and reward
    # if available (win, loss, draw)
    
    X = np.zeros((0, 6), int)
    Xn = np.zeros((0, 6), int) # next state
    R = np.zeros(0, int) # rewards
    
    pgn = open(png_file) 
    cntw = -1
    
    while True:
        if cntw > n_total:
            break
        
        # try to read next game
        try:
            # get next game
            game = chess.pgn.read_game(pgn)
        except:
            break
        # end try
        
        # get game elos, time, etc.
        try:
            w_elo = float(game.headers['WhiteElo'])   
            b_elo = float(game.headers['BlackElo'])   
            
            time_str = game.headers['TimeControl']
            # it will be like 10+0, get the 10 and the 0
            i = time_str.find('+')
            time_base = int(time_str[:i])
            time_inc = int(time_str[i+1:])    
            
            res_str = game.headers['Result']
            if res_str == '1-0':
                result = 1
            elif res_str == '0-1':
                result = -1
            else: # 1/2 - 1/2
                result = 0
            
            term_str =  game.headers['Termination']
            if term_str == 'Normal':
                termin = True
            else:
                termin = False
        except:
            continue
        # end try
        
        # if high rating diff, low ratings or fast time controls, skip game
        if np.abs(w_elo - b_elo) > max_elo_diff:
            continue
        
        if max(w_elo, b_elo) < min_elo:
            continue
        
        if time_base <= 1 and time_inc == 0:
            continue
        
        # now read game moves
        # get number of moves
        n_moves = len( list(game.mainline_moves()) )
        # an array to hold all intermediate positions in the game
        board_pos = np.zeros((n_moves, 8, 8), str)
        
        if n_moves < min_moves:
            continue
        
    
        # go through moves
        cntw += 1
        cnt = -1
        board = game.board() # init game board
        for move in game.mainline_moves():
            board.push(move)
            #print(board); print();
            
            # get board as np
            np_board = board2np(board)
            cnt += 1
            board_pos[cnt] = np_board.copy()
        # end for
        
        # get 2 final pos and reward
        np_board = board_pos[n_moves - 2]
        v = get_material(np_board)
        X = np.vstack((X, v))
        
        np_board2 = board_pos[n_moves - 1]
        v2 = get_material(np_board2)
        Xn = np.vstack((Xn, v2))
        
        # also reward
        R = np.hstack((R, result))
        
        
        # get also some other random positions from the game
        ind = np.random.choice(np.arange(n_moves - 2), samples_per_game, False)
        
        
        # for the selected positions, if material imbalance, include in the dataset
        for i in ind:
            # get ith pos
            np_board = board_pos[i]
            # get material
            v = get_material(np_board)
            
            # get i+1 th pos
            np_board2 = board_pos[i+1]
            # get material
            v2 = get_material(np_board2)
            
            # append
            X = np.vstack((X, v))
            Xn = np.vstack((Xn, v))
            R = np.hstack((R, 0)) # no reward for intermed positions
        # end for
            
            
    # end while
    
    if include_kings == False:
        # drop king imbalance column (not needed in standard chess!)
        X = X[:, :5]
        Xn = Xn[:, :5]
    
    # return data
    return X, Xn, R
# end func
