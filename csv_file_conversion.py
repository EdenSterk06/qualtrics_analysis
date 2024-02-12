import pandas as pd

def process_files(directory):
    # Initialize an empty DataFrame
    df = pd.DataFrame(columns=['lm', 'tm', 'tp', 'num_edge', 'num_shad', 'num_text'])

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Extract information from the file name
            parts = filename.split('_')
            lm, tm, tp = parts[0], parts[1], parts[2]

            # Append the information to the DataFrame
            df = df.append({'lm': lm,
                            'tm': tm,
                            'tp': tp,
                            'num_edge': '',
                            'num_shad': '',
                            'num_text': ''}, ignore_index=True)

    # Save the DataFrame to a CSV file
    df.to_csv('output.csv', index=False)

# Example usage:
process_files('33_81')

# Make sure to replace `'directory_of_files'` with the actual path to the directory.

# Will generate csv file