Kapoor's Closet — Backend

A Django REST Framework backend for an e-commerce platform modeled on Kardashian Kloset, built as a portfolio project to practice backend/API design, authentication flows, and payment integration.

Live API: https://kapoor-closet-backend.onrender.com/api/ Frontend repo: https://github.com/nehakonakalla9/kapoor-closet-frontend Live site: https://kapoor-closet-frontend.vercel.app

Note: hosted on Render's free tier. The first request after 15 minutes of inactivity can take 30–60 seconds while the service spins back up.

Overview

Kapoor's Closet is a sample e-commerce site where users browse a catalog of items (styled as a celebrity closet resale concept), wishlist and cart items, and check out with real payment processing via Razorpay. Product images use photos of the Kapoor family as sample data — this is a portfolio piece, not intended for public distribution.

Login is required for all browsing (no anonymous access) — verified users can browse, wishlist, add to cart, and pay.

Tech Stack
Framework: Django + Django REST Framework
Database: PostgreSQL
Auth: JWT (djangorestframework-simplejwt), access + refresh tokens
Email: Resend (HTTP-based transactional email API)
Payments: Razorpay (test mode)
Hosting: Render (web service + managed Postgres)
Features
Registration & verification: Email + OTP based signup (no password auth). Registration collects first name, last name, email, and mobile number; a 4-digit OTP is emailed and must be verified before a real user account is created.
Product catalog: Read-only API with category filtering, nested Category → Style → Product hierarchy, image support.
Wishlist: Authenticated users can wishlist products, view their list, and remove entries.
Cart: Add/update/remove items, with stock validation against product quantity.
Checkout: Converts a cart into an Order + OrderItems (with price snapshotting so later price changes don't affect old orders), wrapped in a atomic transaction.
Payments: Razorpay order creation, checkout handoff, and cryptographic signature verification on payment completion, updating Order and Payment status together.
Admin-managed catalog: Products are added via Django admin by the site owner; there is no seller-facing flow.
API Structure (high level)
POST /api/register/ — submit registration details, triggers OTP email
POST /api/verify/ — verify OTP, creates user, returns JWT tokens
GET /api/products/ — list products (supports ?category= filter), auth required
GET/POST/DELETE /api/wishlist/ — manage wishlist, auth required
GET/POST/PATCH/DELETE /api/cart/ — manage cart, auth required
POST /api/orders/checkout/ — convert cart to order
POST /api/orders/<id>/create_payment/ — create Razorpay order for a given order
POST /api/orders/<id>/verify_payment/ — verify Razorpay payment signature and mark order paid
Setup (local)
bash
git clone https://github.com/nehakonakalla9/kapoor-closet-backend.git
cd kapoor-closet-backend
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt

Create a .env file in the project root with:

SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/kapoor_closet
RESEND_API_KEY=your_resend_key
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
CORS_ALLOWED_ORIGINS=http://localhost:3000

Then:

bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Known Limitations
OTP emails only reach the Resend account owner's inbox. Email delivery uses Resend's shared test sender (onboarding@resend.dev), which restricts sending to the account holder's own address only. Sending to arbitrary recipients (i.e. letting other people actually register) requires verifying a real domain on Resend, which wasn't set up for this portfolio project. In practice, this means only the developer's own email can currently complete registration end to end.
Media files are served directly by Django in production (via django.views.static.serve), which Django explicitly recommends against at scale. This was a pragmatic choice for a small portfolio project rather than setting up cloud storage (e.g. S3, Cloudinary) or a dedicated static file server.
No out-of-stock wishlist notifications. Wishlisting a sold-out item doesn't currently trigger any restock alert — considered and deliberately deferred.
No idle session timeout. JWT access/refresh token expiry is the only session boundary; an earlier plan to add a 10-minute inactivity timeout was dropped as unnecessary complexity for this scope.
Single admin, no seller onboarding. All product management goes through Django admin by one superuser; there's no multi-seller support.
Cart is one-of-each only. Since catalog items are modeled as unique/limited-quantity pieces, the cart doesn't support quantity > 1 of the same product.
Free-tier hosting constraints: Render's free web service spins down after inactivity (cold start delay), and its free Postgres database has its own lifecycle limits — something to be mindful of if reviving this project after a long gap.
Future Scope
Verify a real domain on Resend to allow registration from any email address.
Move media storage to a cloud provider (S3/Cloudinary) instead of local disk serving.
Add order history / order detail views for users.
Add restock notifications for wishlisted out-of-stock items.
Add refund/cancellation handling to the Order/Payment flow (currently only pending/paid/failed states exist).
Consider a lightweight seller/admin role separation if the catalog ever needs multiple contributors.
Add automated tests (the project was tested manually via Postman throughout development; no test suite currently exists).
What I'd do differently
Set up production email (a verified sending domain) earlier, rather than discovering the sandbox restriction after the rest of the flow was built and deployed.
Configure media/static file handling for production from the start, instead of retrofitting it after images silently failed to load post-deploy.
Keep local and deployed databases in sync intentionally (e.g. via seed scripts or fixtures checked into the repo) rather than only realizing after deploy that product data never existed on the production database.
