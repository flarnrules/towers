#!/bin/bash
export STARSD_KEYRING_BACKEND=file

# transaction is saved here
TRANSACTIONS_DIR="../data/transactions"

# if you are starting fresh, this makes directory if directory not there
mkdir -p $TRANSACTIONS_DIR

# royalties calculation
PYTHON_SCRIPT_PATH="/home/flarnrules/repos/towers/collections/2-proto_towers/code/scripts/royalties.py"

# run the Python script and capture the output
echo "Generating transaction data..."
OUTPUT=$(echo -e "y\ny" | python $PYTHON_SCRIPT_PATH)

# print the entire output to debug
echo "Full output from Python script:"
echo "$OUTPUT"

# extract the last line, assuming it's the JSON file path
# json file is created by roylaties.py
JSON_FILE=$(echo "$OUTPUT" | tail -n 1)

# Validate JSON file existence
if [ ! -f "$JSON_FILE" ]; then
    echo "JSON file not found: $JSON_FILE"
    exit 1
fi

echo "Generated JSON file: $JSON_FILE"

# parameters for the transactio
# you need to name your wallet
KEY_NAME="royalties"
CHAIN_ID="stargaze-1"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# confirm if wanna sign, and then sign
read -p "Are you sure you want to sign the transaction? (y/n) " confirm_sign
if [[ "$confirm_sign" == "y" || "$confirm_sign" == "Y" ]]; then
    SIGN_OUTPUT="${TRANSACTIONS_DIR}/signed_tx_${TIMESTAMP}.json"
    echo "Signing the transaction using file: $JSON_FILE"

    # here is the actual use of the starsd CLI!!!!!!
    starsd tx sign "$JSON_FILE" --from "$KEY_NAME" --chain-id "$CHAIN_ID" --output-document "$SIGN_OUTPUT"

    # check if the signing was successful
    if [ $? -ne 0 ]; then
        echo "Error signing the transaction"
        exit 1
    fi
else
    echo "Transaction signing cancelled."
    exit 0
fi

# confirm if wanna broadcast, and then broadcast
read -p "You will broadcast this transaction, are you sure you want to proceed? (y/n) " confirm_broadcast
if [[ "$confirm_broadcast" == "y" || "$confirm_broadcast" == "Y" ]]; then
    
    echo "Broadcasting the signed transaction..."
    starsd tx broadcast "$SIGN_OUTPUT"

    # check if broadcast worked
    if [ $? -ne 0 ]; then
        echo "Error broadcasting the transaction"
        exit 1
    fi
else
    echo "Transaction broadcasting cancelled."
    exit 0
fi
