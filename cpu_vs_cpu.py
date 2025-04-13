import chess
import chess.engine
import time
from typing import NamedTuple

STOCKFISH = '/opt/homebrew/bin/stockfish'


def print_board(board):
    print("\n" + str(board) + "\n")


class CPU(NamedTuple):
    engine: chess.engine.SimpleEngine
    depth: int = 10
    move_time: int = 0.1


def play_engines(cpu1: CPU, cpu2: CPU):
    board = chess.Board()

    cpus = [cpu1, cpu2]

    turn = 0

    print_board(board)

    while not board.is_game_over():
        cpu = cpus[turn]
        result = cpu.engine.play(board,
                                 chess.engine.Limit(depth=cpu.depth, time=cpu.move_time))
        board.push(result.move)

        print(f"{'White' if turn == 0 else 'Black'} played: {board.peek()}")
        print_board(board)
        time.sleep(0.01)

        turn = 1 - turn

    print("Game over:", board.result())
    for cpu in cpus:
        cpu.engine.quit()


# Replace with paths to your engines
cpu1 = CPU(engine=chess.engine.SimpleEngine.popen_uci(STOCKFISH),
           depth=1,
           move_time=0.1)
cpu2 = CPU(engine=chess.engine.SimpleEngine.popen_uci(STOCKFISH),
           depth=12,
           move_time=0.1)


play_engines(cpu1, cpu2)
