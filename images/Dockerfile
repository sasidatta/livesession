# Use a lightweight base image
FROM alpine:3.4

# Set maintainer label (optional)
LABEL maintainer="yourname@example.com"

# Install a small package for demonstration
RUN apk add --no-cache curl bash

# Set working directory
WORKDIR /app

# Copy any local files (optional)
COPY . /app

# Default command
CMD ["sh", "-c", "echo Hello from simple Docker image! && sleep 3600"]
