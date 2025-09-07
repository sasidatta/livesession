# Use Nginx as base image
FROM nginx:alpine

# Set maintainer label (optional)
LABEL maintainer="dattu2009@yahoo.com"

# Copy static site files into Nginx html directory
COPY ./mysite /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Nginx runs automatically (CMD is in base image)