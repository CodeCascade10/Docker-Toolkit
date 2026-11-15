
# Stage 1: Build the Go application
FROM golang:1.25-alpine AS builder

WORKDIR /app

# Copy Go module files
COPY go.mod ./

# Download dependencies
RUN go mod download

# Copy application source
COPY main.go ./

# Compile a static Linux binary
RUN CGO_ENABLED=0 GOOS=linux go build -o app .


# Stage 2: Create a lightweight runtime image
FROM alpine:3.22

WORKDIR /app

# Copy compiled binary from builder
COPY --from=builder /app/app .

# Run the application
CMD ["./app"]
