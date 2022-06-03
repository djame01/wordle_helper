# wordle_helper

Little script to assist you in solving Wordle.

------------------

"extract_to_csv.py" - is used to:
1) extract the list of words from the "Websters_Unabridged_Dictionary.txt" file.
2) these words are grouped by word length and entered into a CSV file based on that word length.

Note:
1) It extracts all words of length 2 and above e.g. it will not extract the words "A" or "I" however it will extract "It" or "be".
2) It stores the words in a CAPITALISED format e.g., SAUSAGES and not Sausages.
3) It stores the words length.
4) It stores each letter individually in a column in CAPITALISED format.


------------------
"create_data.py" is used to:
1) Create the dataframes to be used from a CSV file.


------------------
"interface.py" is used to:

1) Prompt for user input to:
2) Create the dataframes to be analysed from the CSV files.
3) The dataframes created are all based on words of a user inputted length.
4) These dataframes are:     i)  the entire dictionary of words.      ii) words containing a user inputted particular text.
