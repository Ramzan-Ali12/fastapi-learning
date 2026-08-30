FastAPI Learning
│
├── What I learned
├── Project structure
├── API endpoints
├── How to run
├── Request examples
├── Response examples
├── Database
├── Authentication
└── Deployment


Current Architecture
                     FastAPI
                        │
             ┌──────────┴──────────┐
             │                     │
          Auth router          Product router
             │                     │
      POST /auth/login       GET /products/
             │               POST /products/
             │               GET /products/{id}
             │                     │
      username/password       get_current_user
             │                     │
             ↓                     ↓
       "valid_token"         Bearer token