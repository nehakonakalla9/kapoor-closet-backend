
- Database transaction for checkout
- Product price snapshot stored in OrderItem
- Historical orders are unaffected by future price changes

</details>

<details>
<summary>💳 Razorpay Payments</summary>

Razorpay is integrated in test mode.
Create Order
↓
Create Razorpay Order
↓
Frontend Payment
↓
Payment Completed
↓
Signature Verification
↓
Order + Payment Updated



```http
POST /api/orders/<id>/create_payment/
POST /api/orders/<id>/verify_payment/
```

The backend verifies the Razorpay signature before marking the order as paid.

</details>

---

## 🔌 API Overview

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/register/` | Register & send OTP |
| POST | `/api/verify/` | Verify OTP & create user |
| GET | `/api/products/` | Browse products |
| GET/POST/DELETE | `/api/wishlist/` | Manage wishlist |
| GET/POST/PATCH/DELETE | `/api/cart/` | Manage cart |
| POST | `/api/orders/checkout/` | Create order |
| POST | `/api/orders/<id>/create_payment/` | Create Razorpay order |
| POST | `/api/orders/<id>/verify_payment/` | Verify payment |

🔒 Authenticated endpoints require a valid JWT.

---

## 🗄️ Backend Flow

                ┌──────────────┐
                │    User      │
                └──────┬───────┘
                       │
                JWT Authentication
                       │
    ┌──────────────────┼──────────────────┐
    ↓                  ↓                  ↓
Products           Wishlist             Cart
                                          │
                                          ↓
                                      Checkout
                                          │
                                          ↓
                                        Order
                                          │
                                          ↓
                                     Razorpay
                                          │
                                          ↓
                                 Signature Verify




---

## 🚀 Local Setup

**1. Clone**
```bash
git clone https://github.com/nehakonakalla9/kapoor-closet-backend.git
cd kapoor-closet-backend
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env`**
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/kapoor_closet
RESEND_API_KEY=your_resend_key
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
CORS_ALLOWED_ORIGINS=http://localhost:3000



**5. Run**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## ⚠️ Known Limitations

<details>
<summary>📧 Email</summary>

Resend currently uses its shared test sender, so OTP emails can only reach the Resend account owner's email.

Production improvement: verify a real domain with Resend.

</details>

<details>
<summary>🖼️ Media Storage</summary>

Media is currently served directly by Django. For production, this should be moved to S3, Cloudinary, or similar object storage.

</details>

<details>
<summary>👤 Admin</summary>

The catalog is managed by a single Django admin. There is no seller onboarding or multi-vendor system.

</details>

<details>
<summary>☁️ Hosting</summary>

The project uses Render's free tier, so the service can experience cold starts and free-tier database lifecycle limitations.

</details>

<details>
<summary>🧪 Testing</summary>

The API was tested manually using Postman. An automated test suite has not yet been added.

</details>

---

## 🔮 Future Scope

- [ ] Verify production email domain
- [ ] Move media to cloud storage
- [ ] Add order history & order details
- [ ] Add restock notifications
- [ ] Add refund/cancellation handling
- [ ] Add seller/admin role separation
- [ ] Add automated tests
- [ ] Add database seed scripts/fixtures

---

## 🧠 What I'd Do Differently

**Production email earlier**
The Resend sandbox restriction was discovered after building the OTP flow. A verified domain should have been configured earlier.

**Production media storage from the start**
Local media storage worked during development but caused issues after deployment. Cloud storage should have been part of the initial deployment design.

**Database seeding**
Development and production databases were not intentionally kept in sync. Seed scripts/fixtures would make deployment and recovery much easier.

---

## 📚 What This Project Demonstrates

- Django REST Framework
- REST API design
- JWT authentication
- OTP verification
- PostgreSQL data modeling
- Database transactions
- Cart & order workflows
- Razorpay payment integration
- Payment signature verification
- Environment-based configuration
- CORS
- Production deployment & debugging

---

## 🔗 Related

- Frontend: https://github.com/nehakonakalla9/kapoor-closet-frontend
- Live Site: https://kapoor-closet-frontend.vercel.app
- Backend API: https://kapoor-closet-backend.onrender.com/api/
