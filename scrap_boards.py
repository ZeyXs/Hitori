import requests as req
from bs4 import BeautifulSoup


def get_a_board(size: int=5):
	r = req.get(f"https://www.hitoriconquest.com/?puzzleSize={size}")
	soup = BeautifulSoup(r.content, "html.parser")

	rawboard = soup.find("table", {"id": "puzzleTable"})


	board = []
	for i, line in enumerate(rawboard.find_all("tr")):
		board.append([])
		for col in line.find_all("td"):
			n = int(col.find("div").text)
			board[i].append([n, -1])

	return board
