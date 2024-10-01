# Entity Labeling and CoNLL Format Generation

This repository is developed collaboratively by `Getahun Tiruneh` and `Marta Assefa` to create tools for dynamic entity labeling of Amharic messages and generate CoNLL formatted outputs. It is designed for processing data fetched from the `Qenash.com - ቅናሽ` e-commerce channel, specifically targeting price, location, and product entities. The repository allows for dynamic batching of messages for labeling and exporting labeled data in the CoNLL format.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Entity Labeling](#entity-labeling)
  - [Generate CoNLL Output](#generate-conll-output)
  - [Dynamic Batching](#dynamic-batching)
- [Data Source](#data-source)
- [Conclusion](#conclusion)
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
```
## Usage

### Entity Labeling

The entity labeling feature tags tokens in Amharic messages as belonging to one of the following categories:

- **B-PRICE / I-PRICE**: Price-related entities.
- **B-LOC / I-LOC**: Location-related entities.
- **B-PRODUCT / I-PRODUCT**: Product-related entities.
- **O**: Outside any entity.

Here’s how you can label entities in a sample message:

```python
from entity_labeler import EntityLabeler

# Initialize the entity labeler
labeler = EntityLabeler()

# Sample message
message = "ብር 500 ዋጋ በመገናኛ ምርት"

# Label entities
labeled_entities = labeler.label_entities(message)
print(labeled_entities)
```
## Data Source

The data processed in this repository is fetched from the [Qenash.com - ቅናሽ](t.me/qnashcom) e-commerce channel. This platform provides a variety of e-commerce data, and we focus on labeling entities related to prices, locations, and products from these messages.

## Conclusion

This project will contribute to improving the automated extraction of entities from Amharic text in e-commerce messages, thereby enhancing data analysis capabilities in the Ethiopian e-commerce landscape. The structured approach outlined in this document ensures that each task is comprehensively addressed, leading to a robust NER system that is interpretable and reliable. Despite the challenges faced, this project provides valuable insights and methodologies for future research and application in the field of NER for Amharic and similar languages.
Several models were trained, including XLM-Roberta-base, DistilBERT-base-uncased, and BERT-base-multilingual-cased, using the Hugging Face Trainer API. After tokenizing the data and aligning labels, models were fine-tuned and evaluated based on metrics such as precision, recall, F1 score, and accuracy. Among the models, XLM-Roberta-base performed the best with an F1 score of 0.93 and an accuracy of 99.6%, making it the most suitable model for this entity extraction task.

## Contributing

This project is collaboratively developed by **`Getahun Tiruneh`** and **`Marta assefa`**. If you'd like to contribute, feel free to submit issues or pull requests for any improvements or feature requests.

