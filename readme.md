# WeatherBot

WeatherBot is a weather forecast bot that provides weather updates for a specified route. The bot is built using the aiogram library and supports multiple commands to interact with users.

## Features

- Get weather forecasts for a specified route
- Add intermediate points to the route
- Choose the forecast period

## Commands

- `/start` - Start the bot
- `/help` - Show help information
- `/weather` - Get the weather forecast

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/fuccsoc/WeatherBot.git
    ```
2. Navigate to the project directory:
    ```sh
    cd WeatherBot
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the bot:
    ```sh
    python main.py
    ```
2. Interact with the bot using the commands mentioned above.

## Configuration

Make sure to set your tokens in the `.env` file:
```py
TOKEN=your_telegram_bot_token_here
OPENWEATHER_TOKEN=your_openweather_token_here
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.