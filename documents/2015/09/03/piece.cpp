//
//  piece.cpp
//  moreChess
//
//  Created by ADRIAN BEDARD on 2/15/15.
//  Copyright (c) 2015 Adrian. All rights reserved.
//

#include "piece.h"

piece::piece()
{
	xPosition = 0;
	yPosition = 0;
}

piece::piece(int x, int y)
{
	xPosition = 1;
	yPosition = 1;
}

bool piece::menaces(piece *scared)
{
	return false;
}



int piece::getX()
{
	return xPosition;
}

int piece::getY()
{
	return yPosition;
}

void piece::set(int x, int y)
{
	xPosition = x;
	yPosition = y;
}