# Entity Labeling and CoNLL Format Generation

This repository is developed collaboratively by `Getahun Tiruneh` and `Marta Assefa` to create tools for dynamic entity labeling of Amharic messages and generate CoNLL formatted outputs. It is designed for processing data fetched from the `Qenash.com - ቅናሽ` e-commerce channel, specifically targeting price, location, and product entities. The repository allows for dynamic batching of messages for labeling and exporting labeled data in the CoNLL format.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Entity Labeling](#entity-labeling)
  - [Generate CoNLL Output](#generate-conll-output)
  - [Dynamic Batching](#dynamic-batching)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Entity Labeling**: Automatically labels entities such as prices, locations, and products in Amharic messages.
- **CoNLL Format Generation**: Produces output in the standard CoNLL format for NLP tasks.
- **Dynamic Batching**: Allows flexible generation of labeled data from custom message ranges (e.g., 0-50, 51-100, etc.).
- **Amharic Language Support**: Handles Amharic text preprocessing, including the removal of emojis, special characters, and punctuation.

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/getahunTiruneh/Ethio-Mart-Collaboration.git
cd Ethio-Mart-Collaboration
