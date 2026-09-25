# 🛍️ Kapoor's Closet — Backend

A Django REST Framework backend for an e-commerce platform inspired by the celebrity-closet resale concept of Kardashian Kloset.

Built as a portfolio project to practice:

- Backend/API architecture
- Authentication flows
- Database design
- Cart & order workflows
- Payment integration
- Production deployment

---

## 🔗 Project Links

| | Link |
|---|---|
| 🚀 **Live API** | [kapoor-closet-backend.onrender.com/api](https://kapoor-closet-backend.onrender.com/api/) |
| 💻 **Frontend Repository** | [github.com/nehakonakalla9/kapoor-closet-frontend](https://github.com/nehakonakalla9/kapoor-closet-frontend) |
| 🌐 **Live Website** | [kapoor-closet-frontend.vercel.app](https://kapoor-closet-frontend.vercel.app) |

> **Note:** The backend is hosted on Render's free tier.  
> The first request after ~15 minutes of inactivity may take **30–60 seconds** while the service spins back up.

---

## ✨ Overview

**Kapoor's Closet** is a sample e-commerce platform where users can browse a curated catalog of clothing items, wishlist products, manage their cart, and complete checkout using Razorpay.

The project is modeled around a **celebrity closet resale** concept.

> ⚠️ Product images use photos of the Kapoor family as sample portfolio data.  
> This project is intended for demonstration purposes and is **not intended for public commercial distribution**.

### 🔐 Authentication-first architecture

Anonymous browsing is intentionally disabled.

Users must:

1. Register with their details
2. Receive a verification OTP
3. Verify their email
4. Receive JWT access + refresh tokens
5. Use the authenticated API

Once verified, users can:

- 🛍️ Browse products
- ❤️ Manage wishlist
- 🛒 Manage cart
- 💳 Checkout
- 💰 Complete payment

---

# 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django |
| API | Django REST Framework |
| Database | PostgreSQL |
| Authentication | JWT — Simple JWT |
| Email | Resend |
| Payments | Razorpay — Test Mode |
| Hosting | Render |
| Frontend | Next.js / React |
| API Testing | Postman |
| Version Control | Git / GitHub |

---

# 🚀 Features

<details>
<summary><strong>🔐 Registration & Email Verification</strong></summary>

<br>

The application uses an OTP-based registration flow instead of traditional password authentication.

### Registration flow

```text
Registration Details
        ↓
POST /api/register/
        ↓
OTP Generated
        ↓
OTP Sent via Resend
        ↓
POST /api/verify/
        ↓
User Created
        ↓
JWT Access + Refresh Tokens
