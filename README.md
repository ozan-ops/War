# War Card Game

This Python script simulates the classic card game War. In War, two players compete to win all the cards by comparing the ranks of their cards. The game continues until one player has all the cards.

## How to Play

1. Clone the repository or download the `War.py` file.
2. Run the script using Python:

    ```
    python War.py
    ```

3. Follow the prompts to play the game.

## Rules of the Game

- Each player receives half of a standard deck of 52 playing cards.
- Players take turns comparing the top card of their deck.
- The player with the higher card wins both cards and adds them to their deck.
- In the event of a tie, a "war" is declared:
  - Both players place three cards face down and reveal the fourth card.
  - The player with the higher fourth card wins all cards on the table.
- The game continues until one player runs out of cards.

## Classes

### `Card`

Represents a playing card with a suit, rank, and value.

### `Deck`

Represents a deck of cards. It can shuffle the deck and deal cards to players.

### `Player`

Represents a player in the game. Each player has a name and a set of cards.

## Example

Here's an example of how the script works:

Round 1
Round 2
Round 3
...
Player One is out of cards
PLAYER TWO WINS!!!

In this example, Player One ran out of cards, and Player Two won the game.
