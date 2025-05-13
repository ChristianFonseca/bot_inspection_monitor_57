# Samsung Monitor Availability Bot

This bot monitors the availability of 57-inch Samsung monitors on the official Samsung Peru store and sends notifications when products are available.

## Features

- Automated monitoring of Samsung monitors page
- Notifications via AWS SNS when products are available
- Headless execution (no graphical interface)
- Configuration through environment variables
- Docker support for easy deployment

## Requirements

- Python 3.x
- Chrome/Chromium
- ChromeDriver
- AWS account with SNS access
- Docker (optional, for containerized deployment)

## Dependencies

```
selenium
beautifulsoup4
boto3
python-dotenv
```

## Configuration

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in a `.env` file:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
SNS_TOPIC_ARN=your_topic_arn
```

## Usage

### Local Execution
To run the bot locally:

```bash
python local/bot.py
```

### Docker Deployment
To run the bot using Docker:

1. Build the Docker image:
```bash
docker build -t samsung-monitor-bot .
```

2. Run the container:
```bash
docker run samsung-monitor-bot
```

## Project Structure

- `app.py`: Main bot script
- `.env`: Configuration file (not included in repository)
- `requirements.txt`: Dependencies list
- `Dockerfile`: Container configuration
- `local/`: Directory containing local execution scripts
- `notebooks/`: Directory containing developing notebooks.

## Notes

- The bot is configured to specifically monitor 57-inch monitors on the Samsung Peru store
- Notifications are sent through AWS SNS when available products are detected
- It's recommended to run the bot periodically using a task scheduler (cron, etc.)
- When using Docker, all dependencies including Chrome and ChromeDriver are automatically installed in the container
