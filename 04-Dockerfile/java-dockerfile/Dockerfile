
# Stage 1: Build the Java application
FROM eclipse-temurin:21-jdk-alpine AS builder

WORKDIR /app

# Copy Java source code
COPY src/ ./src/

# Compile the application
RUN javac -d out src/Main.java


# Stage 2: Run the application
FROM eclipse-temurin:21-jre-alpine

WORKDIR /app

# Copy compiled classes from builder stage
COPY --from=builder /app/out ./out

# Run the Java application
CMD ["java", "-cp", "out", "Main"]
