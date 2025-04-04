import pandas as pd

# Load the Excel files
mentee_file = 'mentee_data.xlsx'
mentor_file = 'mentor_data.xlsx'

# Load the mentee and mentor data into pandas DataFrames
mentee_df = pd.read_excel(mentee_file)
mentor_df = pd.read_excel(mentor_file)

# Function to pair mentees with mentors
def pair_mentors_and_mentees(mentee_df, mentor_df):
    pairs = []

    # Iterate over all mentees and mentors to find a match
    for mentee_index, mentee in mentee_df.iterrows():
        matched_mentor = None
        
        for mentor_index, mentor in mentor_df.iterrows():
            # Check if the mentee and mentor's preferred mentorship type matches
            if mentee['Preferred Mentorship Format'] in mentor['Preferred Mentorship Format']:

                # Further matching logic (based on skills, availability, etc.)
                if mentee['Interested in finding a new Career or Technical Mentor?'] in mentor['Skills to Share with a Mentee']:
                    if (mentee['Days Available'] == mentor['Days Available']) or (mentee['Preferred Mentorship Format'] == mentor['Preferred Mentorship Format']):
                        matched_mentor = mentor
                        break
        
        # If a match is found, add the pair to the list
        if matched_mentor is not None:
            pairs.append({
                'Mentee First Name': mentee['First Name'],
                'Mentee Last Name': mentee['Last Name'],
                'Mentee Email': mentee['Email Address'],
                'Mentor First Name': matched_mentor['First Name'],
                'Mentor Last Name': matched_mentor['Last Name'],
                'Mentor Email': matched_mentor['Email Address']
            })

    return pd.DataFrame(pairs)

# Pair mentors and mentees
matched_pairs = pair_mentors_and_mentees(mentee_df, mentor_df)

# Save the result to a new Excel file
matched_pairs.to_excel('mentor_mentee_pairs.xlsx', index=False)

print("Mentor-Mentee pairs have been successfully created and saved to 'mentor_mentee_pairs.xlsx'.")
