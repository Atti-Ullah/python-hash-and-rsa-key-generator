# Hash & RSA Key Generator

## Overview

This is a Flask-based web application that provides cryptographic utilities for generating hash values and RSA key pairs. The application offers a user-friendly interface for:

- Generating cryptographic hashes (MD5, SHA1, SHA256, SHA512) from text input
- Generating RSA key pairs with configurable key sizes (1024, 2048, 4096 bits)

The application is designed as a single-page web tool with a RESTful API backend, making it suitable for both interactive use through the browser and programmatic access via API endpoints.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Single-Page Application Design**
- The frontend is built using vanilla HTML, CSS, and JavaScript (implied from the templates structure)
- Uses a gradient purple color scheme (#667eea to #764ba2) for modern aesthetics
- Implements a responsive grid layout that adapts to different screen sizes (minmax 500px cards)
- CSS-in-HTML approach for styling, keeping everything self-contained

**Rationale**: A simple SPA approach minimizes complexity and dependencies while providing a clean, modern interface for cryptographic operations. The embedded CSS approach keeps the application lightweight and easy to deploy.

### Backend Architecture

**Flask Web Framework**
- Lightweight Python web framework chosen for simplicity
- RESTful API design with JSON request/response format
- Two main API endpoints:
  - `POST /generate_hash` - Hash generation endpoint
  - `POST /generate_rsa_keys` - RSA key pair generation endpoint
- Template rendering for the main page via `GET /`

**Rationale**: Flask provides a minimal but sufficient framework for this utility application. The separation of concerns (HTML template + JSON API endpoints) allows the backend to serve both web UI and potential API consumers.

**Cryptographic Processing**
- Hash generation uses Python's built-in `hashlib` library
- RSA key generation uses the `cryptography` library's hazmat primitives
- Supports multiple hash algorithms with configurable selection
- Supports multiple RSA key sizes (1024, 2048, 4096 bits)
- Key serialization using PEM format (implied from imports)

**Rationale**: Using established cryptographic libraries (hashlib, cryptography) ensures security and reliability. The hazmat (hazardous materials) layer provides low-level cryptographic primitives with fine-grained control over key generation and serialization.

**Input Validation**
- Hash endpoint validates presence of text input
- Hash endpoint validates hash type against allowed values
- RSA endpoint validates key size against allowed values (1024, 2048, 4096)
- Returns appropriate HTTP 400 errors for invalid inputs

**Rationale**: Input validation prevents errors and potential security issues from malformed requests.

### Data Storage

**No Persistent Storage**
- Application operates entirely in-memory
- No database or file storage for generated hashes or keys
- All operations are stateless

**Rationale**: As a cryptographic utility tool, there's no need to persist sensitive data like private keys or hash values. Users receive results immediately and are responsible for their own storage.

### Authentication & Authorization

**No Authentication**
- Application is publicly accessible
- No user accounts or session management

**Rationale**: This is a utility tool that doesn't handle sensitive user data (users provide their own input). Authentication would add unnecessary complexity for a public utility.

## External Dependencies

### Python Libraries

**Flask** (Web Framework)
- Purpose: HTTP server, routing, request/response handling, template rendering
- Used for: Core web application functionality

**cryptography** (Cryptographic Library)
- Purpose: RSA key generation and serialization
- Specific modules used:
  - `cryptography.hazmat.primitives.asymmetric.rsa` - RSA key generation
  - `cryptography.hazmat.primitives.serialization` - Key serialization to PEM format
  - `cryptography.hazmat.backends.default_backend` - Cryptographic backend

**hashlib** (Standard Library)
- Purpose: Cryptographic hash function implementations
- Supported algorithms: MD5, SHA1, SHA256, SHA512

### Runtime Environment

**Python 3.x Required**
- Application uses modern Python syntax and libraries
- No specific version constraint identified, but Python 3.6+ recommended for cryptography library compatibility

### Third-Party Services

**None**
- Application runs entirely self-contained
- No external API calls or service integrations
- No CDN dependencies visible (CSS/JS appear to be inline)