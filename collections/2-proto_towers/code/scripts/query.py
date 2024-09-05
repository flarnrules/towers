import requests
import json

# proto towers stars120pue6syyajg6wtj0339qa42a279xaj8km889lgx2lvw325leevs2s79h2
# babu stars1nyfn4p8x5a8ysc5t6umgaxuety6x8g6me3hyt4vx6svmh8695m8qqkdqy3

def query_collection():
    address = 'stars120pue6syyajg6wtj0339qa42a279xaj8km889lgx2lvw325leevs2s79h2'  # Hardcoded address here
    url = 'https://graphql.mainnet.stargaze-apis.com/graphql'
    query = """
    query Query($address: String!) {
        collection(address: $address) {
            floorPrice
            offers {
                offerPrice {
                    amount
                }
            }
        }
    }
    """
    variables = {"address": address}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    
    if response.status_code == 200:
        data = response.json()['data']['collection']
        floor_price = int(data['floorPrice']) / 1_000_000 if data['floorPrice'] is not None else 0
        offers = [int(offer['offerPrice']['amount']) for offer in data['offers'] if offer['offerPrice']]
        top_offer = max(offers) / 1_000_000 if offers else 0
        return floor_price, top_offer
    else:
        raise Exception("Failed to query data")

if __name__ == "__main__":
    floor, offer = query_collection()
    print(f"Floor: {floor} STARS, Top Offer: {offer} STARS")
