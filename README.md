# Instructions for augmenting BERT-pair
Here you can find the code for BERT-pair with data augmentation. Keyboard augmentation, back translation and easy data augmentation.

Data Augmentation for a BERT-pair model. In order to use the code please follow the following steps:

1. Go to https://github.com/HSLCY/ABSA-BERT-pair and follow the steps on the github page. We use large parts of their code to run BERT-pair.
2. First run the benchmark model.
3. Then use the methods in the folder "data_augmentation" to create additional positive pairs.
5. After running the data augmentation you can use the additional positive pairs to train BERT-pair.

# Data Augmentation techniques

To use keyboard augmentation please correspond: https://nlpaug.readthedocs.io/en/latest/augmenter/char/keyboard.html
To use easy data augmentation please correspond: https://nlpaug.readthedocs.io/en/latest/augmenter/word/word.html
To use back translation please correspond: https://huggingface.co/docs/transformers/model_doc/marian
