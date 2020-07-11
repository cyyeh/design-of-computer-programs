# Design of Computer Programs

What I would like to do in this repo is try to solve problems using different programming languages. With different
programming languages comes with different syntax features that allow us to do things in different ways. I hope this
would be an interesting way to learn new languages that we can try using them to solve earlier solved problems, rather
than merely learn new syntax features. Now these problems mainly come from a Udacity course, Design of Computer Programs.

This will and should be a live updating repo that I will try my best to add new puzzles.

## UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

```python
>>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
300
```

The rules of bowling are as follows:

1. A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll two, or three.  Your total
score is the sum of your scores for the ten frames.
2. If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, `bowling([8, 1, 7, ...])` means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
3. If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, `bowling([8, 2, 7, ...])` means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
4. If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, `bowling([10, 7, 3, ...])` means that you get a strike, you score `10 + 7 + 3 = 20` in the first frame; the second frame starts with the 7.

## UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

```
['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
```

(You can assume that the days mentioned are all in the same week.)


## References

- [Udacity: Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212)
