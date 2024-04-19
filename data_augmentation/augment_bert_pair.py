from augmenters import (keyboard_augmentation,
                        copy_csv_file,
                        backtranslation,
                        easy_data_augmentation)
import pandas as pd
# Create new files for 12 positive pairs
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/ka/ka_train_NLI_16_12.csv')
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/bt/bt_train_NLI_16_12.csv')
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/eda/eda_train_NLI_16_12.csv')

# Create new files for 8 positive pairs
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/ka/ka_train_NLI_16_8.csv')
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/bt/bt_train_NLI_16_8.csv')
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/eda/eda_train_NLI_16_8.csv')

# Create new files for 4 positive pairs
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/ka/ka_train_NLI_16_4.csv')
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/bt/bt_train_NLI_16_4.csv')
copy_csv_file('../data/semevaldata/bert-pair/train_NLI_16.csv',
              '../data/semevaldata/bert-pair/eda/eda_train_NLI_16_4.csv')

# Augment data for 12 positive pairs
keyboard_augmentation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                      '../data/semevaldata/bert-pair/ka/ka_train_NLI_16_12.csv',
                      low_freq_min=1, low_freq_max=50, k=12)

backtranslation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                '../data/semevaldata/bert-pair/bt/bt_train_NLI_16_12.csv',
                low_freq_min=1, low_freq_max=50, k=12)

easy_data_augmentation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                       '../data/semevaldata/bert-pair/eda/eda_train_NLI_16_12.csv',
                       low_freq_min=1, low_freq_max=50, k=12)

# Augment data for 8 positive pairs
keyboard_augmentation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                      '../data/semevaldata/bert-pair/ka/ka_train_NLI_16_8.csv',
                      low_freq_min=1, low_freq_max=50, k=8)

backtranslation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                '../data/semevaldata/bert-pair/bt/bt_train_NLI_16_8.csv',
                low_freq_min=1, low_freq_max=50, k=8)

easy_data_augmentation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                       '../data/semevaldata/bert-pair/eda/eda_train_NLI_16_8.csv',
                       low_freq_min=1, low_freq_max=50, k=8)

# Augment data for 4 positive pairs
keyboard_augmentation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                      '../data/semevaldata/bert-pair/ka/ka_train_NLI_16_4.csv',
                      low_freq_min=1, low_freq_max=50, k=4)

backtranslation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                '../data/semevaldata/bert-pair/bt/bt_train_NLI_16_4.csv',
                low_freq_min=1, low_freq_max=50, k=4)

easy_data_augmentation('../data/semevaldata/ABSA-16_SB1_Restaurants_Train_Data.xml',
                       '../data/semevaldata/bert-pair/eda/eda_train_NLI_16_4.csv',
                       low_freq_min=1, low_freq_max=50, k=4)


