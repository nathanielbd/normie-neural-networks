# normie-neural-networks

Do you like memes's (DULM) Normie Test is a quiz with ~40 questions that places the taker on a two-axes plot relative to internet culture personality architypes like 'normies' and 'simps.' Notably, the quiz is not open source and it runs on server-side PHP.

Scraped data can be found in `data-with-stats.csv`. Data with random hidden answers to the statistical questions (sex, height, attractiveness, ..., climate) can be found in `data.csv`. Data with fixed answers (male, defaults) to the statistical questions can be found in `data.csv`. Details to replicate these can be found in `script.js`.

See `experiment.ipynb` for data exploration, reverse-engineering of the weights using a multilayer perceptron.

See `x_weights.csv` and `y_weights.csv` for the reverse-engineered weights for the question answers.