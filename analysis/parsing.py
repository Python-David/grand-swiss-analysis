import chess.pgn
import pandas as pd
import re
import uuid

from tqdm import tqdm

# Regex for parsing evals and clock annotations from comments
EVAL_RE = re.compile(r"\[%eval ([^\]]+)\]")
CLK_RE  = re.compile(r"\[%clk ([^\]]+)\]")

def parse_game_headers(game, game_id: str) -> dict:
    """
    Extracts metadata for one game → returns dict for games.csv
    """
    return {
        "game_id": game_id,
        "event": game.headers.get("Event"),
        "site": game.headers.get("Site"),
        "date": game.headers.get("Date"),
        "round": game.headers.get("Round"),
        "white": game.headers.get("White"),
        "black": game.headers.get("Black"),
        "result": game.headers.get("Result"),
        "white_elo": int(game.headers.get("WhiteElo", 0) or 0),
        "black_elo": int(game.headers.get("BlackElo", 0) or 0),
        "white_fide_id": game.headers.get("WhiteFideId"),
        "black_fide_id": game.headers.get("BlackFideId"),
        "eco": game.headers.get("ECO"),
        "opening": game.headers.get("Opening"),
        "ply_count": sum(1 for _ in game.mainline_moves()),
        "game_url": game.headers.get("GameURL"),
        "broadcast_url": game.headers.get("BroadcastURL"),
    }


def parse_game_moves(game, game_id: str) -> list[dict]:
    """
    Extracts move-by-move data for one game → returns list of dicts for moves.csv
    """
    board = game.board()
    moves_data = []
    move_number = 1

    for node in game.mainline():
        move = node.move
        san = board.san(move)
        comment = node.comment

        # Extract eval
        eval_value = None
        eval_match = EVAL_RE.search(comment)
        if eval_match:
            raw_eval = eval_match.group(1)
            if raw_eval.startswith("#"):  # mate
                eval_value = 10000 if not raw_eval.startswith("#-") else -10000
            else:
                eval_value = float(raw_eval)

        # Extract clock
        clock_str = None
        clk_match = CLK_RE.search(comment)
        if clk_match:
            clock_str = clk_match.group(1)

        moves_data.append({
            "game_id": game_id,
            "move_number": move_number,
            "turn": "white" if board.turn else "black",
            "san": san,
            "eval": eval_value,
            "clock": clock_str,
            "fen": board.fen(),
        })

        board.push(move)
        move_number += 1

    return moves_data


def parse_master_pgn(pgn_path: str, games_out: str, moves_out: str):
    """
    Reads PGN file → writes games.csv and moves.csv
    """
    games_list = []
    moves_list = []

    # First, count games to give tqdm a total
    with open(pgn_path, "r", encoding="utf-8") as f:
        total_games = sum(1 for line in f if line.startswith("[Event "))

    with open(pgn_path, "r", encoding="utf-8") as f:
        for game in tqdm(iter(lambda: chess.pgn.read_game(f), None),
                         total=total_games,
                         desc="Parsing games"):
            game_id = str(uuid.uuid4())
            games_list.append(parse_game_headers(game, game_id))
            moves_list.extend(parse_game_moves(game, game_id))

    # Save
    pd.DataFrame(games_list).to_csv(games_out, index=False)
    pd.DataFrame(moves_list).to_csv(moves_out, index=False)

    print(f"\n Parsed {len(games_list)} games")
    print(f"   → {games_out}")
    print(f"   → {moves_out}")



if __name__ == "__main__":
    parse_master_pgn(
        "data/raw/lichess_broadcast_fide-grand-swiss-2025--open_vSyxclHS_2025.09.15.pgn",
        "data/processed/games.csv",
        "data/processed/moves.csv"
    )
