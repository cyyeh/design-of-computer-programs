"""
UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

    >>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    300

The rules of bowling are as follows:

(1) A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll two, or three.  Your total
score is the sum of your scores for the ten frames.
(2) If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, bowling([8, 1, 7, ...]) means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
(3) If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, bowling([8, 2, 7, ...]) means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
(4) If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, bowling([10, 7, 3, ...]) means that you get a strike, you score
10 + 7 + 3 = 20 in the first frame; the second frame starts with the 7.

"""


def bowling(balls):
    "Compute the total score for a player's game of bowling."
    # bowling([int, ...]) -> int
    FINAL_FRAME = 10
    current_frame = 1
    idx = 0
    score = 0

    def is_strike(balls, idx): return balls[idx] == 10
    def is_spare(balls, idx): return sum(balls[idx:idx+2]) == 10

    def add_3_ball_score(balls, idx): return sum(balls[idx:idx+3])
    def add_2_ball_score(balls, idx): return sum(balls[idx:idx+2])

    while current_frame <= FINAL_FRAME:
        if is_strike(balls, idx):  # strike
            score += add_3_ball_score(balls, idx)
            idx += 1
        elif is_spare(balls, idx):  # spare
            score += add_3_ball_score(balls, idx)
            idx += 2
        else:
            score += add_2_ball_score(balls, idx)
            idx += 2
        current_frame += 1

    return score


def bowling2(balls):
    "Compute the score for one player's game of bowling."
    def score_frame(balls):
        "Return (score, balls): the score for this frame and the remaining balls."
        n_used, n_scoring = (
            (1, 3) if balls[0] == 10  # strike
            else (2, 3) if balls[0] + balls[1] == 10  # spare
            else (2, 2)
        )  # open frame
        score = sum(balls[:n_scoring])
        balls[:n_used] = []
        return score
    return sum(score_frame(balls) for frame in range(10))


def test_bowling():
    assert 0 == bowling([0] * 20)
    assert 20 == bowling([1] * 20)
    assert 80 == bowling([4] * 20)
    assert 190 == bowling([9, 1] * 10 + [9])
    assert 300 == bowling([10] * 12)
    assert 200 == bowling([10, 5, 5] * 5 + [10])
    assert 11 == bowling([0, 0] * 9 + [10, 1, 0])
    assert 12 == bowling([0, 0] * 8 + [10, 1, 0])

    assert 0 == bowling2([0] * 20)
    assert 20 == bowling2([1] * 20)
    assert 80 == bowling2([4] * 20)
    assert 190 == bowling2([9, 1] * 10 + [9])
    assert 300 == bowling2([10] * 12)
    assert 200 == bowling2([10, 5, 5] * 5 + [10])
    assert 11 == bowling2([0, 0] * 9 + [10, 1, 0])
    assert 12 == bowling2([0, 0] * 8 + [10, 1, 0])


test_bowling()
