
# Use lightweight Node.js base image
FROM node:22-alpine

# Set working directory
WORKDIR /app

# Set environment variables
ENV NODE_ENV=production

# Copy package files
COPY package*.json ./

# Install production dependencies
RUN npm ci --omit=dev

# Copy application source code
COPY app.js .

# Create non-root user
USER node

# Expose application port
EXPOSE 3000

# Start Node.js application
CMD ["npm", "start"]
