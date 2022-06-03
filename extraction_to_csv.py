import glob                 # used to check CSV files exist
import os.path              # used to check CSV files exist
import re                   # used to find words that are uppercase characters
import time                 # used to time the program throughout
import pandas as pd
from pathlib import Path


def get_words_from_text_dictionary(file_location: str, column_name: list) -> pd:
    file_data = open(file_location, "r")
    pattern = re.compile("^[A-Z]+$")
    df_words = pd.DataFrame(columns=column_name, dtype="string")
    for line in file_data:
        first_word = re.split('\\s', line)[0]
        if first_word.isupper() and pattern.match(first_word):
            df_words.loc[len(df_words)] = first_word
    file_data.close()
    df_words = df_words.drop_duplicates()
    return df_words


def create_data_csv_letters(df: pd):
    max_word_length = df.word.str.len().max()       # Get the maximum length word
    df['length'] = df.word.str.len()                # Add a word length column
    while max_word_length > 1:
        df1 = df[df['length'] == max_word_length]   # Creates a DataFrame of the chosen word length
        df2 = df1.word.str.split('', expand=True)   # Splits word into a string list of characters
        df2 = df2.iloc[:, 1:-1]         # Removes the first and last elements of the list of characters which are blank
        df3 = pd.concat([df1, df2], axis=1)         # Add the word+length DataFrame to the list of characters DataFrame
        csv_output_file = f"word_length_{max_word_length}_as_characters.csv"
        path_to_file = Path(folder_location + csv_output_file)
        if not path_to_file.is_file():
            df3.to_csv(folder_location + csv_output_file, index=False)
        max_word_length -= 1

        
start_extracting_timestamp = time.time()            # Get a timestamp of the start of the program, housekeeping purposes
folder_location = "data/"
input_text_file = "Websters_Unabridged_Dictionary.txt"  # use this dictionary file
data_words = get_words_from_text_dictionary(folder_location + input_text_file, ["word"])
create_data_csv_letters(data_words)

extracting_time_taken = time.time() - start_extracting_timestamp
print(f'Extracting data process took (seconds): {extracting_time_taken}')  # Print time taken for program to execute


#%%
