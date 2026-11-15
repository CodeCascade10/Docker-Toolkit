
const express = require("express");

const app = express();

const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Home route
app.get("/", (req, res) => {
    res.json({
        message: "Hello from Node.js Docker!",
        status: "Running successfully",
        technology: "Node.js + Express + Docker"
    });
});

// About route
app.get("/about", (req, res) => {
    res.json({
        application: "Node.js Docker Demo",
        version: "1.0.0",
        environment: process.env.NODE_ENV || "development"
    });
});

// Health check route
app.get("/health", (req, res) => {
    res.status(200).json({
        status: "healthy"
    });
});

// Users route
app.get("/users", (req, res) => {
    const users = [
        { id: 1, name: "Alice" },
        { id: 2, name: "Bob" },
        { id: 3, name: "Charlie" }
    ];

    res.json({
        users: users
    });
});

// Start server
app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
});
