# 🚀 QuickBlog – A Minimal Blog Platform with UPI QR Payment Support

QuickBlog is a modern and lightweight Django-powered blog application that allows users to read, post, and interact with blogs — **plus a unique built-in UPI QR Code generator** for accepting donations or payments. Perfect for writers, creators, or organizations that want to share ideas and receive support seamlessly.

---

## ✨ Features

### 📝 Blog System
- Full blog CRUD using Django Admin
- Rich text editing with TinyMCE (for admin)
- Blog listing with pagination
- Detailed blog view with image support
- future scope for Readers :
  - ✅ Like blogs
  - 💬 Comment on blogs
  - ⭐ Save blogs to favorites
  - Favorites auto-cleaned if blog is deleted

### 💸 UPI QR Code Generator
- Custom form to enter UPI ID and amount
- Generates dynamic QR Code using Python’s `qrcode` library
- Scan-ready using Paytm/PhonePe/Google Pay (if UPI is active)
- Clean UI with Tailwind CSS
- Shows QR after generation for instant use

### 💬 Donation Form (Optional Module)
- Purpose & message input
- Sends message via email (using `send_mail`)
- Built for future integration (e.g., PayPal, Stripe)

---

## 🛠️ Tech Stack

| Layer         | Tech Used |
|---------------|-----------|
| Backend       | Python, Django 5.2.2 |
| Frontend      | HTML5, Tailwind CSS |
| Rich Text     | TinyMCE for admin blog editor |
| QR Code       | `qrcode`, `Pillow` |
| Email Support | Django `send_mail` function |
| Database      | SQLite (default) |
| Hosting       | PythonAnywhere / Localhost |

---
![image](https://github.com/user-attachments/assets/3f4d4387-ff7a-4704-87b4-f8acd57c08a5)
![image](https://github.com/user-attachments/assets/cd7a4af8-878f-4740-9c78-9be802710e53)
![image](https://github.com/user-attachments/assets/6a5ce338-9966-47f7-a153-54ee212243ba)
![image](https://github.com/user-attachments/assets/0e560919-ac46-4e61-9477-aaec66baefae)
![image](https://github.com/user-attachments/assets/82c55fbc-3e27-4154-b305-731c4afb6b94)






## 🧪 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/QuickBlog-Django.git
cd QuickBlog-Django

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

# 3. Install requirements
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start server
python manage.py runserver
