FROM python:3.14-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (needed for yt-dlp/ffmpeg)
RUN apt update && apt install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy the bot code directory
COPY src/ ./src/

# Copy pyproject.toml and install Python dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Create downloads directory
RUN mkdir -p downloads

# Run the bot
CMD ["python", "-m", "tiktok_saver"]