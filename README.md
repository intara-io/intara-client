# Intara Python Client

## Installation

To install the package, use the following command:

### pip
```bash
pip install git+https://github.com/intara-io/intara-client
```

### poetry

```bash
poetry add git+https://github.com/intara-io/intara-client
```

## Usage

### Importing and Initializing the Client

```python
from intara_client.client import IntaraClient

client = IntaraClient(api_key="YOUR_API_KEY")
```

### SERP Data Retrieval

Retrieve SERP data for a given keyword.

```python
serp_data = client.serp("pizza")
print(serp_data[0])
```

**Example Output:**

```python
{
  'id': 'a9ed4c2f-0b7b-4aa8-b017-0140e28c1476',
  'fetched_at': '2024-09-13T20:02:19.963084Z',
  'type': 'organic',
  'rank_group': 1,
  'rank_absolute': 1,
  'position': 'left',
  'title': 'Pizza Hut | Delivery & Carryout - No One OutPizzas The Hut!',
  'domain': 'www.pizzahut.com',
  'url': 'https://www.pizzahut.com/',
  'description': 'Discover classic & new menu items, find deals and enjoy seamless ordering for delivery and carryout. No One OutPizzas the Hut®.',
  'is_paid': False,
  'rating_value': None,
  'rating_votes_count': None,
  'rating_max': None,
  'keyword_serp': '75301203-ee30-4a8e-b27c-9564d8ee4c58'
}
```

#### Using `location_code`

You can specify a `location_code` to get location-specific SERP data.

```python
# Using a specific location code (e.g., New York State)
serp_data = client.serp("pizza", location_code=21167)
print(serp_data[0])
```

**Example Output:**

```python
{
  'id': '8302e991-d44e-45f6-b7cb-072c4140bfe0',
  'fetched_at': '2024-09-14T11:02:41.100561Z',
  'type': 'local_pack',
  'rank_group': 1,
  'rank_absolute': 1,
  'position': 'left',
  'title': "Franco's Pizzeria and Deli",
  'domain': None,
  'url': None,
  'description': 'Syracuse, NY \nLate-night Italian & American eatery \n',
  'is_paid': False,
  'rating_value': 3.8,
  'rating_votes_count': 958,
  'rating_max': 5.0,
  'keyword_serp': 'f27a15c7-4838-47da-b857-92c893b2a860'
}
```

### Monthly Search Volume (MSV)

Retrieve MSV data for a given keyword.

```python
# Single keyword
msv_data = client.msv("pizza")
print(msv_data)
```

**Example Output:**

```python
{
  'id': 'e5620899-8917-4f04-bb01-dbc9cb634e0c',
  'keyword': 'pizza',
  'location_code': 2840,
  'language_code': 'en',
  'search_partners': False,
  'competition': 'LOW',
  'competition_index': 7,
  'search_volume': 7480000,
  'low_top_of_page_bid': 1.41,
  'high_top_of_page_bid': 2.87,
  'cpc': 2.61,
  'last_updated': '2024-09-13T20:02:42.885518Z'
}
```

#### Using `location_code`

```python
# Using a specific location code (e.g., New York State)
msv_data = client.msv("pizza", location_code=21167)
print(msv_data)
```

**Example Output:**

```python
{
  'id': 'a5f48e62-d3b7-49cc-bd05-f73ad869078c',
  'keyword': 'pizza',
  'location_code': 21167,
  'language_code': 'en',
  'search_partners': False,
  'competition': 'LOW',
  'competition_index': 7,
  'search_volume': 7480000,
  'low_top_of_page_bid': 1.41,
  'high_top_of_page_bid': 2.87,
  'cpc': 2.61,
  'last_updated': '2024-09-14T11:04:37.793329Z'
}
```

### Alpha Parser

```python
parsed_data = client.alpha_parser(
    url="https://www.zocdoc.com/acupuncturists/dallas-211240pm",
    industry="Healthcare"
)
print(parsed_data)
```

**Important:** The `industry` argument is case-sensitive.

#### Refreshing Cache

By default, the alpha parser may return results generated with cached HTML. To force an HTML refresh, set `disable_cache` to `True`.

```python
parsed_data = client.alpha_parser(
    url="https://www.zocdoc.com/acupuncturists/dallas-211240pm",
    industry="Healthcare",
    disable_cache=True
)
```

## Location Codes

The `location_code` parameter is used to specify the geographical location for SERP and MSV data. You can find the appropriate `location_code` from the `locations_us.csv` or `locations_all.csv` files.
