# Use a Ruby base image suitable for Jekyll
FROM ruby:3.2.2-slim-bullseye

# Install build tools and Node.js
RUN apt-get update && apt-get install -y     build-essential     nodejs     && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install Jekyll and Bundler
RUN gem install jekyll bundler

# Copy the current directory into the container
# This will be overridden by the volume mount in docker-compose for development
COPY . .

# Expose port 4000 for Jekyll serve (if you decide to use it later)
EXPOSE 4000

# Default command to run Jekyll build
CMD ["jekyll", "build"]