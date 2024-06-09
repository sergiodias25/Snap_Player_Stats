import json

def get_CardUnlockHistory(cardUnlockHistory):
    # Process the cardUnlockHistory list into the required format
    card_list = []

    for card in cardUnlockHistory:
        # Assuming the card names are in the format provided
        card_list.append(card)
    
    return generate_card_unlock_history(card_list)

def generate_card_unlock_history(cards):
    # Number of columns
    num_columns = 3
    # Split cards into columns
    columns = [[] for _ in range(num_columns)]
    for i, card in enumerate(cards):
        columns[i % num_columns].append(card)

    # Create HTML for columns
    html_columns = '<table style="width: 100%;"><tr>'
    for col in columns:
        html_columns += '<td class="variant-column">'
        html_columns += "<br>".join(col)
        html_columns += '</td>'
    html_columns += '</tr></table>'

    return html_columns

# Example usage
cardUnlockHistory = [
    "1: Jessica Jones", "2: Ka Zar", "4: Mr Fantastic", "6: Spectrum",
    "8: Nightcrawler", "10: Wolfsbane", "12: White Tiger", "14: Odin",
    "18: Groot", "22: Angel", "26: Multiple Man", "30: Onslaught"
    # Add more cards as required
]

card_unlock_history_html = get_CardUnlockHistory(cardUnlockHistory)
print(card_unlock_history_html)