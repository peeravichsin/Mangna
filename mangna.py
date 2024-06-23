
import argparse
from datetime import datetime
import dictionaries

# Configuration settings
CONNECT_CHAR = dictionaries.connect_char

def connect_words(word_list, connect_char):
    connected_words = []
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if i != j:
                for char in connect_char:
                    concatenated_string = word_list[i] + char + word_list[j]
                    connected_words.append(concatenated_string)
    return connected_words

def read_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except IOError:
        print(f"Error: File '{file_path}' not found or cannot be read.")
        return []

def mangna(source, connect, include_suffixes, include_years):

    word_variants = []
    current_year = datetime.now().year
    
    # Connect words if requested
    if connect:
        source = connect_words(source, CONNECT_CHAR)
    
    # Iterate through each word in source
    for wrd in set(map(str.strip, map(str.lower, source))):
        # Add base word variant
        base_word = wrd
        
        # Generate variants for connected words
        for connected_word in source:
            variant = connected_word
            
            # Add suffix variants if requested
            if include_suffixes:
                for suffix in dictionaries.suffixes:
                    variant_with_suffix = variant + suffix
                    
                    # Add year variants if requested
                    if include_years:
                        for i in range(current_year - 100, current_year + 1):
                            word_variants.append(variant_with_suffix + str(i))
                    else:
                        word_variants.append(variant_with_suffix)
            
            # Add year variants if requested (without suffixes)
            elif include_years:
                for i in range(current_year - 100, current_year + 1):
                    word_variants.append(variant + str(i))
            
            # Add base variant (no suffixes or years)
            else:
                word_variants.append(variant)
    
    return list(set(word_variants))

def save_to_file(output_list, file_path):
    try:
        with open(file_path, 'w') as file:
            for item in output_list:
                file.write(item + '\n')
        print(f"Output saved to {file_path}")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'")

def calculate_output_count(words, connect, include_suffixes, include_years):
    if connect:
        source = connect_words(words, CONNECT_CHAR)
    else:
        source = words
    
    num_base_words = len(source)
    num_connected_words = num_base_words * (len(source) - 1)  # Each word can connect with every other word
    
    if include_suffixes and include_years:
        num_variants_per_word = len(dictionaries.suffixes) * (1 + 101)
    elif include_suffixes:
        num_variants_per_word = len(dictionaries.suffixes)
    elif include_years:
        num_variants_per_word = 101
    else:
        num_variants_per_word = 1
    
    total_output = num_base_words + num_connected_words * num_variants_per_word
    
    # Format total_output with commas for better readability
    formatted_output = "{:,}".format(total_output)
    
    return formatted_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate concatenated words and variants")
    parser.add_argument("-i", "--input-file", required=True, help="Text file containing words (one per line)")
    parser.add_argument("-o", "--output-file", default="output.txt", help="Output file to save generated lines (default: output.txt)")
    parser.add_argument("-c", "--connect", action="store_true", help="Connect generated words first")
    parser.add_argument("-s", "--suffixes", action="store_true", help="Include suffix variants")
    parser.add_argument("-y", "--years", action="store_true", help="Include year variants")
    
    args = parser.parse_args()
    
    # Determine default behavior if no specific arguments are provided
    if not args.connect and not args.suffixes and not args.years:
        args.suffixes = True  # Default behavior: Include suffix variants
    
    Mang_list = read_words_from_file(args.input_file)

    # Warn and prompt user if all three options (-c, -s, -y) are present
    if args.connect and args.suffixes and args.years:
        output_count = calculate_output_count(Mang_list, args.connect, args.suffixes, args.years)
        print(f"\033[91mWarning: You have selected to include suffixes, years, and connect words, which will generate {output_count} output variants.  And this Operation will cause Memory Error !!!\033[0m")
        decision = input("Do you want to continue? (Yes/No): ").strip().lower()
        
        if decision != 'yes':
            print("Operation aborted.")
            exit()

    # Adjust behavior if only -c (connect) is provided without --suffixes
    if args.connect and not args.suffixes and not args.years:
        generated_lines = mangna(Mang_list, args.connect, False, False)
    else:
        generated_lines = mangna(Mang_list, args.connect, args.suffixes, args.years)

    save_to_file(generated_lines, args.output_file)