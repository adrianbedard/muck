//
//  board.cpp
//  moreChess
//
//  Created by ADRIAN BEDARD on 2/15/15.
//  Copyright (c) 2015 Adrian. All rights reserved.
//

#include "board.h"
#include <iostream>
#include "piece.h"
	//#include "rook.h"

board::board()
{
	grid = new piece*[100];
	inArray = 0;
	solved = false;
	clearBoard();
}

board::~board()
{
	delete grid;
}

board::board(int dim)
{
	dimension = dim;
	
	grid = new piece*[dimension * dimension];
	cout << grid[0];
	clearBoard();
	solved = false;
	
	
}

void board::clearBoard()
{
	for(int place = 0; place < dimension*dimension; place++)
		{
	grid[place] = new piece();
		}
}

bool board::isSafe(piece *newPiece)
{
	for(int checker = 0; checker < dimension*dimension; checker++)
		{
		if(grid[checker]->menaces(newPiece))
			{
			return false;
			}
		}
	return true;
}

void board::insert(int location, piece *toInsert)
{
	grid[location] = toInsert;
	
	
}

void board::printBoard()
{
	for(int i = 0; i < dimension; i++)
		{
		for(int j = 0; j < dimension; j++)
			{
			cout << grid[(i * dimension) + j]->getY();
			}
		}
	cout << endl;
}