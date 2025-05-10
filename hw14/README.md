# CartPole with Fixed Strategy (Exercise 14)

This project solves the CartPole balancing problem using a fixed rule-based strategy (no machine learning).

## Strategy
- If the pole is leaning left, move left.
- If the pole is leaning right, move right.
- Takes angular velocity into account for faster correction.

## Files
- `cartpole_fixed.py`: Main script with hardcoded control logic.

## Run
```bash
python cartpole_fixed.py
