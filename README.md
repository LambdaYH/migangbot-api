# Market API

A REST API for retrieving market data for various games.

## Features

- Query market data for in-game items across different games
- Modular architecture for easy extension to other games/markets

## FFXIV Market API

- Query market data for any tradable item in FFXIV
- Filtering for high-quality (HQ) items only
- Data sourced from [Universalis](https://universalis.app/)

### GET /api/ffxiv/get_market_data

Get market data for a specific item on a specific server.

**Parameters:**

- `server_name` (string, required): The server name to query (e.g., "Moogle", "Tonberry")
- `item_name` (string, required): The item name to search for
- `hq` (boolean, optional, default: false): Filter for high-quality items only

**Example Response:**

```json
{
  "status": "success",
  "data": "Moogle 的 白银锭 数据如下：\n10,000x10 = 100,000   RetainerName\n11,000x5 = 55,000   RetainerName2\n...\n更新时间:2023-09-01 12:34:56"
}
```

## Project Structure

```
market-api/
├── ffxiv/                  # FFXIV specific code
│   ├── __init__.py         # Package initialization
│   ├── market.py           # Market data functions
│   └── routes.py           # API routes for FFXIV
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Setup and Installation

1. Clone the repository
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the API server
```
python main.py
```

The API will be available at http://localhost:8000

## Documentation

API documentation is automatically generated and available at http://localhost:8000/docs when the server is running. 